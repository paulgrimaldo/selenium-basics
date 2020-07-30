import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver


class HelloWorld(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        cls.driver.implicitly_wait(10)

    def test_hello_world(self):
        self.driver.get('htpps://www.google.com')

    def test_visit_wikipedia(self):
        self.driver.get('https://www.wikipedia.com')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(
        verbosity=2,
        testRunner=HTMLTestRunner(
            output='reports',
            report_name='hello-world-report'
        )
    )
