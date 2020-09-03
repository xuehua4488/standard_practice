# -*- coding: utf-8 -*-
import pytest
import yaml
@pytest.mark.parametrize(['a','b'],[(1,2),(8,9)])
def test_eval(a,b):
    # print('a+b=',a+b)
    print(a)
    print(b)


