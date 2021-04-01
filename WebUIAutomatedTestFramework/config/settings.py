#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： 青城子
# datetime： 2021/3/28 13:46 
# ide： PyCharm

import os
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 浏览器有界面运行还是无界面运行,True是有界面运行,False无界面
INTERFACE = False
# 无头浏览器默认宽和高设置,无头浏览器无法通过driver.maximize_window()来讲浏览器最大化
# 通过driver.set_window_size(1552,840)来设置，这里用的是我自己笔记本的大小，具体可根据运行电脑屏幕设置
WIDTH = 1552
HEIGHT = 840
# True谷歌无头浏览器，False为phantomjs无头浏览器
HEADLESS_BROWSER = True
# 默认暂停时间
STOP_TIME = 3

# 测试报告目录
REPORT_PATH = os.path.join(BASE_DIR, "testreport")
# 截图目录
SCREENS_PATH = os.path.join(BASE_DIR, "screenshot")
# 数据目录
DATABASE = os.path.join(BASE_DIR, "database")
# 截图目录保存天数，默认10天
SAVE_DATE = 10
# 测试报告保存天数，默认10天
REPORT_SAVE_DATE = 10
# 图片目录
IMG_PATH = os.path.join(DATABASE, "imgs")
# 测试地址
URL = "http://adm.testfdd.com"
# 后台用户名
USERNAME = "tianx"
PASSWORD = "xxoo"

# 房源相关公共参数
PROPERTY_PARAMETERS = {
    "language": ['zh-cn', 'en', 'km', 'th'],  # 房源语言
    "house_ty": [1, 2, 3, 4, 5, 6, 7, 8, 9],  # 房源类型
    "city_type": [1, 114, 125],  # 金边、西哈努克、柴桢省
    "locations": {1: "金边", 114: "西哈努克", 125: "柴桢省"},
    "money": [1999, 2789, 9999, 5679, 8769],
    "area": [67, 89, 98, 125, 256, 324, 56],
    "address": ["金边桑园区商业大道11号", "金边国际机场", " 金边市森速区", "金边市玛卡拉区威旺", "金边市堆谷区万谷2"]
}

# 发送邮箱相关
# 发送方用户名
USER = "test_tx@126.com"
# 126邮箱中的授权码
AUTH_CODE = ""
HOST = "smtp.126.com"

# 日志文件命令
# 日志级别
LOG_LEVEL = "debug"
# 屏幕输出流
LOG_STREAM_LEVEL = "debug"
# 文件输出流
LOG_FILE_LEVEL = "info"

# 日志文件命名
LOG_FILE_NAME = os.path.join(BASE_DIR, "logs", datetime.datetime.now().strftime("%Y-%m-%d") + ".logs")
