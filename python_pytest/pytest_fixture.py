# -*- coding: utf-8 -*-
import pytest


@pytest.fixture(params=[1, 2, 3])
def fixture_param(request):
    request.param
    print('\033[31;1m我是fixture_para,这是第%s次打印\033[0m' % request.param)
    return request.param


# # 一定要加indirect,要不就会直接把fixture_param当成测试函数的一个参数来用，加上indirect=True这个参数，才会在fixture_para的查找。
@pytest.mark.parametrize('fixture_param', ['a', 'b'], indirect=True)
@pytest.mark.parametrize('a,b', [(1, 6), (2, 7), (3, 8), (4, 9)])
def test_fixture_param(a, b, fixture_param):
    print('我是test_fixture_para函数,参数a是%s,b是%s' % (a, b))
    # print('我是test_fixture_para函数,参数为%s,'%fixture_param)


if __name__ == '__main__':
    pytest.main(['-s', 'pytest_fixture.py'])
