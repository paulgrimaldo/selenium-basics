import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from google_page import GooglePage


class Google(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        self.driver.get('https://www.google.com')
        self.driver.maximize_window()

    def test_search(self):
        google = GooglePage(self.driver)
        google.open()
        google.search('Selenium')
        self.assertEqual('Selenium', google.keyword)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        verbosity=2,
        testRunner=HTMLTestRunner(
            output='reports',
            report_name='google-report'
        )
    )
