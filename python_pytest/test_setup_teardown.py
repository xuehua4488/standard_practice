# -*- coding: utf-8 -*-

import pytest
# @pytest.fixture(autouse='True')

class TestDemo:
    def test_demo01(self):
        print('test_demo01 in TestDemo class')

    def test_demo02(self):
        print('test_demo02 in TestDemo class')


def test_case01():
    print('execute testcase01')


def test_case02():
    print('execute testcase02')


def test_case03():
    print('execute testcase03')

#
# @pytest.mark.parametrize('x', [1, 2])
# @pytest.mark.parametrize('y', [8, 10, 11])
# def test_para(x, y):
#     print('有多少组?', {x}, {y})


if __name__ == '__main__':
    pytest.main("-v -x TestDemo")
    # pytest.main(['-v','-s','TestDemo'])
