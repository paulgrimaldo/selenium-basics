import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyunitreport import HTMLTestRunner


class SortTables(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(
            'http://the-internet.herokuapp.com/tables'
        )

    def test_sort_tables(self):
        table_data = [[]for i in range(5)]
        print(table_data)

        for i in range(5):
            header = self.driver.find_element_by_xpath(
                f'//*[@id="table1"]/thead/tr/th[{i+1}]/span'
            )
            table_data[i].append(header.text)

            for j in range(4):
                row_data = self.driver.find_element_by_xpath(
                    f'//*[@id="table1"]/tbody/tr[{j+1}]/td[{i +1}]'
                )
                table_data[i].append(row_data.text)

        print(table_data)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        verbosity=2,
        testRunner=HTMLTestRunner(
            output='reports',
            report_name='sort-tables-report'
        )
    )
