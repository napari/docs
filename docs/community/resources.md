(napari-resources)=

# napari resources

Logos, colors, and other brand resources for the napari project live in the
[napari-resources repository](https://github.com/napari/napari-resources).
Make sure to read the
[license and usage guidelines](https://github.com/napari/napari-resources#permissions-and-usage-guidelines)
before using any of these in your own work.

## napari logo

![napari logo designs](https://github.com/napari/napari-resources/releases/latest/download/montage.png)

To download the latest logos as SVG or PNG files, head to the
[latest release page](https://github.com/napari/napari-resources/releases/latest).

The logos are also available as a Python package, which is useful for
including them in your own application or plugin:

```sh
pip install napari-resources
```

```python
from napari_resources import logo_path

svg = logo_path('gradient-plain-dark.svg')
```

See the
[napari-resources README](https://github.com/napari/napari-resources#readme)
for the full list of logo variants and how to render them to an image.

## Website colors

Below is the list of colors used in the napari website.

- primary blue: #80d1ff
- deep blue: #009bf2
- light blue: #d2efff
- dark gray: #686868
- gray: #f7f7f7

For dark mode, we use two additional colors:

- purple: #4d485c
- dark blue: #526a77

See more details in the
[napari-sphinx-theme colors page](https://napari.org/napari-sphinx-theme/colors.html).
