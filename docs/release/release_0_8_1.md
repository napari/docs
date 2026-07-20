# napari 0.8.1

*Wed, Jul 29, 2026*

We're happy to announce the release of napari 0.8.1!
napari is a fast, interactive, multi-dimensional image viewer for Python.
It's designed for browsing, annotating, and analyzing large multi-dimensional
images. It's built on top of Qt (for the GUI), vispy (for performant GPU-based
rendering), and the scientific Python stack (numpy, scipy).

For more information, examples, and documentation, please visit our website,
https://napari.org.

napari follows [EffVer (Intended Effort Versioning)](https://effver.org/); this is a **Meso** release containing awesome new features, but some effort may be needed when updating previous projects to use this version.

## Bug Fixes

- Fix cross layer in multiple viewer example to use line vectors. ([#9213](https://github.com/napari/napari/pull/9213))

## Documentation

- Update homepage video for 0.8 changes ([docs#1070](https://github.com/napari/docs/pull/1070))
- Start creating 0.8.1 release notes ([docs#1073](https://github.com/napari/docs/pull/1073))

## Other Pull Requests

- Update label name in condition of label trigger build ([docs#1067](https://github.com/napari/docs/pull/1067))
- Update version switcher to point to 0.8.0 as stable ([docs#1071](https://github.com/napari/docs/pull/1071))
- Use shared version of label clean workflow ([#9116](https://github.com/napari/napari/pull/9116))
- TST: parameterizing with iterables is deprecated in pytest ([#9217](https://github.com/napari/napari/pull/9217))
- Make tensorstore optional dependency of `test_labels` again ([#9220](https://github.com/napari/napari/pull/9220))


## 3 authors added to this release (alphabetical)

(+) denotes first-time contributors 🥳

- [Filippo  Maria Castelli, PhD](https://github.com/napari/napari/commits?author=filippocastelli) - @filippocastelli +
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) ([docs](https://github.com/napari/docs/commits?author=Czaki))  - @Czaki
- [Tim Monko](https://github.com/napari/docs/commits?author=TimMonko) - @TimMonko

## 6 reviewers added to this release (alphabetical)

(+) denotes first-time contributors 🥳

- [Carol Willing](https://github.com/napari/docs/commits?author=willingc) - @willingc
- [Draga Doncila Pop](https://github.com/napari/docs/commits?author=DragaDoncila) - @DragaDoncila
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) ([docs](https://github.com/napari/docs/commits?author=Czaki))  - @Czaki
- [Juan Nunez-Iglesias](https://github.com/napari/docs/commits?author=jni) - @jni
- [Lorenzo Gaifas](https://github.com/napari/docs/commits?author=brisvag) - @brisvag
- [Tim Monko](https://github.com/napari/docs/commits?author=TimMonko) - @TimMonko
