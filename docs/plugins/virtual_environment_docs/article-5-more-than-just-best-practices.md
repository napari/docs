# Article 5: More than just best practices  

This article explains the different types of tools that can help you develop and test your code. 

## Article Information

* Article 1: [Virtual environments](./article-1-virtual-environments)   
* Article 2: [Deploying your plugin](./article-2-deploying-your-plugin.md)   
* Article 3: [Version management](./article-3-version-management.md)    
* Article 4: [Developer tools](./article-4-developer-tools.md)   
* Article 5: [More than just best practices](./article-5-more-than-just-best-practices.md)  
* Article 6: [Survey](./article-6-Survey.md)  

Please also refer to: 
https://napari.org/stable/plugins/best_practices.html   

## Strongly recommended best practices

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
     
The next article in this series is the [Survey](./article-6-survey.md) article. 
