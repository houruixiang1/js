import requests
import execjs

url = 'https://www.newrank.cn/xdnphb/main/v1/day/rank'

headers = {
    # ':authority': 'www.newrank.cn',
    # ':method': 'POST',
    # ':path': '/xdnphb/main/v1/day/rank',
    # ':scheme': 'https',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-length': '148',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.newrank.cn',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 '
                  'Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

# 读js文件
with open('ranking.js', mode='r', encoding='utf-8') as f:
    js_content = f.read()

# 得到参数nonce，9位的随机字符串
context = execjs.compile(js_content)
ret = context.call("get_nonce", "")
print(ret)

# 得到参数xyz，标准md5
cc = f'/xdnphb/main/v1/day/rank?AppKey=joker&end=2022-09-06&rank_name=文化&rank_name_group=生活&start=2022-09-06&nonce={ret}'
content = execjs.compile(js_content)
reet = content.call("get_xyz", cc)
print(reet)

params = {
    'end': '2022-09-06',
    'rank_name': '文化',
    'rank_name_group': '生活',
    'start': '2022-09-06',
    'nonce': ret,
    'xyz': reet
}

resp = requests.post(url=url, headers=headers, data=params)
print(resp.text)
