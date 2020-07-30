
import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from time import sleep
from ddt import ddt, data, unpack


@ddt
class SearchDDT(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('http://demo-store.seleniumacademy.com/')

    @data(('dress', 6), ('music', 5))
    @unpack
    def test_search_ddt(self, search_value, expected_count):
        search_field = self.driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        products = self.driver.find_elements_by_xpath(
            '//h2[@class="product-name"]/a'
        )
        for product in products:
            print(product.text)

        self.assertEqual(expected_count, len(products))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        verbosity=2,
        testRunner=HTMLTestRunner(
            output='reports',
            report_name='search-ddt-report'
        )
    )
