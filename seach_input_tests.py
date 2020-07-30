import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class SearchInputTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        self.driver.get('http://demo.onestepcheckout.com/')
        self.driver.maximize_window()

    def test_search_tee(self):
        search_field = self.driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('tee')
        search_field.submit()

    def test_search_salt_shaker(self):
        search_field = self.driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('salt shaker')
        search_field.submit()

        products = self.driver.find_elements_by_xpath(
            '//*[@id="product-collection-image-389"]')
        self.assertTrue(1, len(products))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        verbosity=2,
        testRunner=HTMLTestRunner(
            output='reports',
            report_name='search-input-report'
        )
    )
