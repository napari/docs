# napari 0.1.0

We're happy to announce the release of napari 0.1.0! napari is a fast,
interactive, multi-dimensional image viewer for Python. It's designed for
browsing, annotating, and analyzing large multi-dimensional images. It's built
on top of Qt (for the GUI), vispy (for performant GPU-based rendering), and the
scientific Python stack (numpy, scipy).

This is our first minor release, timed for the 2019 SciPy Conference in Austin.
It marks our transition from pre-alpha to alpha, and establishes a reasonable
API for adding images, shapes, and other basic layer types to an interactive
viewer. It supports launching a viewer with python scripting or from Jupyter
notebooks.

For more information, examples, and documentation, please visit our website:
https://github.com/napari/napari

## Pull Requests

- Add shapes ({pr}`100`)
- Vectors Layer ({pr}`129`)
- setup css basics ({pr}`167`)
- Update shields on README ({pr}`169`)
- Add dimension sliders ({pr}`171`)
- New more convenient ViewerApp API ({pr}`172`)
- WIP: Labels layer ({pr}`175`)
- automate running/testing of examples ({pr}`176`)
- fix error with nD markers ({pr}`183`)
- fix sphinx-apidoc command on CONTRIBUTING.MD ({pr}`187`)
- Allow other array-like data ({pr}`188`)
- Add example using a Zarr array ({pr}`191`)
- readme updates ({pr}`192`)
- fix empty markers ({pr}`194`)
- Interactive labels ({pr}`195`)
- improve layer selection / name editing ({pr}`196`)
- Rasterize shapes ({pr}`197`)
- Fix color map to work with unlimited labels. ({pr}`203`)
- Make clim range an input argument ({pr}`205`)
- Use triangles for vectors ({pr}`215`)
- support clipping appropriately ({pr}`216`)
- fix nD fill ({pr}`217`)
- fix nD paint ({pr}`218`)
- vectors layer speed up ({pr}`219`)
- Generate svg from shapes layer ({pr}`220`)
- allow for other arrays used with labels ({pr}`228`)
- fix drawing lines in shapes layer ({pr}`230`)
- fix empty polygons in shapes layer ({pr}`231`)
- add support for custom key bindings ({pr}`232`)
- Deduplicate marker symbols ({pr}`233`)
- switch to qtpy ({pr}`235`)
- new styles ({pr}`236`)
- add support for settable viewer title ({pr}`237`)
- fix escape selecting shape error ({pr}`242`)
- updated screenshots ({pr}`244`)
- unify titlebar ({pr}`245`)
- refactor layers list ({pr}`246`)
- remove app ({pr}`247`)
- fix range slider imports ({pr}`248`)
- Refactor layer indices and coords ({pr}`249`)
- remove example data utils file ({pr}`250`)
- theme setting ({pr}`253`)
- layer active when only one selected ({pr}`257`)
- tiny theme related fixes ({pr}`258`)
- Viewer to svg ({pr}`259`)
- Fix svg canvas ({pr}`264`)
- remove async utils ({pr}`267`)
- refactor draggable layers ({pr}`271`)
- fix bbox call on new markers ({pr}`272`)
- fix default selection logic ({pr}`273`)
- add layer viewer update events ({pr}`274`)
- flip markers ({pr}`275`)
- fix markers sizing ({pr}`276`)
- fix blending update ({pr}`277`)
- fix int clim value ({pr}`278`)
- remove viewer from individual layer object ({pr}`279`)
- Black formatter PR ({pr}`282`)
- revert layers list ({pr}`284`)
- fix image dims update ({pr}`288`)
- fix status updates on dims changes ({pr}`289`)
- Refactor viewer syntax ({pr}`290`)
- Simplify the colormaps list and add the single-color colormaps ({pr}`291`)
- Remove qtviewer from viewer ({pr}`292`)
- refactor theme setting ({pr}`293`)
- Pyramid layer ({pr}`295`)
- Nd shapes ({pr}`297`)
- WIP: Stop using add_to_viewer syntax for basic layers ({pr}`303`)
- fix click on layer list ({pr}`306`)
- use stylesheet for styling of range slider ({pr}`307`)
- Unify layer mode Enums ({pr}`311`)
- Thumbnails ({pr}`314`)
- fix remove layer ({pr}`315`)
- Blending Enum ({pr}`317`)
- Change Image.interpolation to Enum ({pr}`319`)
- Reformatting whole repo with Black ({pr}`322`)
- Nd pyramids ({pr}`323`)
- Expand button ({pr}`324`)
- Revert "Reformatting whole repo with Black" ({pr}`327`)
- Black Format CI task ({pr}`329`)
- Refactor layer qt properties and controls ({pr}`330`)
- black format pyramid examples ({pr}`333`)
- fix labels colormap ({pr}`340`)
- fix black ignore ({pr}`341`)
- Nd vectors ({pr}`343`)
- remove broadcast from shapes ({pr}`345`)
- fix layer select styling ({pr}`347`)
- Change layers.Markers to layers.Points ({pr}`348`)
- add points thumbnail ({pr}`352`)
- fix resource compiling instructions ({pr}`353`)
- Improve resource building contrib ({pr}`354`)
- Add menubar to napari main window ({pr}`356`)
- fix selected default ({pr}`361`)
- Add dims test and fix 5D images ({pr}`362`)
- Shape thumbnails ({pr}`364`)
- [FIX] setting remote upstream in contributing guidelines  ({pr}`366`)
- Refactor thumbnail type conversion ({pr}`370`)
- Selectable points ({pr}`371`)
- Test layers list model and view ({pr}`373`)
- vectors thumbnails ({pr}`377`)
- add drag and drop ({pr}`378`)
- standardize keybindings framework ({pr}`389`)
- Refactor directory structure ({pr}`390`)
- Test image and pyramid layers ({pr}`391`)
- Rename app_context gui_qt ({pr}`392`)
- Test labels layer ({pr}`393`)
- Test points layer ({pr}`394`)
- Test vectors ({pr}`396`)
- modified multiple images overlaid figure ({pr}`399`)
- Test shapes ({pr}`400`)
- add viewer model tests ({pr}`401`)
- update readme for alpha release ({pr}`402`)

## 12 authors added to this release (alphabetical)

- [Ahmet Can Solak](https://github.com/napari/napari/commits?author=AhmetCanSolak) - @AhmetCanSolak
- [Bryant Chhun](https://github.com/napari/napari/commits?author=bryantChhun) - @bryantChhun
- [Eric Perlman](https://github.com/napari/napari/commits?author=perlman) - @perlman
- [John Kirkham](https://github.com/napari/napari/commits?author=jakirkham) - @jakirkham
- [Jeremy Freeman](https://github.com/napari/napari/commits?author=freeman-lab) - @freeman-lab
- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) - @jni
- [Kevin Yamauchi](https://github.com/napari/napari/commits?author=kevinyamauchi) - @kevinyamauchi
- [Kira Evans](https://github.com/napari/napari/commits?author=kne42) - @kne42
- [Loic Royer](https://github.com/napari/napari/commits?author=royerloic) - @royerloic
- [Mars Huang](https://github.com/napari/napari/commits?author=marshuang80) - @marshuang80
- [Nicholas Sofroniew](https://github.com/napari/napari/commits?author=sofroniewn) - @sofroniewn
- [Pranathi Vemuri](https://github.com/napari/napari/commits?author=pranathivemuri) - @pranathivemuri

## 10 reviewers added to this release (alphabetical)

- [Ahmet Can Solak](https://github.com/napari/napari/commits?author=AhmetCanSolak) - @AhmetCanSolak
- [Bryant Chhun](https://github.com/napari/napari/commits?author=bryantChhun) - @bryantChhun
- [Charlotte Weaver](https://github.com/napari/napari/commits?author=csweaver) - @csweaver
- [Jeremy Freeman](https://github.com/napari/napari/commits?author=freeman-lab) - @freeman-lab
- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) - @jni
- [Kevin Yamauchi](https://github.com/napari/napari/commits?author=kevinyamauchi) - @kevinyamauchi
- [Kira Evans](https://github.com/napari/napari/commits?author=kne42) - @kne42
- [Loic Royer](https://github.com/napari/napari/commits?author=royerloic) - @royerloic
- [Nicholas Sofroniew](https://github.com/napari/napari/commits?author=sofroniewn) - @sofroniewn
- [Shannon Axelrod](https://github.com/napari/napari/commits?author=shanaxel42) - @shanaxel42
