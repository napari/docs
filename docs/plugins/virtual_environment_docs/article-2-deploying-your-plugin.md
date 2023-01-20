# Article 2: Tools and tips when building napari plugins: Deploying your plugin  

This article explains some of the techniques you can use to deploy your plugin. 

## Article information  
* Article 1: [Virtual environments](./article-1-virtual-environments.md)   
* Article 2: This article  
* Article 3: [Version management](./article-3-version-management.md)     
* Article 4: [Developer tools](./article-4-developer-tools.md)   
* Article 5: [More than just best practices](./article-5-more-than-just-best-practices.md)  
* Article 6: [Survey](./article-6-Survey.md)   

## This article covers:   
* [PyPI and Anaconda](#pypi-and-anaconda)
    - [Package formats (PyPI)](#package-formats-pypi)
    - [PyPI](#pypi)
* [Deploying plugins](#deploying-plugins)
    - [Automatically via GitHub actions](#automatically-via-github-actions)
    - [Anaconda cloud via conda-forge](#anaconda-cloud-via-conda-forge)


## PyPI and Anaconda
Try to deploy to both! But for now, try to at least use pip. You can always also provide your users with manual installation instructions (e.g. if you want to use conda or have specific dependencies).

### Package formats (PyPI)
**sdist** means source distribution. An **sdist** includes all of the files that are required to *build* your package. An **sdist** may require specific additional software (e.g. compilers) to actually build.

**wheel** is a prebuilt package, ready to drop into site-packages. It includes compiled OS-specific extensions (if applicable).

You are *strongly* encouraged to ship both! If the wheel is not present, pip will try to build it from the sdist before installation, and that may fail depending on the package.  

**Note:** This goes for dependencies too! Check all your dependencies for wheel availability.  

**Example:** See if a given package ships a wheel. https://pypi.org/project/napari/#files

### PyPI
**build** (package builder): https://pypa-build.readthedocs.io/en/latest/  
**twine** (PyPI Client): https://twine.readthedocs.io/en/latest/  
```python

    # twine is a PyPI Client  
    # build is a PEP 517 package builder  
    $ pip install twine build

    # create a wheel and an sdist  
    $ python -m build  
     
    # (Optional) upload to test PyPI  
    $ twine upload -r testpypi dist/*  

    # Upload to PyPI  
    $ twine upload dist/*  

```
**Note:** `python -m build` is the modern alternative to setuptools `python setup.py sdist bdist_wheel`. (It calls setuptools behind the scenes.)

## Deploying plugins:

### Automatically via GitHub actions
This requires either: 
* Running twine manually (e.g: your-repo/.github/workflows/deploy.yaml)  
or   
* Using a pre-made GitHub action: https://github.com/pypa/gh-action-pypi-publish   

```yaml
jobs:  
    deploy:  
      name: Deploy
      runs on: ubuntu-latest  
      if: “success() && startsWith(github.ref, ‘refs/tags/’)”  
      steps:  
    - uses: actions/checkout@v2  

    -     name: Set up Python  
           uses: actions/setup-python@v2  
     -     with:   
           python-version “3.x”  

     -     name: install  
           run:  
               pip install -U pip  
               pip install -U build twine  
               python -m build  
  
    -     name: Build and publish  
          run:  twine upload dist/*  
          env: 
             TWINE_USERNAME: __token__  
             TWINE_PASSWORD: ${{ secrets.TWINE_API_KEY }}  

```

  **Note:** Gate this action on some criterion, like a git tag: https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_Idif

### Anaconda cloud via conda-forge
https://conda-forge.org/docs/maintainer/adding_pkgs.html

1. Fork https://github.com/conda-forge/staged-recipes
2. Create a new branch
3. Create a new folder in recipes directory (copy the existing example)
4. Update the **meta.yaml** file to include your package's build and run requirements
5. Commit and open a PR to https://github.com/conda-forge/staged-recipes   

Once your recipe is approved and merged, the rest happens *automagically*, and your package will appear on the anaconda cloud.

This is **far** easier if you already have an sdist published to PyPI.

The next article in this series is [Version management](./article-3-version-management.md).
