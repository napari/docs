# Article 3: Version management  

This article covers the methods of updating your version string everywhere.

## Article Information  

* Article 1: [Virtual environments](./article-1-virtual-environments)  
* Article 2: [Deploying your plugin](./article-2-deploying-your-plugin.md)    
* Article 3: This article   
* Article 4: [Developer tools](./article-4-developer-tools.md)   
* Article 5: [Survey](./article-6-Survey.md) 

## This article covers:  
* [Using git tags](#using-git-tags)
* [Using a local script to edit files](#using-a-local-script-to-edit-files)  
* [Manually](#manually)

**Goal:** Make sure that you bump your version string everywhere it may appear, in unison, prior to publishing your package.  A version number can be in `init.py`, `setup.cfg`, etc.

In increasing order of work, but decreasing order of magic, the methods of bummping your version string are listed below. 

## Using git tags:  
setuptools_scm: [https://github.com/pypa/setuptools_scm](https://github.com/pypa/setuptools_scm)

   `# configure in pyproject.toml, then…`  
   `$ git tag -a v0.1.0 -m v0.1.0`  

  The next time you run <font color="red">`python -m build`</font>, either locally or in GitHub actions, your package version will be based on the latest git tag.

## Using a local script to edit files:  
One tool for doing this is [bump2version](https://github.com/c4urself/bump2version). For example:
```console
   $ pip install bump2version  
   # then configure all the places you use your version   
   $ bump2version -$current-version 0.5.1 minor  
```   

## Manually
This is ***not*** recommended, you *will* eventually make mistakes and have mismatched version/metadata somewhere.  
  
  ### *The "best" versioning and deployment workflow is the one you will actually use!*  
  
       
Get comfortable with at least one workflow for versioning and deploying your package  
 . . . . . . . . . . . . . . . . *otherwise, you won't do it.*

The next article in this series is [Developer tools](./article-4-developer-tools.md).
