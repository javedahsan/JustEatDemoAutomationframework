import HtmlTestRunner
import unittest
import os

from unittest import TestLoader, TestSuite, TextTestRunner
from JustEatWebPage.PageObject.Tests.test_01_JustEat_HomePage_TestSuite import TestHomePage


''' Project directory path'''
import env
file_path = env.Reports_dir

if __name__ == "__main__":

    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(TestHomePage),
    ))

    # direct = os.getcwd()
    outfile = open(file_path + 'DemoTest.html', 'w')

    runner1 = HtmlTestRunner.HTMLTestRunner(
        stream=outfile
        # title='Test Report',
        # description='Demo Tests'
    )
    #
    runner1.run(suite)
    # runner = TextTestRunner(verbosity=2)
    # runner.run(suite)






