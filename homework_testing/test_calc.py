# -*- coding: utf-8 -*-
import pytest
import yaml
import os
print(os.path)
#
from data.calc import Calc


class TestDemo:
    def setup(self):
        self.calc = Calc()

    @pytest.mark.parametrize('testdate1', yaml.safe_load(open('..\data\data.yml')))
    def test_add(self,testdate1):
        # print(f'a:{a},b:{b}')
        c = self.calc.add(**testdate1)
        print(f'c : {c}')

    @pytest.mark.parametrize('testdate2', yaml.safe_load(open('..\data\data.yml')))
    def test_sub(self,testdate2):
        c = self.calc.sub(**testdate2)
        print(f'c :{c}')

    @pytest.mark.parametrize('testdate3', yaml.safe_load(open('..\data\data.yml')))
    def test_time(self,testdate3):
        c = self.calc.time(**testdate3)
        print(f'c :{c}')

    @pytest.mark.parametrize('testdate4', yaml.safe_load(open('..\data\div.yml')))
    def test_div(self, testdate4):
        c = self.calc.div(**testdate4)
        print(f'c :{c}')

#
# if __name__ == '__main__':
#     pytest.main()
#     f = open('../data/data.yml', 'r',encoding='UTF-8')
#     data = f.read()
#     print(type(data))
#     print(data)
#
#     d = yaml.load(data)
#     print(d)
#     print(type(d))