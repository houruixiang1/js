# encoding: utf-8
# @Time : 2022/12/15
# @File : 15.py

# -*- coding: utf-8 -*-
import math
import random
import time
import pywasm
import requests


def main():
    sums = 0
    t = int(time.time())
    t1 = int(t / 2)
    t2 = int(t / 2 - math.floor(random.random() * 50 + 1))
    vm = pywasm.load("./main.wasm")
    r = vm.exec("encode", [t1, t2])
    m = f"{r}|{t1}|{t2}"
    for i in range(1, 6):
        params = {
            "m": m,
            "page": i,
        }
        headers = {
            'user-agent': 'yuanrenxue.project;',
            'cookie': 'sessionid=yiz6zrvnmuait29ndzb7dufael2ooddj;'
        }
        response = requests.get(url="https://match.yuanrenxue.com/api/match/15", params=params, headers=headers).json()
        # print(response.text)
        for each in response["data"]:
            sums += each["value"]
    print(sums)


if __name__ == "__main__":
    url = 'https://match.yuanrenxue.com/static/match/match15/main.wasm'
    headers = {
        'user-agent': 'yuanrenxue.project;',
        'cookie': 'sessionid=yiz6zrvnmuait29ndzb7dufael2ooddj;'
    }
    data = requests.get(url=url, headers=headers).content
    with open('./main.wasm', 'wb') as f:
        f.write(data)
    main()
