# Tools and tips when building napari plugins: Virtual environments
These articles will be more valuable if you are familiar with the Python programming language and the Napari software. They are taken from the [January 2022 Testing workshop](https://drive.google.com/file/d/1DaMrRz-rLRQ6-_y0J8O3GRpVPCn0rgYs/view) video starting at about minute 50:25. The articles should stand on their own and are summaries of the information in the video. 
  
* Article 1: This article  
* Article 2: [Deploying your plugin](./Deploying-your-plugin.md)  
* Article 3: [Version management](./Version-management.md)  
* Article 4: [Developer tools](./Developer-tools.md)
* Article 5: [More than just best practices](./More-than-just-best-practices.md)  
* Article 6: [Survey](./Survey.md)  

This article covers: 
* [Resources](#resources)  
* [Creating environments](#creating-environments)  
* [Removing environments](#removing-environments)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  
Virtual environments  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;... are super important!  

## Resources
Some resources you might find helpful: 
* ~1.5-hour lecture on getting set up with python and virtual environments:
https://nic.med.harvard.edu/python/

* Use miniconda or mini forge. Install it in the home directory.
https://docs.conda.io/en/latest/miniconda.html  
https://github.com/conda-forge/miniforge  (comes pre-configured with conda-forge) 

* Make sure you have conda-forge in your config. The default anaconda channel has some very outdated packages, e.g. old version of Qt.   
https://forum.image.sc/t/napari-issues-on-bigsur/52630/10  
```python
    $conda config --add channels conda-forge  
    $conda config --set channel_priority strict  
```

## Creating environments  
  
Create environments liberally!  

To create an environment, use the following commands at the command prompt (terminal):

```python
    $ conda create -n name-of-env python
    $ conda activate name-of-env
    $ pip/conda install <whatever> 
```

Virtual environments  
. . . are made to be ephemeral.  

## Removing environments
Consider your environment as disposable.
If you are ever having weird problems, nuke your environment and start over using the following commands:  

```python
    $ conda activate base  
    $ conda remove -n name-of-env --all -y
    $ conda create -n name-of-env python
    $ conda activate name-of-env
    $ pip/conda install <whatever>
```  
  
Encourage your users to do the same. You can waste a lot of time trying to debug something that someone unknowingly did when installing a variety of things into their environment. If they can provide a repeatable example (starting from environment creation), then it's worth debugging.

The next article in this series is [Deploying your plugin](./Deploying-your-plugin.md). 
