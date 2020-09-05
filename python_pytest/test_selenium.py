# -*- coding: utf-8 -*-

from selenium import webdriver
import pytest


class TestSelenium:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown_method(self):
        self.driver.quit()

    def test_selenium(self):
        self.driver.get('http://www.baidu.com')
        self.driver.find_element_by_id('kw').send_keys('霍格沃兹测试学院')
        self.driver.find_element_by_id('su').click()
        self.driver.find_element_by_partial_link_text('霍格沃兹测试学院腾讯课堂官网').click()
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        self.driver.find_element_by_partial_link_text('名企定向培养').click()



