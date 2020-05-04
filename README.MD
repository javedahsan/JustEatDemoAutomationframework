#Just Eat Demo
****

This Project demonstrates to develop Page object methodolgy base Automation Test Framework using Python and, Selenium.

All test are setup to test the web application JustEat using url http://www.just-eat.co.uk/
 
### How To Start

To run the tests the following steps should be followed:

+   Make sure at least [Python 3.8.2](https://www.python.org/downloads/release/python) [see Python 3.8.X release] is installed.

    '''
        $python -v
        e.g. : Python 3.8.2
    '''
+   Also make sure Python's [Pip](http://pypi.python.org/pypi/pip) is installed.

    '''
        pip -v
        e.g. pip 20.0.2 from /usr/lib/python2.7/lib/site-packages/pip 
    '''    
 +  Install required packages that are needed to run the Robot tests.
    go to project home directory e.g. ~/projectJustEatRobo and run the following command:
    '''
        pip install -r requirements.txt
    '''
 + If all required packages are installed successfully using following command:
    '''
        $ pip  freeze
        List of all installed packages will be displayed
    '''    
 + Before we can run the Selenium test suites, we need to install Firefox (or you can install other drivers Chrome, Safari etc.)
 ### Run the tests
Running the tests is very easy:
```
    $ python  <project working directory>script location>\test_01_JustEat_HomePage_TestSuite.pyrobot.run testsuites
e.g. D:\projectJustEat\JustEatWebPage\PageObject\Tests

```    
+ List of all folders:
`Tests`      - location for All testcases
`driver`     - location for all webdrivers
`PageObject` - location for locators, object implementation classes and log files, see subfolders
`Reports`    - location for Test Status report in html format, easily view in any browser
`ScreenShots`- location for all Screen shots

  