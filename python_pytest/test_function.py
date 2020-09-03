# -*- coding: utf-8 -*-

import pytest


def test_setup_module():
    print('this is a module setup')


def test_teardown_module():
    print('this is a module teardown_class')


def test_setup_function():
    print('this is a function setup')


def test_teardown_function():
    print('this is a function teardown')


class TestDemo:
    def test_setup_class(self):
        print('this is a setup_class in Class')

    def test_teardown(self):
        print('this is a teardown_class in Class')

    def test_case01(self):
        print('this is a test_case01')

    def test_setup_method(self):
        print('this is a setup_method in method')

    def test_teardown_method(self):
        print('this is a teardown_method in method')


if __name__ == '__main__':
    pytest.main()
