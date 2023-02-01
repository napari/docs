# 1: Virtual environments  

This guide explains the value of using virtual environments and how to create and remove them. 

## Other topics in this series:  

* 1: This guide  
* 2: [Deploying your plugin](./2-deploying-your-plugin.md)  
* 3: [Version management](./3-version-management.md)     
* 4: [Developer tools](./4-developer-tools.md)   
* 5: [Survey](./5-Survey.md)   

### This guide covers: 
* [Resources](#resources)  
* [Creating environments](#creating-environments)  
* [Removing environments](#removing-environments)

</br>
Virtual environments  
</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;. . . are super important!  
</br>  

## Resources
Some resources you might find helpful: 
* ~1.5-hour lecture on getting set up with python and virtual environments:
https://nic.med.harvard.edu/python/

* Use [miniconda](https://docs.conda.io/en/latest/miniconda.html) or [mini forge](https://github.com/conda-forge/miniforge) (comes pre-configured with conda-forge). Install it in the home directory.
https://docs.conda.io/en/latest/miniconda.html  
https://github.com/conda-forge/miniforge  (comes pre-configured with conda-forge) 

* Make sure you have conda-forge in your config. The default anaconda channel has some very outdated packages, e.g. [old version of Qt](https://forum.image.sc/t/napari-issues-on-bigsur/52630/10).   
https://forum.image.sc/t/napari-issues-on-bigsur/52630/10  
```console
    $conda config --add channels conda-forge  
    $conda config --set channel_priority strict  
```

## Creating environments  
  
Create environments liberally!  

To create an environment, use the following commands at the command prompt (terminal):

```console
    $ conda create -n name-of-env python
    $ conda activate name-of-env
    $ pip/conda install <whatever> 
```

Virtual environments  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  . . . are made to be ephemeral.  

## Removing environments
Consider your environment as disposable.
If you are ever having weird problems, nuke your environment and start over using the following commands:  

```console
    $ conda activate base  
    $ conda remove -n name-of-env --all -y
    $ conda create -n name-of-env python
    $ conda activate name-of-env
    $ pip/conda install <whatever>
```  
  
Encourage your users to do the same. You can waste a lot of time trying to debug something that someone unknowingly did when installing a variety of things into their environment. If they can provide a repeatable example (starting from environment creation), then it's worth debugging.

The next topic in this series is [Deploying your plugin](./2-deploying-your-plugin.md). 
