# # encoding: utf-8
# # @Time : 2022/11/10
# # @File : demo.py
#
# # 90000   8638302113.4100
# # 100000   8966821800.3500
# # 150000    10285911780.1400
# # import datetime
# #
# # print(458*60)
# #
# # day = datetime.date.today().isoweekday()
# # print(day)
#
# # proId = ''
# # proId.rstrip(',')
#
# from speedtest import Speedtest
#
# def Testing_Speed(net):
#     download = net.download()
#     upload = net.upload()
#     print(f'下载速度: {download/(1024*1024)} Mbps')
#     print(f'上传速度: {upload/(1024*1024)} Mbps')
#     print("开始网速的测试 ...")
#
# net = Speedtest()
# Testing_Speed(net)
#
# import speedtest  # 导入speedtest_cli
#
# print("准备测试ing...")
#
# # 创建实例对象
# test = speedtest.Speedtest()
# # 获取可用于测试的服务器列表
# test.get_servers()
# # 筛选出最佳服务器
# best = test.get_best_server()
#
# print("正在测试ing...")
#
# # 下载速度
# download_speed = int(test.download() / 1024 / 1024)
# # 上传速度
# upload_speed = int(test.upload() / 1024 / 1024)
#
# # 输出结果
# print("下载速度：" + str(download_speed) + " Mbits")
from loguru import logger


def jjj(tt):
    try:
        num = int(tt)
        return True, num
    except Exception as err:
        logger.error(f"解析出错！！！，{err}")
        return False, tt

tt = '111'
print(jjj(tt))

print((1634301829.3224893-1632341828.3055165)/100)