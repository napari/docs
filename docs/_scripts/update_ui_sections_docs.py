# ---- Standard library imports
import json
from pathlib import Path

# ---- Napari imports
from napari._qt.containers import qt_layer_list
from napari._qt.layer_controls import qt_layer_controls_container
from napari._qt.widgets import qt_viewer_status_bar
from napari._qt._qapp_model import qactions
from napari._qt import qt_viewer
from napari._qt import dialogs
from napari_console import qt_console

# ---- Third-party imports
from pydeps import cli, colors, dot, py2depgraph
from pydeps.pydeps import depgraph_to_dotsrc
from pydeps.target import Target
import seedir as sd

# ---- General constants
# Docs paths
DOCS = Path(__file__).parent.parent
UI_SECTIONS_DOCS_ROOT_PATH = DOCS / "developers" / "architecture" / "ui_sections"

# Napari and Napari UI sections modules paths
NAPARI_ROOT_DIRECTORY_PATH = Path(qt_layer_list.__file__).parent.parent.parent
LAYER_LIST_MODULE_PATH = Path(qt_layer_list.__file__)
LAYER_CONTROLS_MODULE_PATH = Path(qt_layer_controls_container.__file__)
APPLICATION_STATUS_BAR_MODULE_PATH = Path(qt_viewer_status_bar.__file__)
APPLICATION_MENUS_MODULE_PATH = Path(qactions.__file__)
VIEWER_MODULE_PATH = Path(qt_viewer.__file__)
DIALOGS_MODULE_PATH = Path(dialogs.__file__).parent
CONSOLE_MODULE_PATH = Path(qt_console.__file__).parent


# ---- Utility functions
def generate_dependencies_graph(options):
    """
    Generate the module dependency analysis for the given options.

    The options follow the arguments that the pydeps package CLI supports.

    Parameters
    ----------
    options : dict
        Dictionary with the pydeps CLI arguments to use.

    Returns
    -------
    dep_graph : DepGraph
        Result dependency graph constructed by pydeps.
    dot_src : str
        Result dependency graph description using .dot format.
        It can return `None` depending on the options passed.
    graph_content : bytes
        Result dependency graph in binary format.
        It can return `None` depending on the options passed.

    """
    colors.START_COLOR = options["start_color"]
    target = Target(options["fname"])
    with target.chdir_work():
        dep_graph = py2depgraph.py2dep(target, **options)
    dot_src = depgraph_to_dotsrc(target, dep_graph, **options)
    graph_content = None
    if not options["no_output"]:
        graph_content = dot.call_graphviz_dot(dot_src, options["format"])
        if options["output"]:
            output_file = Path(options["output"])
            output_file.parent.mkdir(exist_ok=True, parents=True)
            output_file.write_bytes(graph_content)
    return dep_graph, dot_src, graph_content


def generate_directory_layout(
    dependencies_graph,
    root_directory=NAPARI_ROOT_DIRECTORY_PATH,
    output_file=None,
):
    """
    Generate the code base related directory layout given the module
    dependencies graph.

    Parameters
    ----------
    dependencies_graph : DepGraph
        Dependency graph constructed by pydeps.
    root_directory : Path, optional
        Path to the root directory where the modules are located.
        The default is NAPARI_ROOT_DIRECTORY_PATH.
    output_file : str, optional
        Path to file to write with the directory layout output.
        The default is None.

    Returns
    -------
    directory_layout_content: str
        The directory layout generated.

    """
    dependencies_dict = json.loads(str(dependencies_graph))
    files_to_include = []
    for dependency in dependencies_dict.values():
        if dependency["path"]:
            files_to_include.append(Path(dependency["path"]))

    def directory_layout_mask(item):
        item_path = Path(item)
        if item in files_to_include:
            return True
        elif item_path.is_dir():
            for file_to_include in files_to_include:
                if Path(file_to_include).is_relative_to(item_path):
                    return True
        else:
            return False

    directory_layout_content = "```\n"
    directory_layout_content += (
        sd.seedir(
            path=root_directory,
            style="lines",
            printout=False,
            mask=directory_layout_mask,
        )
        + "\n"
    )
    directory_layout_content += "```\n"

    if output_file:
        output_file = Path(output_file)
        output_file.parent.mkdir(exist_ok=True, parents=True)
        output_file.write_text(directory_layout_content, encoding="utf-8")

    return directory_layout_content


def generate_mermaid_diagram(
    dependencies_graph,
    graph_orientation="LR",
    graph_node_default_style=None,
    graph_node_external_style=None,
    graph_link_default_style=None,
    graph_urls_prefix=None,
    graph_title=None,
    graph_description=None,
):
    """
    Generate a mermaid diagram given a dependencies diagram and a set of
    options.

    Parameters
    ----------
    dependencies_graph : DepGraph
        Dependency graph constructed by pydeps.
    graph_orientation : str, optional
        The orientation of the graph to be created and supported by mermaid.
        For more info see:
            https://mermaid.js.org/syntax/flowchart.html#flowchart-orientation
        The default is "LR".
    graph_node_default_style : str, optional
        The default style that should be used for the graph nodes/vertices by
        mermaid. For more info see:
            https://mermaid.js.org/syntax/flowchart.html#styling-and-classes
        The default is None.
    graph_node_external_style : str, optional
        The style that should be used for the graph nodes/vertices by mermaid
        that are detected as external modules. For more info see:
            https://mermaid.js.org/syntax/flowchart.html#styling-and-classes
        The default is None.
    graph_link_default_style : str, optional
        The default style that should be used for the graph edges/links by
        mermaid. For more info see:
            https://mermaid.js.org/syntax/flowchart.html#styling-and-classes
        The default is None.
    graph_urls_prefix : str, optional
        The base url used to add links to the nodes/vertices in the graph.
        For more info see:
            https://mermaid.js.org/syntax/flowchart.html#interaction
        The default is None.
    graph_title : str, optional
        Accessible title for the graph. For more info see:
            https://mermaid.js.org/config/accessibility.html#accessible-title-and-description
        The default is None.
    graph_description : str, optional
        Accessible description for the graph. The default is None.

    Returns
    -------
    mermaid_diagram_content : str
        The mermaid diagram.

    """
    dependencies_dict = json.loads(str(dependencies_graph))
    mermaid_diagram_content = "```{mermaid}\n"
    mermaid_diagram_content += f"graph {graph_orientation or 'LR'}\n"
    if graph_title:
        mermaid_diagram_content += f"\taccTitle: {graph_title}\n"
    if graph_description:
        mermaid_diagram_content += f"\taccDescr: {graph_description}\n"
    external_nodes = []
    subgraphs = {}
    for dependency in dependencies_dict.values():
        dep_name = dependency["name"]
        mermaid_diagram_content += f"\t{dep_name}({dep_name})\n"
        if "imports" in dependency:
            dep_imports = dependency["imports"]
            for dep_import_name in dep_imports:
                if (
                    dep_import_name != dep_name
                    and dep_import_name not in dep_name
                ):
                    mermaid_diagram_content += (
                        f"\t{dep_name} --> {dep_import_name}\n"
                    )
        if graph_urls_prefix and dependency["path"]:
            module_path = Path(dependency["path"])
            # Check if module is outside napari, like
            # a plugin such as `napari_console`
            if module_path.is_relative_to(NAPARI_ROOT_DIRECTORY_PATH):
                module_relative_path = module_path.relative_to(
                    NAPARI_ROOT_DIRECTORY_PATH
                ).as_posix()
                module_url = f"{graph_urls_prefix}{module_relative_path}"
                mermaid_diagram_content += (
                    f'\tclick {dep_name} "{module_url}" _blank\n'
                )
                dep_name_parent = ".".join(dep_name.split(".")[:-1])
                if dep_name_parent not in subgraphs:
                    subgraphs[dep_name_parent] = [dep_name]
                else:
                    subgraphs[dep_name_parent].append(dep_name)
            else:
                external_nodes.append(dep_name)

    for subgraph_key, subgraph_value in subgraphs.items():
        mermaid_diagram_content += (
            f"\tsubgraph module.{subgraph_key}[{subgraph_key}]\n"
        )
        for dep_subgraph_name in subgraph_value:
            mermaid_diagram_content += f"\t\t {dep_subgraph_name}\n"
        mermaid_diagram_content += "\tend\n"
        mermaid_diagram_content += f"\tclass module.{subgraph_key} subgraphs\n"

    if external_nodes:
        mermaid_diagram_content += (
            "\tsubgraph module.external[external]\n"
        )
        for external_node in external_nodes:
            mermaid_diagram_content += f"\t\t {external_node}\n"
        mermaid_diagram_content += "\tend\n"
        mermaid_diagram_content += "\tclass module.external subgraphs\n"

    if subgraphs:
        mermaid_diagram_content += (
            "\tclassDef subgraphs fill:white,strock:black,color:black;"
        )
    if graph_node_default_style:
        mermaid_diagram_content += (
            f"\tclassDef default {graph_node_default_style}\n"
        )
    if graph_link_default_style:
        mermaid_diagram_content += (
            f"\tlinkStyle default {graph_link_default_style}\n"
        )
    if graph_node_external_style:
        mermaid_diagram_content += (
            f"\tclassDef external {graph_node_external_style}\n"
        )
        for external_dep in external_nodes:
            mermaid_diagram_content += f"\tclass {external_dep} external\n"

    mermaid_diagram_content += "```\n"

    return mermaid_diagram_content


def generate_docs_ui_section_page(
    section_name,
    mermaid_diagram,
    directory_layout,
    output_file=None,
):
    """
    Generate the markdown page content for a UI section.

    The generated content consists of a title, a dependencies diagram and
    a directory layout.

    Both, dependencies diagram and directory layout, have a subtitle
    before them.

    Parameters
    ----------
    section_name : str
        The name of the UI section. It will be used as the page title.
    mermaid_diagram : str
        DESCRIPTION.
    directory_layout : str
        DESCRIPTION.
    output_file : Path, optional
        Path to file where the content should be written. The default is None.

    Returns
    -------
    page_content : str
        The UI section page content.

    """
    page_content = f"## {section_name}\n"
    page_content += "### Dependencies diagram (related `napari` modules)\n"
    page_content += mermaid_diagram
    page_content += "### Source code directory layout (related to modules inside `napari`)\n"
    page_content += directory_layout
    if output_file:
        output_file.parent.mkdir(exist_ok=True, parents=True)
        output_file.write_text(page_content, encoding="utf-8")

    return page_content


def generate_docs_ui_section(
    section_name,
    output_page,
    pydeps_args,
    mermaid_graph_base_properties,
):
    """
    Generate the needed content for a UI section page as well as a formatted
    page for the section.

    Parameters
    ----------
    section_name : str
        The name of the UI section.
    output_page : Path
        Path to file where the generated page content will be written.
    pydeps_args : list
        List with the arguments that will be passed to pydeps.
    mermaid_graph_base_properties : dict
        Dictionary with the base configuration needed to generate a mermaid
        diagram.

    Returns
    -------
    dep_graph : DepGraph
        DESCRIPTION.
    dot_src : str
        Dot description of the generated dependencies graph.
    pydeps_graph : bytes
        Generated dependencies graph by pydeps.
    mermaid_graph : str
        Generated mermaid graph.
    dir_layout : str
        Generated directory layout of the UI section.
    ui_page : str
        Content of generated UI section page.

    """
    options = cli.parse_args(pydeps_args)
    (
        dep_graph,
        dot_src,
        pydeps_graph,
    ) = generate_dependencies_graph(options)
    graph_title = (
        f"Dependencies between modules in the napari {section_name} UI section"
    )
    graph_description = (
        "Diagram showing the dependencies between the modules "
        f"involved in the definition of the napari {section_name} UI section"
    )
    mermaid_graph = generate_mermaid_diagram(
        dep_graph,
        **mermaid_graph_base_properties,
        graph_title=graph_title,
        graph_description=graph_description,
    )
    dir_layout = generate_directory_layout(dep_graph)
    ui_page = generate_docs_ui_section_page(
        section_name,
        mermaid_graph,
        dir_layout,
        output_page,
    )
    return dep_graph, dot_src, pydeps_graph, mermaid_graph, dir_layout, ui_page


# ---- Main and UI sections parameters
def main():
    # General 'settings'
    mermaid_graph_base_settings = {
        "graph_orientation": "LR",
        "graph_node_default_style": "fill:#00c3ff,color:black;",
        "graph_node_external_style": "fill:#ffa600,color:black;",
        "graph_link_default_style": "stroke:#00c3ff",
        "graph_urls_prefix": "https://github.com/napari/napari/tree/main/napari/",
    }
    ui_sections = []

    # ---- Layer list section parameters
    layer_list_section_name = "Layers list"
    layer_list_output_page = UI_SECTIONS_DOCS_ROOT_PATH / "layers_list_ui.md"
    layer_list_pydeps_args = [
        f"{LAYER_LIST_MODULE_PATH}",
        "--exclude",
        "*_qt.qt_event*",
        "*_qt.containers.qt_tree*",
        "*_qt.containers.qt_axis*",
        "*components._viewer*",
        "*components.viewer*",
        "*components.dims*",
        "*components.camera*",
        "*components.LayerList",
        # "napari.layers.*",
        "--exclude-exact",
        "napari._qt._qapp_model.qactions._debug",
        "napari._qt._qapp_model.qactions._file",
        "napari._qt._qapp_model.qactions._view",
        "napari._qt._qapp_model.qactions._plugins",
        "napari._qt._qapp_model.qactions._window",
        "napari._qt._qapp_model.qactions._layers_actions",
        "napari._qt._qapp_model.qactions._help",
        "napari._qt.layer_controls",
        "napari._qt.containers",
        "napari.components",
        "napari._qt",
        "napari._qt._qapp_model.injection",
        "--only",
        "napari._qt",
        "napari.components",
        "napari.layers",
        "--show-deps",
        "--no-output",
    ]
    ui_sections.append(
        (
            layer_list_section_name,
            layer_list_output_page,
            layer_list_pydeps_args,
            mermaid_graph_base_settings,
        )
    )

    # ---- Layer controls section parameters
    layer_controls_section_name = "Layers controls"
    layer_controls_output_page = (
        UI_SECTIONS_DOCS_ROOT_PATH / "layers_controls_ui.md"
    )
    layer_controls_pydeps_args = [
        f"{LAYER_CONTROLS_MODULE_PATH}",
        "--exclude",
        "*qt_event_loop",
        "napari.layers.*",
        "*components*",
        "*qt_event_tracing*",
        "*qt_event_filters*",
        "*dialogs*",
        "*app_model*",
        "*utils",
        "*status*",
        "*thread*",
        "*perf",
        "*resources",
        "*qplugins",
        "--exclude-exact",
        "napari._qt.widgets",
        "--only",
        "napari._qt",
        "napari.components",
        "napari.layers",
        "napari.viewer",
        "--max-bacon",
        "3",
        "--show-deps",
        "--no-output",
    ]
    ui_sections.append(
        (
            layer_controls_section_name,
            layer_controls_output_page,
            layer_controls_pydeps_args,
            mermaid_graph_base_settings,
        )
    )

    # ---- Application status bar section parameters
    application_status_bar_section_name = "Application status bar"
    application_status_bar_output_page = (
        UI_SECTIONS_DOCS_ROOT_PATH / "application_status_bar_ui.md"
    )
    application_status_bar_pydeps_args = [
        f"{APPLICATION_STATUS_BAR_MODULE_PATH}",
        "--exclude",
        "*qt_viewer_dock_widget",
        "napari._qt._qapp_model*",
        "*qt_event_loop",
        "*_qplugins",
        "*utils",
        "*qt_resources*",
        "*preferences_dialog",
        "*screenshot_dialog",
        "*qt_viewer",
        "*confirm_close_dialog",
        "*qt_notification",
        "--exclude-exact",
        "napari._qt.threads",
        "napari._qt.widgets",
        "napari._qt.dialogs",
        "--only",
        "napari._qt",
        "napari.utils.progress",
        "napari.viewer",
        "--show-deps",
        "--no-output",
    ]
    ui_sections.append(
        (
            application_status_bar_section_name,
            application_status_bar_output_page,
            application_status_bar_pydeps_args,
            mermaid_graph_base_settings,
        )
    )

    # ---- Application menus section parameters
    application_menus_section_name = "Application menus"
    application_menus_output_page = (
        UI_SECTIONS_DOCS_ROOT_PATH / "application_menus_ui.md"
    )
    application_menus_pydeps_args = [
        f"{APPLICATION_MENUS_MODULE_PATH}",
        "--exclude",
        "*qt_event_loop*",
        "*utils*",
        "*qt_resources*",
        "*containers*",
        "*experimental*",
        "*perf*",
        "*qt_welcome*",
        "*qt_viewer_dock_widget*",
        "*qt_viewer_status_bar*",
        "*qt_dims*",
        "*_qplugins*",
        "*qt_event_filters*",
        "*threads*",
        "*layer_controls*",
        "*qt_notification*",
        "*qt_activity_dialog*",
        "*qt_progress_bar",
        "*qt_spinbox",
        "*qt_splash_screen",
        "*qt_tooltip",
        "--exclude-exact",
        "napari._qt.widgets",
        "napari._qt.dialogs",
        "napari._qt._qapp_model",
        "napari._qt._qapp_model.injection",
        "napari._qt._qapp_model._menus",
        "--only",
        "napari._qt",
        "napari.viewer",
        "--max-bacon",
        "3",
        "--show-deps",
        "--no-output",
    ]
    ui_sections.append(
        (
            application_menus_section_name,
            application_menus_output_page,
            application_menus_pydeps_args,
            mermaid_graph_base_settings,
        )
    )

    # ---- Viewer section parameters
    viewer_section_name = "Viewer"
    viewer_output_page = UI_SECTIONS_DOCS_ROOT_PATH / "viewer_ui.md"
    viewer_pydeps_args = [
        f"{VIEWER_MODULE_PATH}",
        "--exclude",
        "*experimental*",
        "*perf*",
        "*plugins*",
        "*Dims",
        "*_qt.qt_event*",
        "napari.layers.*",
        "napari._qt.containers.*",
        "napari._qt.layer_controls.*",
        "napari._qt.dialogs.*",
        "--exclude-exact",
        "napari._qt._qapp_model",
        "napari._qt.menus",
        "napari._qt.qt_resources",
        "napari._qt.widgets",
        "napari._qt.widgets.qt_splash_screen",
        "napari.components",
        "napari._qt",
        "--only",
        "napari._qt",
        "napari.components",
        "napari.layers",
        "--max-bacon",
        "3",
        "--show-deps",
        "--no-output",
    ]
    ui_sections.append(
        (
            viewer_section_name,
            viewer_output_page,
            viewer_pydeps_args,
            mermaid_graph_base_settings,
        )
    )

    # ---- Dialogs section parameters
    dialogs_section_name = "Dialogs"
    dialogs_output_page = UI_SECTIONS_DOCS_ROOT_PATH / "dialogs_ui.md"
    dialogs_pydeps_args = [
        f"{DIALOGS_MODULE_PATH}",
        "--exclude",
        "*test*",
        "*containers*",
        "*experimental*",
        "*layer_controls*",
        "*perf*",
        "*thread*",
        "*qactions._window",
        "*qactions._layerlist_context",
        "*qactions._layers_actions",
        "*qactions._view",
        "*qactions._toggle_action",
        "*splash*",
        "*theme*",
        "*keyboard*",
        "*popup*",
        "*event*",
        "*dock_widget*",
        "*welcome*",
        "*viewer_buttons",
        "*mode_buttons",
        "*dict_table",
        "*slider_compat",
        "*size_preview",
        "*darkdetect*",
        "*resources*",
        "--exclude-exact",
        "napari._qt.dialogs",
        "napari._vendor",
        "napari._qt",
        "napari._qt.widgets",
        "napari._qt._qapp_model",
        "napari._qt._qapp_model.injection",
        "napari._qt._qplugins",
        "--only",
        "napari._qt",
        "napari._vendor",
        "--show-deps",
        "--no-output",
    ]
    ui_sections.append(
        (
            dialogs_section_name,
            dialogs_output_page,
            dialogs_pydeps_args,
            mermaid_graph_base_settings,
        )
    )

    # ---- Napari-console section parameters
    console_section_name = "Console (napari-console)"
    console_output_page = UI_SECTIONS_DOCS_ROOT_PATH / "console_ui.md"
    console_pydeps_args = [
        f"{VIEWER_MODULE_PATH}",
        "--only",
        "napari.components._viewer_key_bindings",
        "napari.components.viewer",
        "napari.viewer",
        "napari.utils.notifications",
        "napari._qt.qt_viewer",
        "napari._qt.widgets.qt_viewer_buttons",
        "napari._qt._qapp_model.qactions._window",
        "napari._qt.qt_main_window",
        "napari_console",
        "--show-deps",
        "--no-output",
    ]
    ui_sections.append(
        (
            console_section_name,
            console_output_page,
            console_pydeps_args,
            mermaid_graph_base_settings,
        )
    )

    for (
        section_name,
        output_page,
        pydeps_args,
        mermaid_graph_base_settings,
    ) in ui_sections:
        generate_docs_ui_section(
            section_name,
            output_page,
            pydeps_args,
            mermaid_graph_base_settings,
        )


if __name__ == "__main__":
    # ---- Call main
    main()
