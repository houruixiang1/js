# encoding: utf-8
# @Time : 2022/9/16
# @File : wanfang.py

import blackboxprotobuf
# a = "ï²®†Ë²®† ·Äô".encode()
# deserialize_data, message_type =blackboxprotobuf.protobuf_to_json(a)
# print(deserialize_data)  # 非序列化的原始数据
# print(message_type)  # 消息类型结构

message_type = {'1': {'type': 'int', 'name': ''}, '2': {'type': 'int', 'name': ''}, '3': {'type': 'int', 'name': ''}, '4': {'type': 'int', 'name': ''}}
before_data = {'1': 1, '2': 312312312442, '3': 8709708978, '4': 78971987}
form_data = blackboxprotobuf.encode_message(before_data, message_type)
print(form_data)

content = b'\x08\x9f\x19\x10\xbc)\x18\xa9) \x9f\x19(\x86#0\xc7(8\xa1"@\xfeBH\xd2:P\xcd\x03'
# content = form_data
print(blackboxprotobuf.protobuf_to_json(content))

