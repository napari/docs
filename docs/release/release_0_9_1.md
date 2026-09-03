# napari 0.9.1

*Fri, Sep 04, 2026*

We're happy to announce the bugfix release of napari 0.9.1!
napari is a fast, interactive, multi-dimensional image viewer for Python.
It's designed for browsing, annotating, and analyzing large multi-dimensional
images. It's built on top of Qt (for the GUI), vispy (for performant GPU-based
rendering), and the scientific Python stack (numpy, scipy).

This is special, not plansed release that fixes a bug with resizing of dock widgets in the viewer.

For more information, examples, and documentation, please visit our website,
https://napari.org.
napari follows [EffVer (Intended Effort Versioning)](https://effver.org/); this is a **Meso** release containing awesome new features, but some effort may be needed when updating previous projects to use this version.

## Improvements

- Allow single widget in layer controls ([#9448](https://github.com/napari/napari/pull/9448))

## Bug Fixes

- [bug fix] Keep playback in sync when dimension ranges change ([#9440](https://github.com/napari/napari/pull/9440))
- Fix out-of-sync extent in async mode ([#9459](https://github.com/napari/napari/pull/9459))
- Revert widget size policy change ([#9484](https://github.com/napari/napari/pull/9484))

## Documentation

- Prefetch data that are problematic and causing docs build failure ([docs#1103](https://github.com/napari/docs/pull/1103))
- Fix incorrect image link formatting in 0.9 release notes ([docs#1123](https://github.com/napari/docs/pull/1123))
- Add 0.9.1 release notes ([docs#1128](https://github.com/napari/docs/pull/1128))
- Update version switch to set 0.9.1 to default release  ([docs#1129](https://github.com/napari/docs/pull/1129))
- Update README image using the imshow.py example ([#9467](https://github.com/napari/napari/pull/9467))

## Other Pull Requests

- [pre-commit.ci] pre-commit autoupdate ([#9445](https://github.com/napari/napari/pull/9445))


## 5 authors added to this release (alphabetical)

(+) denotes first-time contributors 🥳

- [Grzegorz Bokota](https://github.com/napari/docs/commits?author=Czaki) - @Czaki
- [Juan Nunez-Iglesias](https://github.com/napari/docs/commits?author=jni) - @jni
- [Lorenzo Gaifas](https://github.com/napari/napari/commits?author=brisvag) - @brisvag
- [Matthias Schabel](https://github.com/napari/napari/commits?author=matthiasschabel) - @matthiasschabel
- [Suyash Naik](https://github.com/napari/napari/commits?author=Suyash-Naik) - @Suyash-Naik +

## 9 reviewers added to this release (alphabetical)

(+) denotes first-time contributors 🥳

- [Aniket](https://github.com/napari/docs/commits?author=Aniketsy) - @Aniketsy
- [Grzegorz Bokota](https://github.com/napari/docs/commits?author=Czaki) - @Czaki
- [Jacopo Abramo](https://github.com/napari/docs/commits?author=jacopoabramo) - @jacopoabramo
- [Juan Nunez-Iglesias](https://github.com/napari/docs/commits?author=jni) - @jni
- [Lorenzo Gaifas](https://github.com/napari/napari/commits?author=brisvag) - @brisvag
- [Matthias Schabel](https://github.com/napari/napari/commits?author=matthiasschabel) - @matthiasschabel
- [Peter Sobolewski](https://github.com/napari/docs/commits?author=psobolewskiPhD) - @psobolewskiPhD
- [Suyash Naik](https://github.com/napari/napari/commits?author=Suyash-Naik) - @Suyash-Naik +
- [Tim Monko](https://github.com/napari/docs/commits?author=TimMonko) - @TimMonko
