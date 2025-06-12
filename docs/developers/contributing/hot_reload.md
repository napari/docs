(napari-translations)=

# Hot Reloading in Development Mode

When working on napari itself or developing plugins, manually restarting the application after every code change can quickly become tedious. To speed up the development cycle, napari supports **hot-reloading**, allowing you to reload code changes on the fly without closing and reopening the app.

## What is Hot Reloading?

Hot reloading enables napari to automatically reload Python modules during runtime, making development significantly more efficient. With this feature enabled, you can:

* Make changes to the napari or napari-builtins source code
* Or make changes to **your** plugin source code (use `--dev_module YOUR_PLUGIN_NAME` to add to list of watched modules)
* Instantly see those changes reflected in the running app
* Avoid repetitive app restarts

Under the hood, this feature uses [qtreload](https://github.com/lukasz-migas/qtreload) a module reloader tailored for Qt-based Python applications.

```{raw} html
<figure>
  <video width="100%" controls autoplay loop muted playsinline>
    <source src="../../_static/images/hot_reload_qss.webm" type="video/webm" />
    <source src="../../_static/images/hot_reload_qss.mp4" type="video/mp4" />
    <img src="../../_static/images/hot_reload_qss.png"
      title="Your browser does not support the video tag"
      alt="PyCharm window and napari viewer side by side. The Pycharm window shows a code editor with a QSS file being edited. Once file is saved, the napari
      stylesheet is reloaded and napari viewer is updated with the new style."
    >
  </video>
</figure>
```

```{raw} html
<figure>
  <video width="100%" controls autoplay loop muted playsinline>
    <source src="../../_static/images/hot_reload_py.webm" type="video/webm" />
    <source src="../../_static/images/hot_reload_py.mp4" type="video/mp4" />
    <img src="../../_static/images/hot_reload_py.png"
      title="Your browser does not support the video tag"
      alt="PyCharm window and napari viewer side by side. The Pycharm window shows a code editor with a Python file being edited. Once file is saved, the user opens a popup window which was updated and the layout has been changed to include a new QLabel. This is repeated again to show that the changes are
      applied immediately without restarting napari."
    >
  </video>
</figure>
```

## How to Enable Hot Reloading

Hot relaoding is enabled when napari is launched in **developer mode**. You can activate developer mode in one of two ways:

### Option 1: Command Line Flag

```bash
napari --dev
```

This will set the environment flag so that the `qtreload` widget is activated.

### Option 2: Environment Variable

The `NAPARI_DEV` environment variable can be set to enable developer mode:

```bash
# set environment variable
export NAPARI_DEV=1
# launch napari
napari
```

This is especially useful if you prefer to use your own Python scripts to launch napari.

## Hot Reloading Your Plugin

By default, hot reloading only applies to the napari core libraries (napari and napari-builtins). IF you're working on a plugin and want your changes. to reload as well, you'll need to explicitly include it when launching napari.

### Option 1: Command Line Flag
Use the --dev_module flag to specify additional modules to reload:

```bash
napari --dev --dev_module my_plugin
```

You can add this flag multiple times if you are working on more than one module:

```bash
napari --dev --dev_module my_plugin --dev_module my_other_module
```

### Option 2: Environment Variable

The `NAPARI_DEV_MODULES` environment variable can be used to specify a comma-separated list of modules to watch for changes:

```bash
# set environment variable
export NAPARI_DEV=1
export NAPARI_DEV_MODULES=my_plugin,my_other_module
# launch napari
napari
```

```{admonition} Plugin/module installation
:class: tip

Your plugin/module must already be installed in the environment (e.g. via `pip install -e .` for this to work).
```

## How It Works

The `qtreload` system monitors changes to registered modules and reloads them using Python’s import machinery. It watches for changes to the `.py` and `.qss`.

When `.py` file changes, it reloads the file. Here are some useful rules to keep in mind:

* If you've **added** a new function, that function will be added to the class/object.
* If you've **updated** a function, it should just work without issues.
* If you've **added** a new property, that property will be added to the class/object.
* If you've **edited** a property, that change might not be reflected
* If you've **edited** UI, that change will only take effect if you close and reopen the widget that was changed (so main windows will not be changed but if you edit a container for a layer type and then remove and add that layer, the change **will** be reflected)
* code within the `__init__.py` file cannot be reloaded (sorry)
* new files are not actively watched - you can manually reload the list of files

When `.qss` file changes, it emits an event which is handled by the application - in napari's case, it simply reloads the stylesheet and applies it to the entire application.