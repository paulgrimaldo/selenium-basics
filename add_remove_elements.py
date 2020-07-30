
import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from time import sleep


class AddRemoveElement(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(
            'http://the-internet.herokuapp.com/add_remove_elements/'
        )

    def test_add_remove_element(self):
        elements_added = int(input('How many elements will you add?'))
        elements_removed = int(input('How many elements will you remove?'))
        total_ements = elements_added - elements_removed

        add_button = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/button')
        sleep(3)

        for i in range(elements_added):
            add_button.click()

        for i in range(elements_removed):
            try:
                delete_button = self.driver.find_element_by_xpath(
                    '//*[@id="elements"]/button[1]')
                delete_button.click()
            except:
                print('Can not delete elements that does not exists')
                break
        if total_ements > 0:
            print(f"There are {total_ements} elements on screen")
        else:
            print('There are no elements')

        sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        verbosity=2,
        testRunner=HTMLTestRunner(
            output='reports',
            report_name='add-remove-elements-report'
        )
    )
