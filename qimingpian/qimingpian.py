# encoding: utf-8
# @Time : 2022/10/26
# @File : qimingpian.py
import json

import requests
import execjs


url = 'https://vipapi.qimingpian.cn/DataList/productListVip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 '
                  'Safari/537.36 ',
}

response = requests.post(url=url, headers=headers)
encrypt_data = response.json()['encrypt_data']

# print(encrypt_data)
# 读js文件
with open('qimingpian.js', mode='r', encoding='utf-8') as f:
    js_content = f.read()


node = execjs.compile(js_content)
ret = node.call("sss", encrypt_data)
# print(ret)
json_data = json.loads(ret)
print(json_data)

