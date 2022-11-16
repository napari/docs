# Tools and tips when building napari plugins: Developer tools
This article will be more valuable if you are familiar with the Python programming language and the Napari software. It is taken from the [January 2022 Testing workshop](https://drive.google.com/file/d/1DaMrRz-rLRQ6-_y0J8O3GRpVPCn0rgYs/view) video starting at about minute 49:08. The articles should stand on their own and are summaries of the information in the video. 
  
* Article 1: [Virtual environments](./Virtual-environments)   
* Article 2: [Deploying your plugin](./Deploying-your-plugin)  
* Article 3: [Version management](./Version-management)  
* Article 4: This article
* Article 5: [More than just best practices](./More-than-just-best-practices)  
* Article 6: [Survey](./Survey)  

This article covers the following topics:   
* [General tools](#general-tools)
    - [Linting tools](#linting-tools)  
    - [Formatting tools](#formatting-tools)  
    - [Pre-commit tools](#pre-commit-tools)  
* [Napari-plugin-specific-developer-tools](#napari-plugin-specific-developer-tools)
  
## General tools  
All of these are *optional*.  
Many are very helpful, but they do take a little time to learn. The more time you spend coding, the greater the return-on-investment for using them. It's a personal decision on whether the time saved by using these outweighs the time required to understand the tools.

### Linting tools   
These _check_ your code.  
* flake8 (https://flake8.pycqa.org/) - checks various code style conventions, unused variables, line spacings, etc…  
* mypy (https://github.com/python/mypy)  
    - Static type checker: enforces proper usage of types.  
    - Super useful once you get the hang of it, but definitely an intermediate-advanced tool.  
    - Along with high test coverage, probably the best time-saver and project robustness tool.    

### Formatting tools 
These _auto-modify_ your code.  
* black (https://github.com/psf/black)  
  Forces code to follow specific style, indentations, etc...  
* autoflake (https://github.com/myint/autoflake)  
  Auto-fixes some flake8 failures.  
* isort (https://github.com/PyCQA/isort)  
  Auto-sorts and formats your imports.
* setup-cfg-fmt (https://github.com/asottile/setup-cfg-fmt)  
  Sorts and enforces conventions in setup.cfg.  

### Pre-commit tools
* pre-commit (https://pre-commit.com/), runs all your checks each time you run git commit, preventing bad code from ever getting checked in.  
```console     $ pip install pre-commit
     # install the pre-commit "hook"  
     $ pre-commit install  
     # then configure in .pre-commit-config.yaml  
     # (optionally) Run hooks on demand  
     $ pre-commit run -$all-files  
```  

* pre-commit-ci (https://pre-commit.ci/)
    - Runs all your pre-commit hooks on CI (Continuous Integration).
    - Useful even if contributors don't install and run your pre-commit hooks locally before they open a PR.  
  
## Napari-plugin-specific developer tools  

* https://github.com/tlambert03/napari-plugin-checks 
    - This is a *pre-commit hook*. It is intended to be added to your 
    `.pre-commit-config.yaml` file
    - It *statically* (without importing) checks various best practices about your plugin:  
`     repo: https://github.com/tlambert03/napari-plugin-action `      
`     rev: v0.2.0  `     
`     hooks: `     
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`id: napari-plugin-checks`     

* https://github.com/tlambert03/napari-plugin-action  (work in progress)
    - This is a _github-action_. 
    - It is intended to be added to your GitHub workflow.
    - It (currently) checks that your plugin is installable, and performs a few sanity checks about Qt backends and dock widgets.  
`     uses: tlambert03/napari-plugin-action@main  `  
`     with:     `     
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`package_name:  <your-package-name>`     

The next article in this series is [More than just best practices](./More-than-just-best-practices).  
