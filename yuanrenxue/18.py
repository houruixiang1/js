# encoding: utf-8
# @Time : 2022/12/15
# @File : 18.py

from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import time
import base64
import requests

# headers = {
#     'authority': 'match.yuanrenxue.com',
#     'pragma': 'no-cache',
#     'cache-control': 'no-cache',
#     'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
#     'sec-ch-ua-mobile': '?0',
#     'user-agent': 'yuanrenxue.project;',
#     'sec-ch-ua-platform': '"Windows"',
#     'accept': '*/*',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-dest': 'empty',
#     'referer': 'https://match.yuanrenxue.com/match/18',
#     'accept-language': 'zh-CN,zh;q=0.9',
#     'cookie': 'sessionid=t3qu97inecyo58bj9qy8sj6echyl24yk; '
# }

headers = {
    # "cookie": "sessionid=t3qu97inecyo58bj9qy8sj6echyl24yk",
    "user-agent": "yuanrenxue.project"
}

cookies = {
    "sessionid": "t3qu97inecyo58bj9qy8sj6echyl24yk",
}
xx = []
for i in range(1, 6):
    # 构造有鼠标轨迹构成的text值,鼠标移动轨迹可以固定
    text = '{0}|756d354,756d354,756u354,756u354'.format(str(i))
    print(text)
    byte_text = bytes(text, encoding="utf-8")  # 转换为字节形式
    print(byte_text)

    # 将时间戳转换为KEY,iv
    t = int(time.time())
    print(hex(t))
    iv = hex(t)[2:] * 2
    byte_iv = bytes(iv, encoding="utf-8")
    byte_key = byte_iv

    # 初始化加密器，使用CBC模式进行加密
    cryptor = AES.new(byte_key, AES.MODE_CBC, byte_iv)
    enc_result = base64.b64encode(cryptor.encrypt(pad(byte_text, 16)))

    params = (
        ('page', str(i)),
        ('t', str(t)),
        ('v', str(enc_result, 'utf-8')),
    )

    response = requests.get('https://match.yuanrenxue.com/match/18data', headers=headers, cookies=cookies, params=params)
    # response = requests.get('https://match.yuanrenxue.com/match/18data', headers=headers, params=params)
    data = response.json()
    print(data)
    values = data.get('data', '')
    for value in values:
        result = value.get('value', '')
        xx.append(result)

print(xx)
sx = 0
for ix in xx:
    sx = sx + int(ix)
print(sx)