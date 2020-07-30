import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyunitreport import HTMLTestRunner


class DynamicTypo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(
            'http://the-internet.herokuapp.com/typos'
        )

    def test_dynamic_typo(self):
        paragraph_to_check = self.driver.find_element_by_css_selector(
            '#content > div > p:nth-child(3)'
        )
        text_to_check = paragraph_to_check.text
        print(text_to_check)
        tries = 1
        found = False
        correct_text = "Sometimes you'll see a typo, other times you won't."
        while text_to_check != correct_text:
            paragraph_to_check = self.driver.find_element_by_css_selector(
                '#content > div > p:nth-child(3)'
            )
            text_to_check = paragraph_to_check.text
            self.driver.refresh()

        while not found:
            if text_to_check == correct_text:
                tries += 1
                self.driver.refresh()
                found = True

        self.assertEqual(found, True)
        print(f"It took {tries} tries to find the typo")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        verbosity=2,
        testRunner=HTMLTestRunner(
            output='reports',
            report_name='dynamic-typos-report'
        )
    )
