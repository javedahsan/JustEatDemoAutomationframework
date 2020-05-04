import logging
from selenium import webdriver
import time


logger = logging.getLogger(__name__)
request_header = {
    "Content-Type": "text/json"
}

''' Project directory path'''
import env
file_path = env.Driver_dir

def firefox_driver():
    """
       This tests verifies the OpsHubMonitor UI is launched from the system using firefox browser.
    """
    import logging
    from selenium import webdriver
    import time

    logger = logging.getLogger(__name__)
    request_header = {
        "Content-Type": "text/json"
    }

    def firefox_driver():
        """
           This tests verifies the OpsHubMonitor UI is launched from the system using firefox browser.
        """
        browerdriver = webdriver.Firefox(executable_path=file_path + "geckodriver.exe")
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("http://opensource-demo.orangehrmlive.com/")

        firefox_options = webdriver.firefox.options.Options()
        browser = webdriver.Firefox(options=firefox_options)
        browser.maximize_window()
        driver.get("http://opensource-demo.orangehrmlive.com/")
        return browser

    driver = firefox_driver()

    def get_driver():
        return driver


