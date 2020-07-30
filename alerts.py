import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner


class CompareProducts(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('http://demo-store.seleniumacademy.com/')

    def test_compare_products_removal_alert(self):
        search_field = self.driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('tee')
        search_field.submit()

        self.driver.find_element_by_class_name('link-compare').click()
        self.driver.find_element_by_link_text('Clear All').click()

        alert = self.driver.switch_to_alert()
        self.assertEqual(
            'Are you sure you would like to remove all products from your comparison?', alert.text)
        alert.accept()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        verbosity=2,
        testRunner=HTMLTestRunner(
            output='reports',
            report_name='alerts-report'
        )
    )
