import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from time import sleep


class AutomaticNavigation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('https://www.google.com')

    def test_browser_navigation(self):
        search_field = self.driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('Vs Code')
        search_field.submit()
        
        self.driver.back()
        sleep(3)
        self.driver.forward()
        sleep(3)
        self.driver.refresh()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        verbosity=2,
        testRunner=HTMLTestRunner(
            output='reports',
            report_name='automatic-browser-report'
        )
    )
