import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner


class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        self.driver.get('http://demo-store.seleniumacademy.com/')
        self.driver.maximize_window()

    def test_new_user(self):
        self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/header/div/div[2]/div/a/span[2]').click()
        self.driver.find_element_by_link_text('Log In').click()

        create_account_button = self.driver.find_element_by_xpath(
            '//*[@id="login-form"]/div/div[1]/div[2]/a')

        self.assertTrue(create_account_button.is_displayed()
                        and create_account_button.is_enabled())
        create_account_button.click()
        self.assertEqual('Create New Customer Account', self.driver.title)

        first_name = self.driver.find_element_by_id('firstname')
        middle_name = self.driver.find_element_by_id('middlename')
        last_name = self.driver.find_element_by_id('lastname')
        email_address = self.driver.find_element_by_id('email_address')
        new_letters = self.driver.find_element_by_id('is_subscribed')
        password = self.driver.find_element_by_id('password')
        password_confirmation = self.driver.find_element_by_id('confirmation')
        register_button = self.driver.find_element_by_xpath(
            '//*[@id="form-validate"]/div[2]/button')

        self.assertTrue(first_name.is_enabled()
                        and middle_name.is_enabled()
                        and last_name.is_enabled()
                        and email_address.is_enabled()
                        and new_letters.is_enabled()
                        and password.is_enabled()
                        and password_confirmation.is_enabled()
                        and register_button.is_enabled()
                        )
        first_name.send_keys('Paul')
        middle_name.send_keys('Fernando')
        last_name.send_keys('Grimaldo')
        email_address.send_keys('paul@paul.com')
        password.send_keys('123')
        password_confirmation.send_keys('123')
        register_button.click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        verbosity=2,
        testRunner=HTMLTestRunner(
            output='reports',
            report_name='register-new-user-report'
        )
    )
