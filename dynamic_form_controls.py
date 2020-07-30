import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyunitreport import HTMLTestRunner


class DynamicFormControls(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(
            'http://the-internet.herokuapp.com/dynamic_controls'
        )

    def test_dynamic_controls(self):
        checkbox = self.driver.find_element_by_css_selector(
            '#checkbox > input[type=checkbox]'
        )
        checkbox.click()

        remove_add_button = self.driver.find_element_by_css_selector(
            '#checkbox-example > button'
        )
        remove_add_button.click()
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#checkbox-example > button')
        ))
        enable_disable_button = self.driver.find_element_by_xpath(
            '//*[@id="input-example"]/button'
        )
        enable_disable_button.click()
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="input-example"]/button')
        ))
        text_area = self.driver.find_element_by_css_selector(
            '#input-example > input[type=text]'
        )
        text_area.send_keys('Selenium')
        enable_disable_button.click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        verbosity=2,
        testRunner=HTMLTestRunner(
            output='reports',
            report_name='dynamic-form-controls-report'
        )
    )
