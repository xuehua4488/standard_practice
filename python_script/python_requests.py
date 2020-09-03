# -*- coding: utf-8 -*-

import requests

# re = requests.get('http://www.baidu.com')
# print(re.text)

re = requests.post('http://httpbin.org/post', data={'key': 'value'})
print(re.text)
