# -*- coding: utf-8 -*-

class Calc:
    def add(self, a, b):
        print(f'a:{a},b:{b}')
        return a + b

    def sub(self, a, b):
        print(f'a:{a},b:{b}')
        return a - b

    def time(self, a, b):
        print(f'a:{a},b:{b}')
        return a * b

    def div(self, a, b):
        print(f'a:{a},b:{b}')
        try:
            c = a / b
        except Exception as e:
            print(e.args)
            # print(str(e))
            # print(repr(e))
        # except:
        #     print('未知错误')
        finally:
            return c
