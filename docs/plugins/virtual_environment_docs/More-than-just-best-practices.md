# Tools and tips when building napari plugins: More than just best practices
These articles will be more valuable if you are familiar with the Python programming language and the Napari software. They are taken from the [January 2022 Testing workshop](https://drive.google.com/file/d/1DaMrRz-rLRQ6-_y0J8O3GRpVPCn0rgYs/view) video starting at about 1:12:00. The articles should stand on their own and are summaries of the information in the video. 
  
* Article 1: [Virtual environments](./Virtual-environments.md)   
* Article 2: [Deploying your plugin](./Deploying-your-plugin.md)  
* Article 3: [Version management](./Version-management.md)  
* Article 4: [Developer tools](./Developer-tools.md)
* Article 5: This article  
* Article 6: [Survey](./Survey.md)  


Please also refer to: 
https://napari.org/stable/plugins/best_practices.html   

* Don’t include `PySide2` or `PyQt5` in your plugin’s dependencies. Use `qtpy` and let your users pick their backend.
* Try not to depend on packages that require C compilation but do not offer wheels. Check whether they offer wheels at [pypi.org](https://pypi.org/).
* Don’t import heavy dependencies _greedily_ at the top of your module. This is less relevant with npe2.
* Don’t leave resources (such as file handles) open:  

```  
    # yes 
    with open(..&) as fh:  
    text = fh.read()  
  
    # no--$cov-report=html  
    file = open(..&)  
    text = file.read()  
``` 

* Aim for 100% test coverage!  
https://coverage.readthedocs.io/  
https://github.com/pytest-dev/pytest-cov

```console
 $ pip install pytest-cov  
 $ pytest -$cov=<your_package>
 $ open htmlcov/index.html
```
     
The next article in this series is the [Survey](./Survey.md) article. 
