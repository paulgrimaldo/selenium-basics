import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from time import sleep


class MercadoLibreSearchPlaystation4(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        self.driver.get('https://www.mercadolibre.com')
        self.driver.maximize_window()

    def test_search_ps4(self):
        country = self.driver.find_element_by_id('CO')
        country.click()
        sleep(3)
        search_field = self.driver.find_element_by_name('as_word')
        search_field.clear()
        search_field.click()
        search_field.send_keys('playstation 4')
        search_field.submit()
        sleep(3)

        location = self.driver.find_element_by_partial_link_text('Bogotá D.C.')
        location.click()
        sleep(3)

        condition = self.driver.find_element_by_partial_link_text('Nuevo')
        condition.click()
        sleep(3)

        order_menu = self.driver.find_element_by_css_selector(
            '#root-app > div > div > aside > section.ui-search-view-options > div.ui-search-view-options__group > div.ui-search-sort-filter > div > div > button'
        )
        order_menu.click()
        higher_price = self.driver.find_element_by_css_selector(
            '#root-app > div > div > aside > section.ui-search-view-options > div.ui-search-view-options__group > div.ui-search-sort-filter > div > div > div > ul > li:nth-child(3) > div > div > a'
        )
        higher_price.click()
        sleep(3)

        products = {}

        for i in range(5):
            article_name = self.driver.find_element_by_xpath(
                f'//*[@id="root-app"]/div/div/section/ol/li[{i +1}]/div/div/div[2]/div[1]/a/h2'
            ).text
            article_price = self.driver.find_element_by_xpath(
                f'//*[@id="root-app"]/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/div/div/span[1]/span[2]'
            ).text

            products[article_name] = article_price

        print(products)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        verbosity=2,
        testRunner=HTMLTestRunner(
            output='reports',
            report_name='mercado-libre-report'
        )
    )
