# -*- coding: utf-8 -*-
import allure
import pytest
from selenium import webdriver
import time


@pytest.mark.parametrize('test_data1', ['allure', 'pytest', 'unittest'])
def test_steps_demo(test_data1):
    drive = webdriver.Chrome()
    drive.maximize_window()
    drive.get('http://www.baidu.com')
    print('test_data1=%s,' % test_data1)
    drive.find_element_by_id('kw').send_keys(test_data1)
    time.sleep(1)
    drive.find_element_by_id('su').click()
    time.sleep(1)
    drive.save_screenshot('./result/baidu.png')
    allure.attach.file('./result/baidu.png', attachment_type=allure.attachment_type.PNG, name='image')
    allure.attach('<head></head><body>首页</body>', 'attach with html type', allure.attachment_type.HTML)
    drive.quit()
