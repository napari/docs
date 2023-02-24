# ---- Standard library imports
import json
from pathlib import Path

# ---- Napari imports
from napari._qt.containers import qt_layer_list
from napari._qt.layer_controls import qt_layer_controls_container
from napari._qt.widgets import qt_viewer_status_bar
from napari._qt import menus
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
UI_SECTIONS_DOCS_ROOT_PATH = DOCS / "developers" / "ui_sections"

# Napari and Napari UI sections modules paths
NAPARI_ROOT_DIRECTORY_PATH = Path(qt_layer_list.__file__).parent.parent.parent
LAYER_LIST_MODULE_PATH = Path(qt_layer_list.__file__)
LAYER_CONTROLS_MODULE_PATH = Path(qt_layer_controls_container.__file__)
APPLICATION_STATUS_BAR_MODULE_PATH = Path(qt_viewer_status_bar.__file__)
APPLICATION_MENUS_MODULE_PATH = Path(menus.__file__)
VIEWER_MODULE_PATH = Path(qt_viewer.__file__)
DIALOGS_MODULE_PATH = Path(dialogs.__file__)
CONSOLE_MODULE_PATH = Path(qt_console.__file__)


# ---- Utility functions
def generate_dependencies_graph(options):
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
    dependencies_dict = json.loads(str(dependencies_graph))
    files_to_include = [
        Path(dependency["path"]) for dependency in dependencies_dict.values()
    ]

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
):
    dependencies_dict = json.loads(str(dependencies_graph))

    mermaid_diagram_content = "```{mermaid}\n"
    mermaid_diagram_content += f"graph {graph_orientation or 'LR'}\n"
    external_nodes = []
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
        if graph_urls_prefix:
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
            else:
                external_nodes.append(dep_name)
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
    mermaid_graph_direction,
):
    options = cli.parse_args(pydeps_args)
    (
        dep_graph,
        dot_src,
        pydeps_graph,
    ) = generate_dependencies_graph(options)
    mermaid_graph = generate_mermaid_diagram(
        dep_graph, **mermaid_graph_direction
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
    mermaid_graph_settings = {
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
        "--rankdir",
        "RL",
        "--exclude",
        "*experimental*",
        "*perf*",
        "*_qt.menus*",
        "*_qt.dialogs*",
        "*_qt.qt_event*",
        "*_qt.code_syntax_highlight*",
        "*_qt.containers.qt_tree*",
        "*_qt._qapp_model.qactions*",
        "*_qt.widgets.qt_viewer_status*",
        "*_qt.widgets.qt_dims*",
        "*_qt.widgets.qt_welcome*",
        "*_qt.widgets.qt_splash_screen*",
        "*_qt.widgets.qt_progress_bar*",
        "*components._viewer*",
        "*components.viewer*",
        "*components.overlay*",
        "*components.dims*",
        "*components.camera*",
        "*components.tooltip*",
        "*components.cursor*",
        "*components.Dims*",
        "*components.grid*",
        "napari.layers.*",
        "--exclude-exact",
        "napari._qt.widgets",
        "napari._qt.layer_controls",
        "napari._qt.qthreading",
        "--only",
        "napari._qt",
        "napari.components",
        "napari.layers",
        "--reverse",
        "--max-bacon",
        "4",
        "--show-deps",
        "--no-output",
    ]
    ui_sections.append(
        (
            layer_list_section_name,
            layer_list_output_page,
            layer_list_pydeps_args,
            mermaid_graph_settings,
        )
    )

    # ---- Layer controls section parameters
    layer_controls_section_name = "Layers controls"
    layer_controls_output_page = (
        UI_SECTIONS_DOCS_ROOT_PATH / "layers_controls_ui.md"
    )
    layer_controls_pydeps_args = [
        f"{LAYER_CONTROLS_MODULE_PATH}",
        "--rankdir",
        "RL",
        "--exclude",
        "*experimental*",
        "*perf*",
        "*_qt.menus*",
        "*_qt.dialogs*",
        "*_qt.qt_event*",
        "*_qt.code_syntax_highlight*",
        "*_qt._qapp_model*",
        "*_qt.qt_resources*",
        "*_qt.widgets.qt_viewer_status*",
        "*_qt.widgets.qt_dims*",
        "*_qt.widgets.qt_welcome*",
        "*_qt.widgets.qt_splash_screen*",
        "*_qt.widgets.qt_progress_bar*",
        "*_qt.widgets.qt_viewer_buttons*",
        "*components._viewer*",
        "*components.viewer*",
        "*components.overlay*",
        "*components.dims*",
        "*components.camera*",
        "*components.tooltip*",
        "*components.cursor*",
        "*components.Dims*",
        "*components.grid*",
        "napari.layers.*",
        "--exclude-exact",
        "napari._qt.widgets",
        "napari._qt.containers",
        "napari._qt.qthreading",
        "--only",
        "napari._qt",
        "napari.components",
        "napari.layers",
        "--reverse",
        "--max-bacon",
        "4",
        "--show-deps",
        "--no-output",
    ]
    ui_sections.append(
        (
            layer_controls_section_name,
            layer_controls_output_page,
            layer_controls_pydeps_args,
            mermaid_graph_settings,
        )
    )

    # ---- Application status bar section parameters
    application_status_bar_section_name = "Application status bar"
    application_status_bar_output_page = (
        UI_SECTIONS_DOCS_ROOT_PATH / "application_status_bar_ui.md"
    )
    application_status_bar_pydeps_args = [
        f"{APPLICATION_STATUS_BAR_MODULE_PATH}",
        "--rankdir",
        "RL",
        "--exclude",
        "*experimental*",
        "*perf*",
        "*_qt.qt_event*",
        "*_qt._qapp_model*",
        "--exclude-exact",
        "napari._qt.dialogs",
        "napari._qt.dialogs.qt_notification",
        "napari._qt.dialogs.confirm_close_dialog",
        "napari._qt.qt_resources",
        "napari._qt.widgets",
        "napari._qt.widgets.qt_viewer_dock_widget",
        "napari._qt.widgets.qt_splash_screen",
        "napari._qt.qt_viewer",
        "napari._qt.utils",
        "napari._qt.menus",
        "napari._qt.qthreading",
        "--only",
        "napari._qt",
        "napari.utils.progress",
        "--reverse",
        "--max-bacon",
        "3",
        "--show-deps",
        "--no-output",
    ]
    ui_sections.append(
        (
            application_status_bar_section_name,
            application_status_bar_output_page,
            application_status_bar_pydeps_args,
            mermaid_graph_settings,
        )
    )

    # ---- Application menus section parameters
    application_menus_section_name = "Application menus"
    application_menus_output_page = (
        UI_SECTIONS_DOCS_ROOT_PATH / "application_menus_ui.md"
    )
    application_menus_pydeps_args = [
        f"{APPLICATION_MENUS_MODULE_PATH}",
        "--rankdir",
        "RL",
        "--exclude",
        "*experimental*",
        "*perf*",
        "*_qt.qt_event*",
        "--exclude-exact",
        "napari._qt._qapp_model",
        "napari._qt.dialogs",
        "napari._qt.dialogs.qt_notification",
        "napari._qt.dialogs.confirm_close_dialog",
        "napari._qt.dialogs.qt_activity_dialog",
        "napari._qt.widgets.qt_viewer_dock_widget",
        "napari._qt.widgets.qt_viewer_status_bar",
        "napari._qt.widgets.qt_splash_screen",
        "napari._qt.qt_viewer",
        "napari._qt.qthreading",
        "napari._qt.utils",
        "--only",
        "napari._qt",
        "--reverse",
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
            mermaid_graph_settings,
        )
    )

    # ---- Viewer section parameters
    viewer_section_name = "Viewer"
    viewer_output_page = UI_SECTIONS_DOCS_ROOT_PATH / "viewer_ui.md"
    viewer_pydeps_args = [
        f"{VIEWER_MODULE_PATH}",
        "--rankdir",
        "RL",
        "--exclude",
        "*experimental*",
        "*perf*",
        "*_qt.qt_event*",
        "napari.layers.*",
        "napari._qt.containers.*",
        "napari._qt.layer_controls.*",
        "--exclude-exact",
        "napari._qt._qapp_model",
        "napari._qt.dialogs",
        "napari._qt.menus",
        "napari._qt.qt_resources",
        "napari._qt.widgets",
        "napari._qt.widgets.qt_splash_screen",
        "napari._qt.widgets.qt_viewer_status_bar",
        "napari.components",
        "--only",
        "napari._qt",
        "napari.components",
        "napari.layers",
        "--reverse",
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
            mermaid_graph_settings,
        )
    )

    # ---- Dialogs section parameters
    dialogs_section_name = "Dialogs"
    dialogs_output_page = UI_SECTIONS_DOCS_ROOT_PATH / "dialogs_ui.md"
    dialogs_pydeps_args = [
        f"{DIALOGS_MODULE_PATH}",
        "--rankdir",
        "RL",
        "--exclude",
        "*experimental*",
        "*perf*",
        "*_qt.containers*",
        "*_qt.menus.debug*",
        "*_qt.menus.window_menu*",
        "*_qt.layer_controls*",
        "*_qt.qt_event*",
        "--exclude-exact",
        "napari._qt._qapp_model",
        "napari._qt._qapp_model._menus",
        "napari._qt._qapp_model.qactions",
        "napari._qt._qapp_model.qactions._view",
        "napari._qt.dialogs",
        "napari._qt.menus._util",
        "napari._qt.utils",
        "napari._qt.widgets",
        "napari._qt.widgets.qt_dims",
        "napari._qt.widgets.qt_dims_sorter",
        "napari._qt.widgets.qt_splash_screen",
        "napari._qt.widgets.qt_spinbox",
        "napari._qt.widgets.qt_viewer_buttons",
        "napari._qt.widgets.qt_viewer_dock_widget",
        "napari._qt.widgets.qt_welcome",
        "--only",
        "napari._qt",
        "--reverse",
        "--max-bacon",
        "5",
        "--show-deps",
        "--no-output",
    ]
    ui_sections.append(
        (
            dialogs_section_name,
            dialogs_output_page,
            dialogs_pydeps_args,
            mermaid_graph_settings,
        )
    )

    # ---- Napari-console section parameters
    console_section_name = "Console (napari-console)"
    console_output_page = UI_SECTIONS_DOCS_ROOT_PATH / "console_ui.md"
    console_pydeps_args = [
        f"{CONSOLE_MODULE_PATH}",
        "--rankdir",
        "RL",
        "--exclude",
        "*experimental*",
        "*perf*",
        "napari.utils*",
        "napari._vendor*",
        "napari.resources*",
        "--exclude-exact",
        "napari",
        "napari._lazy",
        "napari._version",
        "napari._qt.qt_event_loop",
        "napari._qt.widgets",
        "napari._qt.qt_resources",
        "napari.qt.threading",
        "--only",
        "napari",
        "napari_console",
        "napari_plugin_engine",
        "--reverse",
        "--max-bacon",
        "3",
        "--show-deps",
        "--no-output",
    ]
    ui_sections.append(
        (
            console_section_name,
            console_output_page,
            console_pydeps_args,
            mermaid_graph_settings,
        )
    )

    try:
        for (
            section_name,
            output_page,
            pydeps_args,
            mermaid_graph_direction,
        ) in ui_sections:
            generate_docs_ui_section(
                section_name,
                output_page,
                pydeps_args,
                mermaid_graph_direction,
            )
    except OSError:
        # dot executable unavailable.
        pass


if __name__ == "__main__":
    # ---- Call main
    main()
