import unittest
import csv
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from time import sleep
from ddt import ddt, data, unpack


def get_data(file_name):
    rows = []
    data_file = open(file_name, 'r')
    reader = csv.reader(data_file)
    next(reader, None)

    for row in reader:
        rows.append(row)

    return rows


@ddt
class SearchCsvDDT(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('http://demo-store.seleniumacademy.com/')

    @data(*get_data('testdata.csv'))
    @unpack
    def test_search_csv_ddt(self, search_value, expected_count):
        search_field = self.driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        products = self.driver.find_elements_by_xpath(
            '//h2[@class="product-name"]/a'
        )

        expected_count = int(expected_count)
        if expected_count > 0:
            self.assertEqual(expected_count, len(products))
        else:
            message = self.driver.find_element_by_class_name('note-message')
            self.assertEqual('Your search returns no result.', message)

        print(f"Found {len(products)} products")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        verbosity=2,
        testRunner=HTMLTestRunner(
            output='reports',
            report_name='search-csv-ddt-report'
        )
    )
