# encoding: utf-8
# @Time : 2022/12/15
# @File : 17.py

import httpx

headers = {
    'cookie': 'sessionid=yiz6zrvnmuait29ndzb7dufael2ooddj;',
    'user-agent': 'yuanrenxue.project;',
}
client = httpx.Client(http2=True)
base_url = 'https://match.yuanrenxue.com/api/match/17?page='
xx = []
for i in range(1, 6):
    response = client.get(base_url + str(i), headers=headers)
    data = response.json()
    values = data.get('data', '')
    for value in values:
        result = value.get('value', '')
        xx.append(result)

print(xx)
sx = 0
for ix in xx:
    sx = sx + int(ix)
print(sx)