import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver


class TestSeachPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        self.driver.get('http://demo.onestepcheckout.com/')
        self.driver.maximize_window()

    def test_search_text_field(self):
        seach_field = self.driver.find_element_by_id("search")

    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element_by_name("q")

    def test_search_text_field_by_class_name(self):
        search_field = self.driver.find_element_by_class_name("input-text")

    def test_search_button_enabled(self):
        button = self.driver.find_element_by_class_name("button")

    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_element_by_class_name("promos")
        banners = banner_list.find_elements_by_tag_name('img')
        self.assertEqual(3, len(banners))

    def test_vip_promo(self):
        vip_promo = self.driver.find_element_by_xpath(
            '//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div/ul/li[2]/a/img'
        )

    def test_icon(self):
        icon = self.driver.find_element_by_css_selector(
            "div.header-minicart span.icon"
        )

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        verbosity=2,
        testRunner=HTMLTestRunner(
            output='reports',
            report_name='test-search-report'
        )
    )
