# -*- coding: utf-8 -*-

import allure
import pytest


# @allure.severity(allure.severity_level.CRITICAL)
# @allure.link('http://www.baidu.com')
# def test_with_link():
#     # print('这是一条加了链接的测试')
#     pass
#
#
# TEST_CASE_LINK = 'https://github.com/qameta/allure-integrations/issures/8#issuecomment-268313637'
#
#
# @allure.severity(allure.severity_level.NORMAL)
# @allure.testcase(TEST_CASE_LINK, '登录用例')
# def test_with_testcase_link():
#     # print('这是一条测试用例的链接，链接到测试用例里面')
#     pass
#
#
# @allure.severity(allure.severity_level.NORMAL)
# @allure.issue('140', '这是一个问题')
# def test_bug():
#     pass


def test_attach_test():
    allure.attach('这是一个纯文本',attachment_type=allure.attachment_type.TEXT)

if __name__ == '__main__':
    pytest.main()
