# -*- coding: utf-8 -*-
import pytest


def open():
    print('setup start')
    print('open browser')
    # yield
    print('teardown')
    print('close browser')


@pytest.fixture()
def login():
    print('登录成功')
    # yield
    # print('继续登录成功')

