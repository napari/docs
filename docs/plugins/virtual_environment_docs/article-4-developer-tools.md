# Article 4: Developer tools

This article explains the different types of tools that can help you develop and test your code.  

## Article information  
* Article 1: [Virtual environments](./article-1-virtual-environments)  
* Article 2: [Deploying your plugin](./article-2-deploying-your-plugin.md)    
* Article 3: [Version management](./article-3-version-management.md)   
* Article 4: This article.   
* Article 5: [More than just best practices](./article-5-more-than-just-best-practices.md)   
* Article 6: [Survey](./article-6-Survey.md) 

## This article covers:   
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

The next article in this series is [More than just best practices](./article-5-more-than-just-best-practices.md).  
