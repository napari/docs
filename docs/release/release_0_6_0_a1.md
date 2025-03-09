# napari 0.6.0a1

**Release Date**: 2025-03-14


**This is an early developer preview of napari 0.6.0.**

## Major new features of the 0.6 release, compared to 0.5.6
<!-- Or do we want to compare to 0.5 -->

napari 0.6 is still in development. This release, 0.6.0a1, is the first planned alpha release.

Alpha releases are intended to make it easier to test the current state of new features and bug fixes and to test the release process.
This release is the first alpha release of the 0.6 series. It includes a number of new features and improvements, including:

## Dump of Juan's post last month
tldr:
timeline: alpha release tomorrow, release candidate next week, final release week of Mar 3 at the earliest.
Pydantic 2.0+ will be required
Python 3.10+ will be required
npe1 plugins will be automatically converted to npe2 by default (this may break some features if they rely on import-time behaviour)
but, lots of cool new features, improvements and bug fixes! :rocket:
Read on for more details:
This release brings about some significant changes so we want to take our time in rolling it out, and would appreciate all your assistance in testing it! Here's a list of all the PRs added and coming in 0.6.0, and here is the same list filtered by the "highlight" label, as a preview of what we think is important to highlight.
The main gotchas you should be aware of as a user are:
We are dropping Python 3.9 support. This is slightly earlier than Python 3.9's EOL date (October 2025), but we are still supporting Python 3.10 which is past its recommended window from SPEC0. The bundle follows SPEC0 strictly and so uses Python 3.11. We hope that serves most if not all of our user community!
We are requiring Pydantic version 2 and higher. Supporting Pydantic 1 and 2 together was a lot of effort, but by now most plugins and libraries using Pydantic are at version 2, which does bring significant speed and functionality advantages. If you know a library or plugin you use with napari and that is still strictly on Pydantic 1.x, please let us know!
npe1 plugins will now be automatically converted to npe2 by default (with a warning), which should not change much but it will break plugins that rely on being imported at launch to modify viewer behaviour. You will be able to turn off this automatic conversion in the settings, but this will go away in July, so this is your opportunity to work with plugin authors to migrate to npe2.
The default handedness of the 3D viewer is changing from left-handed to right-handed. Most users probably won't be aware of this, but to a small percentage of users it will fix a bug that has existed since napari started supporting 3D volumes: they were mirror images of each other. For example, if you loaded a DNA atomic model, you would get a left-handed helix. You can read more about it in this snippet (which still incorrectly points to v0.5.6, that will be fixed in the actual release notes and docs). If you incorporated workarounds to make sure your objects were not mirrored, such as setting a negative scale, now is a good time to undo those workarounds! But also, there will be a mechanism to flip the axes back if you were happy with the old handedness.
We also have cool new features, the most amazing of which is the command palette (#5483)!