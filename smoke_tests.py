from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from assertions import AssertionsTest
from seach_input_tests import SearchInputTest

assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_input_test = TestLoader().loadTestsFromTestCase(SearchInputTest)

smoke_test = TestSuite([assertions_test, search_input_test])

kwargs = {
    'output': 'smoke-report'
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)
