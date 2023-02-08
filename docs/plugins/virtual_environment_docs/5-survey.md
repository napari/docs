# 5: Survey

This guide contains questions that were submitted to our survey on testing.  

## Other topics in this series:

* 1: [Virtual environments](./1-virtual-environments.md)   
* 2: [Deploying your plugin](./2-deploying-your-plugin.md)  
* 3: [Version management](./3-version-management.md)  
* 4: [Developer tools](./4-developer-tools.md)
* 5: This guide  

## This guide covers:   
* [Questions](#questions)  
    - [Testing plugins](#testing-plugins)  
    - [Testing widgets](#testing-widgets)  
    - [Better signal or slot documentation or functionality](#better-signal-or-slot-documentation-or-functionality)  
    - [Creating or deleting a point or shape layer](#creating-or-deleting-a-point-or-shape-layer)  
    - [Github tests failing](#github-tests-failing)  
    - [Cancelling a method](#cancelling-a-method)  
    - [Testing environments](#testing-environments)  
* [Topics](#topics)  
    - [npe2](#npe2)  
    - [Widget development](#widget-development)
  
## Questions

### Testing plugins    
Question: What are the best practices to test a plugin with multiple sequential steps?  
e.g. Is it ok to rely on the "results" of a test to run the next test or should they all be fully independent?  

Answer:  
* Ideally, aim for unit testing.  
* Tests should not pass/fail together.  
* Use fixtures to provide a test with inputs, even if you have to make them up.  
  https://docs.pytest.org/en/6.2.x/fixture.html 
* Use mocks (mock-ups) to assert that specific calls are made, without necessarily caring about what happens after that call is made.  
  https://docs.python.org/3/library/unittest.mock.html 

*This is definitely an art form. It takes time. Be patient.*

### Testing widgets
Question: How do you test widgets, the napari viewer, and graphical user interfaces? How do you test Qt in general?

Answer:
* Try not to!
* You should generally trust that a button click (for example) will call your callback and focus on testing that your callback does what it's supposed to do given that it gets called following some UI interaction.
* However: If you have a scenario where you are actually creating a complicated widget directly in Qt, see `pytest-qt` for lots of tips, specifically `qtbot`.
    - pytest-qt - [https://pytest-qt.readthedocs.io/en/latest/intro.html](https://pytest-qt.readthedocs.io/en/latest/intro.html)
    - qtbot - [https://pytest-qt.readthedocs.io/en/latest/reference.html?highlight=qtbot#module-pytestqt.qtbot](https://pytest-qt.readthedocs.io/en/latest/reference.html?highlight=qtbot#module-pytestqt.qtbot)
* Oftentimes, this comes down to knowing and/or learning the Qt API really well.  

### Better signal or slot documentation or functionality
Question: How to create better signal/slot documentation/functionality as the user interacts with the core napari interface? For example, creating/editing/deleting a point or shape layer?

Answer: 
[https://napari.org/guides/stable/events_reference.html](https://napari.org/stable/guides/events_reference.html)  
Granted, this is a work in progress. 

### Creating or deleting a point or shape layer:  
    Viewer.layers.events.inserted  
    Viewer.layers.events.removed  
    Viewer.layers.events.moved  
    Viewer.layers.events.changed  
    Viewer.layers.events.reordered  

Editing a point or shape layer  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;. . .complicated, because it may be a pure numpy object . . .  

### Github tests failing  
Question: How do you avoid github tests failing?  
  
Answer:  
* First make sure all your tests are passing locally.  
* After that, it's complicated. More background or context is needed to answer this question.  
  
### Cancelling a method  
Question: How do you make a process cancellable to interrupt a method that is running in a for loop, for example?  

Answer:  
* In single-threaded python, use `Ctrl-C`  
* In multithreaded python, there are many different patterns. Consider using a generator-based thread worker:  
  https://napari.org/stable/guides/threading.html#generators-for-the-win  

### Testing environments  
Question: Are there testing environments in napari?  
Answer: Napari does not create or otherwise manage environments.  
  
## Topics  
  
### npe2  
Question: Introduction to npe2? Migrating to new plug-in architecture?   
  
Answer:  
* The primary difference is in how plugins are discovered:  
    - npe1 used decorators, requiring module import.  
    - npe2 uses static manifests (`napari.yaml`), describing contributions without requiring import.  
    - Your first plugin: https://napari.org/stable/plugins/first_plugin.html  
  
* Contributions Reference: https://napari.org/stable/plugins/contributions.html  
* Guides for each type of contribution: https://napari.org/stable/plugins/guides.html  
* Migration guide: https://napari.org/stable/plugins/npe2_migration_guide.html  
  
### Widget development  
Question: What is the optimal setup to quickly iterate in widget development?    
  
Answer:   
* Create a script that will start napari and load your widget without any UI interaction.  
* Don't test as a plugin. Start by directly calling `viewer.window.add_dock_widget` with a manually created widget.  
* Familiarize yourself with auto-reload features.  
  https://ipython.readthedocs.io/en/stable/config/extensions/autoreload.html   
* Consider using watchmedo from watchdog:  
  https://github.com/gorakhargosh/watchdog  
  This will monitor a file/directory for changes, and re-run a command each time (which is why step #1 is also useful).  


This is the last topic in this series. 
