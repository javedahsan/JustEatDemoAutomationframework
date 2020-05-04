from selenium import webdriver

Instance = None

def Initialize():
    global Instance
    Instance = webdriver.Firefox(executable_path="D:/projectSelenium/drivers/geckodriver.exe")
    Instance.implicitly_wait(5)
    return Instance

def CloseDriver():
    global Instance
    Instance.quit()