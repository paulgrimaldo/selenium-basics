import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class AssertionsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        self.driver.get('http://demo-store.seleniumacademy.com/')
        self.driver.maximize_window()

    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, 'q'))

    def test_language_options(self):
        self.assertTrue(self.is_element_present(By.ID, 'select-language'))

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        verbosity=2,
        testRunner=HTMLTestRunner(
            output='reports',
            report_name='assertions-report'
        )
    )
