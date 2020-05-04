import os
from selenium import webdriver
'''
Class to record web page screen shot
'''
import env
ss_path = env.ScreenShot_dir

class SS(object):

    def __init__(self, driver):
        self.driver = driver

    def Screenshot(self,path):

        print('filePATH:', ss_path + path)
        self.driver.get_screenshot_as_file(ss_path + path)