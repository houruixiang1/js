# encoding: utf-8
# @Time : 2022/10/28
# @File : youdaofanyi.py
import json
import time

import execjs
import requests

url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'Cookie': 'OUTFOX_SEARCH_USER_ID_NCOO=1703999635.1194286; OUTFOX_SEARCH_USER_ID=890318392@101.80.230.211; ___rl__test__cookies=1667207245708',
    'Origin': 'https://fanyi.youdao.com',
    'Host': 'fanyi.youdao.com',
    'Referer': 'https://fanyi.youdao.com/'
}


# keyword = input(f"请输入要翻译的语句:")
# if keyword == '':
keyword = '我有一只小狗'
# timestamp = int(time.time() * 1000)

with open('youdao.js', mode='r', encoding='utf-8') as f:
    js_content = f.read()

node = execjs.compile(js_content)
ret = node.call("ss", keyword)
print(ret)

data = {
    'i': keyword,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': ret["salt"],
    'sign': ret["sign"],
    'lts': ret["ts"],
    'bv': ret["bv"],
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME'
}
print(data)
resp = requests.post(url=url, headers=headers, data=data)
print(resp.text)
