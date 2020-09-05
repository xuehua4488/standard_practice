# -*- coding: utf-8 -*-
import pytest

@pytest.mark.search
def test_search1():
    print('search1 function')

@pytest.mark.search
def test_search2():
    print('search2 function')

@pytest.mark.search
def test_search3():
    print('search3 function')

@pytest.mark.login
def test_login1(login):
    print('test01 login')

@pytest.mark.login
def test_login2():
    print('test02 login')

@pytest.mark.login
def test_login3():
    print('test03 login')

@pytest.mark.login
def test_login4():
    print('test04 login')


if __name__ == '__main__':
    pytest.main()

