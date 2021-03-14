#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tian'
__data__ = '2021/3/3 14:57'

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 测试报告目录
REPORT_PATH = os.path.join(BASE_DIR, "report")
# 截图目录
SCREENS_PATH = os.path.join(BASE_DIR, "screenshot")
# 日志目录
LOG_PATH = os.path.join(BASE_DIR, "log")
# 数据目录
DATABASE = os.path.join(BASE_DIR, "database")
# 图片目录
IMG_PATH = os.path.join(DATABASE, "img")
# time.sleep()暂停秒数默认配置
STOP_TIME = 3

# 是否启用浏览器界面，调试阶段需要启用浏览器界面，正常运行就不需要，False启用浏览器界面
INTERFACE = False
# 无图浏览器，有谷歌无头浏览器和phantomjs无头浏览器,默认为谷歌无头浏览器
# True谷歌无头浏览器，Fasle为phantomjs无头浏览器
HEADLESS_BROWSER = True
# 截图保存日期，默认10天
SAVE_DATE = 10
# 测试报告
REPORT_SAVE_DATE = 10
# 公共参数
COMMON_PARAMETERS = {
    "url": "http://adm.testfdd.com",  # 测试url
    "log_pag_path": "/Home/Login",  # 后台登录页面
    "admin": "xxxxx",  # 登录用户名
    "password": "xxxxx"  # 密码
}

# 房源相关公共参数
PROPERTY_PARAMETERS = {
    "language": ['zh-cn', 'en', 'km', 'th'],  # 房源语言
    "house_ty": [1, 2, 3, 4, 5, 6, 7, 8, 9],  # 房源类型
    "city_type": [1, 114, 125],  # 金边、西哈努克、柴桢省
    "locations": {1: "金边", 114: "西哈努克", 125: "柴桢省"},
    "address": ["金边桑园区商业大道11号", "金边国际机场", " 金边市森速区", "金边市玛卡拉区威旺", "金边市堆谷区万谷2"]
}
