# from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import re

import time
from ..Pages.element import BasePageElement
from ..locators.locators import MainPageLocators

'''
Reformat postal code from AA511AA to AA51 1AA
'''
def extractPostalCode(postalCode):
    temp = []
    for i in range(len(postalCode)):
            if (postalCode[i] == ' ' or postalCode == None):
                continue
            else:
                temp.append(postalCode[i])
    return  ''.join([i for i in temp])

    '''
    Help script to find out attribute of given object    
    '''
def get_web_element_attribute_names(web_element):
    """Get all attribute names of a web element"""
    # get element html
    html = web_element.get_attribute("outerHTML")
    # find all with regex
    pattern = """([a-z]+-?[a-z]+_?)='?"?"""
    return re.findall(pattern, html)

    '''
    Validate Post Code
    '''
def validate_postalCode(postcode):
    m = re.search('[A-Z]+[A-Z]+[0-9]+[0-9]+[0-9]+[A-Z]+[A-Z]', postcode)

    if m:
        print("Postal code is valid.")
        return True
    else:
        print("Postal code does not match given format e.g. AA511AA")
        return False


class SearchTextElement(BasePageElement):
    locator = "divLogin"

class BasePage(object):
    def __init__(self, driver, delay):
        self.driver = driver
        self.delay = delay
        # self.footer = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located(By.TAG_NAME, "footer"))

class MainPage(BasePage):

    search_text_element = SearchTextElement()

    '''
    Return the page title - Just Eat
    '''
    def get_Title(self):
        return self.driver.title

    '''
    Find Content Title and Subtitle
    Return Text: 
        Tuck into a takeaway today
        Find restaurants delivering right now, near you
    '''

    def find_contentTitles(self):
        retTitle = self.driver.find_element(By.CLASS_NAME, "title").text
        retSubTitle = self.driver.find_element(By.CLASS_NAME, "subtitle").text

        return retTitle, retSubTitle

    '''
        Find Search Query field, label and Search button
        Return Text: 
            name: postcode
            aria-lable: Enter your postcode
            Seach button type : submit
            Find restaurants delivering right now, near you
    '''
    def find_Search(self):
        retform = self.driver.find_element_by_tag_name('form')
        retLabel = retform.find_element(By.TAG_NAME,'label')
        retSearch = retLabel.find_element(By.TAG_NAME, 'input')

        retBtn = retform.find_element(By.TAG_NAME,'button').get_attribute('type')

        retName = retSearch.get_attribute('name')
        retType = retSearch.get_attribute('aria-label')

        return retName, retType, retBtn

    '''
        Validate Postal code in Search Query field 
            Return: 
                if Postal code valid: display list of available resturants in given Postal code
                Else display Error message
                
    '''

    def enter_postalCode(self, postcode):
        retform = self.driver.find_element_by_tag_name('form')
        retLabel = retform.find_element(By.TAG_NAME, 'label')
        self.retSearch = retLabel.find_element(By.TAG_NAME, 'input')

        self.retSearch.clear()
        self.retSearch.send_keys(postcode)
        time.sleep(10)
        # click Submit button
        self.retBtn = retform.find_element(By.TAG_NAME, 'button')
        self.retBtn.click()
        time.sleep(10)

        try:
            WebDriverWait(self.driver, 100).until(
                lambda driver: self.driver.find_element(By.TAG_NAME, "footer"))
            print("Filtered Page is ready")
            # c-locationHeader-container
        except TimeoutException:
            print("Loading took too much time")

    '''
    Filtered list of Resturant based on postal code
    Captured Postal Code
    and counts message including Total number of Resturant found basded on given postal code
    '''
    def count_Filteredresturants(self):
        postCode = self.driver.find_element(By.CLASS_NAME, 'c-locationHeader-container').text
        retPostCode = postCode.split(",")

        countMsg = self.driver.find_element(By.CLASS_NAME, 'c-searchHeader').text
        print("counterMsg", countMsg)
        return extractPostalCode(retPostCode[0]), countMsg

    def postalCode_ErrorMsg(self):
            errMsg = self.driver.find_element(By.ID, 'errorMessage').text
            return errMsg

    def quit(self):
        self.driver.close()

    class SearchResultsPage(BasePage):
        """Search results page action methods come here"""

        def is_results_found(self):
            # Probably should search for this text in the specific page
            # element, but as for now it works fine
            return "No results found." not in self.driver.page_source
