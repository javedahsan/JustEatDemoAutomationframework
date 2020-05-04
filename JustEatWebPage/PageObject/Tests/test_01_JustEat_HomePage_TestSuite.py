import unittest
import HtmlTestRunner
# import JustEatWebPage.PageObject.ScreenShots as fol
from selenium import webdriver
from JustEatWebPage.PageObject.Pages.loginPage import MainPage as Login
from JustEatWebPage.PageObject.Utility.logs import Log

from JustEatWebPage.PageObject.Utility.ScreenShots import SS
import env
file_path = env.Reports_dir
driver_path = env.Driver_dir

class TestHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path= driver_path + 'geckodriver.exe')
        self.driver.get("http://www.just-eat.co.uk/")
        self.delay = 5

    def test_01_home_page(self):
        # Instantiate classes
        login, log, ss = instantiate_class(self.driver, self.delay)

        # expected title
        expected_title = "Just Eat"
        try:
            page_title = login.get_Title()
            print("title", page_title)
            self.assertIn(expected_title, page_title)
            ss.Screenshot('HomePage.png')
            log.loging("Home Page {} is loaded successfully: ".format(page_title), "info")
        except Exception as e:
            log.loging("{} - WebPage Failed to load".format(e), "error")
            ss.Screenshot('HomePageNotFound.png')
            exit()

        # Validate home page content, Title and Subtitle displayed
        contentTitle, contentSubTitle = login.find_contentTitles()
        # print('logo:',contentTitle, ' ', contentSubTitle)
        log.loging("ContentTitle {} and ContentSubTitle {} are displayed successfully: ".format(contentTitle, contentSubTitle), "info")
        ss.Screenshot('contentTitle.png')
        self.assertIn("Tuck into a takeaway today", contentTitle)
        self.assertIn("Find restaurants delivering right now, near you", contentSubTitle)

        # validate Search Query field
        searchName, searchText, searchBtnTyp = login.find_Search()
        log.loging(
            "Enter your postal code {} and Search Button are displayed successfully: ".format(searchText, searchBtnTyp),
            "info")
        ss.Screenshot('SearchQueryInput.png')

        # verification
        self.assertEqual(searchName, 'postcode')
        self.assertEqual(searchText, 'Enter your postcode')
        self.assertEqual(searchBtnTyp, 'submit')

    def test_02_search_valid_postalCode(self):
        # Instantiate classes
        login, log, ss = instantiate_class(self.driver, self.delay)

        page_title = login.get_Title()
        print("title", page_title)
        self.assertIn("Just Eat", page_title)

        postcode = 'AR511AA'
        login.enter_postalCode(postcode)

        # count filtered resturants by postal code
        retPostalCode, countMsg = login.count_Filteredresturants()
        print("ReturnPostal code: ", retPostalCode, countMsg )
        log.loging(
            "Total number {} of filtered resturants are displayed for given postal code {} are displayed successfully: ".format(countMsg, retPostalCode),
            "info")
        ss.Screenshot('TotalFilteredResturantsList.png')
        total = countMsg.split(' ')

        # verification
        self.assertIn("AR51", retPostalCode)
        self.assertGreater(int(total[0]), 0)

    def test_03_search_Invalid_postalCode(self):
        # Instantiate classes
        login, log, ss = instantiate_class(self.driver, self.delay)

        page_title = login.get_Title()
        print("title", page_title)
        self.assertIn("Just Eat", page_title)

        postcode = 'AR51AA'
        login.enter_postalCode(postcode)

        # count filtered resturants by postal code
        retPostalCode, countMsg = login.count_Filteredresturants()
        print("ReturnPostal code: ", retPostalCode)
        log.loging(
            "Error message {} is displayed for given invalid postal code {}".format(
                countMsg, retPostalCode),
            "info")
        ss.Screenshot('ErrMsgInvalidPostalcode.png')

        # verification
        self.assertIn("AR51", retPostalCode)
        self.assertIn('No open restaurants', countMsg)


    def test_04_search_postalCode_withNullValue(self):
        # Instantiate classes
        login, log, ss = instantiate_class(self.driver, self.delay)

        page_title = login.get_Title()
        print("title", page_title)
        self.assertIn("Just Eat", page_title)

        postcode = ''
        login.enter_postalCode(postcode)

        errMsg = login.postalCode_ErrorMsg()

        log.loging(
            "Error message {} is displayed for given null postal code".format(errMsg), "info")
        ss.Screenshot('ErrMsgInvalidPostalcode.png')

        # verification
        self.assertIn("Please enter a postcode", errMsg)

    def tearDown(self):
         self.driver.close()

def instantiate_class(driver, delay):
    # Instantiate login class
    login = Login(driver, delay)

    # Instantiate logging class
    log = Log()
    # Instantiate screen shot driver
    ss = SS(driver)
    return login, log, ss

# ---START OF SCRIPT
if __name__ == "__main__":

    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=(driver_path)))