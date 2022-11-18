This article will be more valuable if you are familiar with the Python programming language and the Napari software. It is the third in a series of articles on testing taken from the [January 2022 testing workshop video](https://drive.google.com/file/d/1DaMrRz-rLRQ6-_y0J8O3GRpVPCn0rgYs/view). The information in this article starts at minute 15:42. This article should stand on its own and is a summary of the information in the video. The other articles are:  
* Article 1: [Python’s assert keyword](./Pythons-assert-keyword.md)  
* Article 2: [Pytest testing framework](./Pytest-testing-frameworks)  
* Article 3: This article  
* Article 4: [Test coverage](./Test-coverage)   
* Article 5: Testing widgets  

This article covers:   
* [Readers](#reader)  
* [Built-in fixtures](#built-in-fixtures)  
* [Custom fixtures and round-trip tests](#custom-fixtures-and-round-trip-tests)  
* [Enclosed testing](#enclosed-testing)  
  
## Resources  
The example plugin and all the tests discussed in this article are available in [this GitHub repository](https://github.com/DragaDoncila/plugin-tests).  
  
## Introduction  
In this article, we discuss a plugin called `plugin_tests`, generated using the cookiecutter, which has a reader and a widget. The reader is the cookiecutter numpy file reader, `napari_get_reader`. It checks whether a path ends in `.npy`. If it doesn't, it returns `None`, and if it does, it returns the `reader_function`, which loads the data. 

![napari_get_reader](../../images/Napari_Plugins_1st_napari_get_reader.PNG)
  
## Reader
The `napari_get_reader` function is the first thing to test. In the top-level directory under `src`, we have the `plugin_tests` module. Inside `plugin_tests` is the `_tests` directory. This is a typical structure when writing tests. There is also a `test_reader.py` file, which is empty. We will populate it with tests.  

![reader_function](../../images/Napari_Plugins_2nd_reader_function.PNG)
  
Test as much as possible and focus on writing small tests that look at one indivisible unit. We are focused on testing the `napari_get_reader` function. Sometimes it returns `None`; sometimes it returns the `reader_function`. We want to ensure that if we pass in a path that ends with `.npy`, it gives us back a function we can call.  
  
We import `numpy` and `napari_get_reader`. `numpy` will be used later.  
  
Best practice: Give tests meaningful names that describe what they're doing. This is left as an exercise for the student.   
  
## Built-in fixtures  
The `tmp_path` parameter is passed in as the path. `tmp_path` is a `pytest` fixture; it is not imported, it comes with `pytest`. `pytest` will inject it when the tests run. `tmp_path` provides a temporary path used to save things. Temporary paths, files, and directories created in this way during the testing process are automatically removed by `pytest` when the tests are completed. 
  
We create a file to read. First, we’ll use a path or build a file path, then generate a small amount of data. We are not testing that the reader reads 20 gigabyte numpy arrays, we’re testing to see if it returns a callable at all.  
  
There are no specific requirements for the contents of the array in this case. We just need some sort of file to save to this temporary directory. The test file will not appear anywhere unless there is a pause during test execution.   
  
temp_dir is another fixture. It provides a full working directory. .mkdir and other commands can be used inside temp_dir.

Using `napari_get_reader` with this path, we assert that the reader is callable. A function should be returned. If it isn’t, we could put an error message here.  

```python
    # tmp_path is a pytest fixture  
    def test_get_reader_returns_callable(tmp_path):  
        """Calling get_reader on numpy file returns callable"""  
   
        # write some fake data  
        my_test_file = str(tmp_path / "myfile.npy")  
        original_data = np.random.rand(20, 20)  
        np.save(my_test_file, original_data)  
 
        # try to read it back in  
        reader = napari_get_reader(my_test_file)  
        assert callable(reader)
```
 
Running the command  `pytest .` in the root directory of the plugin, we discover all the tests it recognizes as tests. It should recognize `test_reader.py` because it's a test file, prefixed with the word test. `test_reader.py` was found and passed the test. 

![pytest passed](../../images/Napari_Plugins_3rd_pytest_passed.PNG)
  
If the file did not end in `.npy` the test would fail because what was returned wasn't callable. This code has been modified to produce an error:  
    
    # tmp_path is a pytest fixture  
    def test_get_reader_returns_callable(tmp_path):  
        """Calling get_reader on numpy file returns callable"""  
 
        # write some fake data
        my_test_file = str(tmp_path / "myfile.np") # note ends in .np  
        original_data = np.random.rand(20, 20)  
        np.save(my_test_file, original_data)  
 
        # try to read it back in  
        reader = napari_get_reader(my_test_file)  
        assert callable(reader)  

Once we run `pytest` we can see that it traced back that the callable of reader is false and it has filled in the fact that reader at the time of the assertion was `None`. This is useful in debugging. 

![test_get_reader_returns_callable Failed](../../images/Napari_Plugins_4th_test_get_reader_returns_callable-failed.PNG)

## Custom fixtures and round-trip tests
Next, we test to see if this function reads the data. This is a round-trip test. We will create a fixture to write the data to make things easier for ourselves. This fixture will be called `test_reader_round_trip`. (Line 25)  
  
Whatever is returned out of a `@pytest.fixture` decorated function is passed as an argument with the name of the fixture, to the test. We are going to call this `pytest.fixture` decorated function `write_im_to_file`, as defined on line 6. We’re going to give this fixture the `tmp_path` fixture. Fixtures can use fixtures. 

`write_im_to_file` returns a function we will call `write_func` that we can pass a path to and have it write the numpy file to that path. `write_func` is defined inside `write_im_to_file` because it’s not needed anywhere else. When we use `write_im_to_file` inside this test it will be referred to as `write_func`. We can call it with a file name, save the data, and read the data back.   
  
We will have access to what `write_func` returns once it’s been called inside the test. It returns both the path where the data has been written and the original data. It accepts an actual file name that we are going to pass.   
  
The benefit of creating this fixture is that whenever we want to write our own test data we don't have to copy three lines of code, we can write just one long line of code. This is useful in testing data with different structures like integers or a specific layer type. Those arguments could be passed to further customize your fixture.  
  
We still want to make sure we get a reader when we call `napari_get_reader` with the file. We call that reader function with the file we created to see if it returns what we expect. Remember the [reader spec](https://napari.org/stable/plugins/contributions.html#contributions-readers), it should actually return a layer data list. Here is the full test, with the fixture:  
    
    @pytest.fixture  
    def write_im_to_file(tmp_path):  
 
        def write_func(filename):  
            my_test_file = str(tmp_path / filename)  
            original_data = np.random.rand(20, 20)  
            np.save(my_test_file, original_data)  
       
            return my_test_file, original_data  
 
        return write_func  
   
    def test_reader_round_trip(write_im_to_file):  
        my_test_file, original_data = write_im_to_file("myfile.npy")  
     
        reader = napari_get_reader(my_test_file)  
        assert callable(reader)  
     
        layer_data_list = reader(my_test_file)  
        assert isinstance(layer_data_list, List) and len(layer_data_list) > 0  
     
        layer_data_tuple = layer_data_list[0]  
        layer_data = layer_data_tuple[0]  
        np.testing.assert_allclose(layer_data, original_data)  
 
We’re going to assert a list length greater than zero. There must be a layer in there; otherwise, we didn't read it correctly. We also assert that it is a list. Once we start testing, there are many things we could test. Try to focus on what's most useful.  
  
We will test that inside that list is what we expected. Remember, it's a list of layer data tuples. The first item of a tuple of the layer data tuple is the actual data. We’re going to test that explicitly.  
  
Then we assert, using `numpy`’s asserting mechanism, `np.testing.assert_allclose` that they are all close, even though they should be exactly the same. This is standard practice when working with floating point precision. Numpy also has [other assertion options](https://numpy.org/doc/stable/reference/routines.testing.html) you may find useful. The layer data we read back with the reader function should be the same as the original data. If that's true, then we made the entire round trip. We save the file; we use the reader to read the file.  

 def test_reader_round_trip(write_im_to_file):  
        my_test_file, original_data = write_im_to_file("myfile.npy")  
     
        reader = napari_get_reader(my_test_file)  
        assert callable(reader)  
     
        layer_data_list = reader(my_test_file)  
        assert isinstance(layer_data_list, List) and len(layer_data_list) > 0  
     
        layer_data_tuple = layer_data_list[0]  
        layer_data = layer_data_tuple[0]  
        np.testing.assert_allclose(layer_data, original_data)  
    
We run our tests again, and now two are collected, both passing.  

![pytest - tests passed](../../images/Napari_Plugins_5th_Tests_Passed.PNG)

  
## Enclosed testing  
We did not need a viewer or napari to test this. It's important that we didn't need those because napari and the napari viewer are out of our control. What we can control is the code the _we_ wrote. We wrote that data by simply mocking up some data and getting a temporary path to it. We could thoroughly test our functions in an enclosed way without relying on other people's code or mocking up many complicated objects.  
  
The next article in this series on testing is [Test coverage](./Test-coverage).  
