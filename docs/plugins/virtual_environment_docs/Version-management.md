# Tools and tips when building napari plugins: Version management
These articles will be more useful if you are familiar with the Python programming language and the Napari software. They are taken from the [January 2022 Testing workshop](https://drive.google.com/file/d/1DaMrRz-rLRQ6-_y0J8O3GRpVPCn0rgYs/view) video starting at about timestamp 1:01:00. The articles should stand on their own and are summaries of the information in the video. 

Article 1: [Virtual environments](./Virtual-environments.md)  
Article 2: [Deploying your plugin](./Deploying-your-plugin.md)  
Article 3: This article  
Article 4: [Developer tools](./Developer-tools.md)  
Article 5: [More than just best practices](./More-than-just-best-practices.md)  
Article 6: [Survey](./Survey.md)  

This article covers the methods of updating your version string everywhere.
* [Using git tags](#using-git-tags)
* [Using a local script to edit files](#using-a-local-script-to-edit-files)  
* [Manually](#manually)

**Goal:** Make sure that you bump your version string everywhere it may appear, in unison, prior to publishing your package.  A package can be init.py, setup, cfg, etc.

In increasing order of work, but decreasing order of magic, the methods of bummping your version string are listed below. 

### Using git tags:  
setuptools_scm: [https://github.com/pypa/setuptools_scm](https://github.com/pypa/setuptools_scm)

   `# configure in pyproject.toml, then…`  
   `$ git tag -a v0.1.0 -m v0.1.0`  

  The next time you run <font color="red">python -m build</font>, either locally or in GitHub actions, your package version will be based on the latest git tag.

### Using a local script to edit files:  
bump2version: [https://github.com/c4urself/bump2version](https://github.com/c4urself/bump2version)
```console
   $ pip install bump2version  
   # then configure all the places you use your version   
   $ bump2version -$current-version 0.5.1 minor  
```   

### Manually
This is ***not*** recommended, you *will* eventually make mistakes and have mismatched version/metadata somewhere.  
  
  ### *The "best" versioning and deployment workflow is the one you will actually use!*  
  
       
Get comfortable with at least one workflow for versioning and deploying your package  
 . . . . . . . . . . . . . . . . *otherwise, you won't do it.*

The next article in this series is [Developer tools](./Developer-tools.md).
