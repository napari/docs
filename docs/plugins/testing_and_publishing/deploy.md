(plugin-deploy)=
# Publish your plugin

## Preparing for release

To help users find your plugin, make sure to use the `Framework :: napari`
[classifier] in your package's core metadata. (If you used the cookiecutter,
this has already been done for you.)

Once your package is listed on [PyPI] (and includes the `Framework :: napari`
[classifier]), it will also be visible on the [napari
hub](https://napari-hub.org/). To ensure you are providing the relevant metadata and
description for your plugin, see the following documentation in the [napari hub
GitHub](https://github.com/chanzuckerberg/napari-hub/tree/main/docs)’s docs
folder:

- [Customizing your plugin’s
  listing](https://github.com/chanzuckerberg/napari-hub/blob/main/docs/customizing-plugin-listing.md)
- [Writing the perfect description for your
  plugin](https://github.com/chanzuckerberg/napari-hub/blob/main/docs/writing-the-perfect-description.md)

```{admonition} The hub
For more about the napari hub, see the [napari hub About
page](https://www.napari-hub.org/about). To learn more about the hub’s
development process, see the [napari hub GitHub’s
Wiki](https://github.com/chanzuckerberg/napari-hub/wiki).

If you want your plugin to be available on PyPI, but not visible on the napari
hub, you can add a `.napari/config.yml` file to the root of your repository with
a visibility key. For details, see the [customization
guide][hub-guide-custom-viz].
```

Finally, once you have curated your package metadata and description, you can
preview your metadata, and check any missing fields using the
napari hub preview page service. Check out [this guide](https://github.com/chanzuckerberg/napari-hub/blob/main/docs/setting-up-preview.md) for instructions on how to set it up.

## Deployment

When you are ready to share your plugin, [upload the Python package to
PyPI][pypi-upload] after which it will be installable using `python -m pip install
<yourpackage>`, or (assuming you added the `Framework :: napari` classifier)
in the builtin plugin installer dialog.

If you used the {ref}`plugin-cookiecutter-template`, you can also
[setup automated deployments][autodeploy] on github for every tagged commit.

````{admonition} What about conda?
While you are free to distribute your plugin on anaconda cloud in addition to
or instead of PyPI, the built-in napari plugin installer doesn't currently install
from conda. In this case, you may guide your users to install your package on the
command line using conda in your readme or documentation.

A future version of napari and the napari stand-alone application may support
directly installing from conda. As such, publishing to conda-forge can be a good
idea. Checkout [deploying to anaconda](deploying-to-anaconda) for more details.
````

When you are ready for users, announce your plugin on the [Image.sc
forum](https://forum.image.sc/tag/napari).


[classifier]: https://pypi.org/classifiers/
[pypi]: https://pypi.org/
[pypi-upload]: https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives
[hubguide]: https://github.com/chanzuckerberg/napari-hub/blob/main/docs/customizing-plugin-listing.md
[hub-guide-custom-viz]: https://github.com/chanzuckerberg/napari-hub/wiki/Customizing-your-plugin's-listing#visibility
[hub-guide-preview]: https://github.com/chanzuckerberg/napari-hub/blob/main/docs/setting-up-preview.md
[autodeploy]: https://github.com/napari/cookiecutter-napari-plugin#set-up-automatic-deployments
