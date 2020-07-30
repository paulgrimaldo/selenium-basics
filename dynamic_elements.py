import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner


class DynamicElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(
            'http://the-internet.herokuapp.com/disappearing_elements'
        )

    def test_name_elements(self):
        options = []
        total_options = 5
        tries = 1
        while len(options) < 5:
            options.clear()

            for i in range(total_options):
                try:
                    option_name = self.driver.find_element_by_xpath(
                        f'//*[@id="content"]/div/ul/li[{i + 1}]/a'
                    )
                    options.append(option_name.text)
                    print(options)
                except:
                    print(f"Option number {i+1} is not found")
                    tries += 1
                    self.driver.refresh()

        print(f"Finished in {tries}")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        verbosity=2,
        testRunner=HTMLTestRunner(
            output='reports',
            report_name='dynamic-elements-report'
        )
    )
