# encoding: utf-8
# @Time : 2022/9/20
# @File : demo_flask
# -*- coding: utf-8 -*-
import platform
import re
import socket
import time

import pymysql
import os
import json
from loguru import logger

# from flask_cors import *

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

# from kafka import KafkaProducer
from flask import Flask, request

app = Flask(__name__)

HOST_NAME = socket.gethostname()
IP = socket.gethostbyname(HOST_NAME)

project = "Mainfest"
metrices = "ChromeCreateTask"


@app.route('/index', methods=['GET'])
def indextest1():
    # source = request.args.get("source")
    # cookie = request.args.get("cookie")
    # first_id = request.args.get("first_id")
    # data1 = getcontent(source, cookie, first_id)
    return '服务已成功启动！'


@app.route('/createTask', methods=['POST'])
def indextest():
    data = request.json
    if data:
        info = data.get('data', '').get('info', '')
        params = data.get('data', '').get('params', '')
        shop_id = info.get('shop_id', '')
        origin = info.get('origin', '')
        flag = info.get('flag', '')  # SKU or SPU
        lv2name = info.get('lv2name', '')
        lv3name = info.get('lv3name', '')
        lv2cid = info.get('lv2cid', '')
        lv3cid = info.get('lv3cid', '')
        default_start_time = params.get('时间选择器1', '')
        default_end_time = params.get('时间选择器2', '')
        description = params.get('text2', '')  # 标识字段
        cookie = params.get('text3', '')

        result = createTask(shop_id, flag, lv2name, lv3name, lv2cid, lv3cid, default_start_time, default_end_time,
                            description, origin, cookie)
    return result


# def kafka_log(project, metrices, key, success=0, fail=0, hostname=None, ip=None, thread=None, topic="logkeyword",
#               asy=False):
#     """
#         不得使用特殊符号，以及指标名为单个词（shoplist √，shop-list ×）
#         :param topic:
#         :param project: 项目名
#         :param metrices: 指标名
#         :param key: 关键自定义指标
#         :param success: 成功数
#         :param fail: 失败数
#         :param hostname: 主机名，手机序列号, 默认本机主机名
#         :param ip: ip，若使用代理则为代理ip， 默认本地ip
#         :param thread: 进程、线程、协程等标志id，也可为宝贝id等，默认nint
#         :return: code=200,success; code=100,err
#         """
#     if hostname is None:
#         hostname = socket.gethostname()
#     if ip is None:
#         ip = socket.gethostbyname(socket.gethostname())
#     if thread is None:
#         thread = "nint"
#     server = "192.168.3.239:9092,192.168.3.156:9092,192.168.3.250:9092"
#     # topic = "DouYinMult"
#     try:
#         kp = KafkaProducer(bootstrap_servers=server)
#         current = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#         msg = f"{current} {hostname} {ip} {project} {metrices} {thread} {key} {success} {fail}"
#         if asy:
#             # "异步发送"
#             kp.send(topic, msg.encode('utf-8'))
#             kp.flush()
#         else:
#             future = kp.send(topic, msg.encode('utf-8'))
#             record_metadata = future.get(timeout=10)
#             partition = record_metadata.partition
#             offset = record_metadata.offset
#             kp.close()
#             return {"code": 200, "data": {"partition": {partition}, "offset": {offset}}}
#     except Exception as e:
#         return {"code": 100, "data": {"err": {e}}}


def createTask(shop_id, flag, lv2name, lv3name, lv2cid, lv3cid, default_start_time, default_end_time, description,
               origin, cookie):
    conn = pymysql.connect(
        host='192.168.3.187',
        port=13306,
        user='dataway-rw',
        passwd='QqHVMhmN*8',
        db='jd_sz'
    )
    if platform.system() == 'Windows':
        conn = pymysql.connect(
            host='127.0.0.1',
            port=28015,
            user='dataway-rw',
            passwd='QqHVMhmN*8',
            db='jd_sz'
        )
    if lv3name:
        sql = f"insert into chrome_tasks (shop_id, flag, name_lv2, name_lv3, cid_lv2, " \
              f"cid_lv3, default_start_time, default_end_time, description, origin, cookie, is_crawled) " \
              f"values ({shop_id}, '{flag}', '{lv2name}', '{lv3name}', {lv2cid}, {lv3cid}, " \
              f"'{default_start_time}', '{default_end_time}', '{description}', '{origin}', '{cookie}', 0)"
    else:
        sql = f"insert into chrome_tasks (shop_id, flag, name_lv2, name_lv3, cid_lv2, " \
              f"cid_lv3, default_start_time, default_end_time, description, origin, cookie, is_crawled) " \
              f"values ({shop_id}, '{flag}', '{lv2name}', {lv3name}, {lv2cid}, {lv3cid}, " \
              f"'{default_start_time}', '{default_end_time}', '{description}', '{origin}', '{cookie}', 0)"
    real_sql = sql.replace('None', 'NULL')
    logger.info(real_sql)

    cur = conn.cursor()
    cur.execute(real_sql)
    conn.commit()

    cur.close()
    conn.close()

    # kafka_log(project=project, metrices=metrices, key="成功1", success=1, fail=0, hostname=HOST_NAME, ip=IP,
    #           asy=True)

    result = {
        'code': 200,
        'info': '插入成功'
    }
    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7788)
