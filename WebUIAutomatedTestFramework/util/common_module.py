#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： 青城子
# datetime： 2021/3/28 19:44 
# ide： PyCharm

import random
import time
import os
import re
import shutil

from config import settings
from util.LogHandler import logger

"""
为自动化提供公共方法
"""


class PublicTools:
    """
    公共类
    """

    def __init__(self):
        # 截图目录
        self.screen_path = settings.SCREENS_PATH
        # 测试报告目录
        self.report_path = settings.REPORT_PATH
        # 当日截图目录名称
        self.directory_time = time.strftime("%Y-%m-%d")

    def del_screen(self):
        """
        默认删除10日以前的截图文件夹
        :return:
        """
        try:
            # 删除前先判断目录是否存在
            if os.path.isdir(self.screen_path):
                if len(os.listdir(self.screen_path)) > settings.SAVE_DATE:
                    # 切换到screenshot目录
                    os.chdir(self.screen_path)
                    scr_path = os.getcwd()
                    for d in os.listdir(scr_path)[0:]:
                        shutil.rmtree(d)
                        if len(os.listdir(scr_path)) <= settings.SAVE_DATE:
                            break
                else:
                    return "不够10日"
            else:
                return "截图目录不存在"
        except Exception as error:
            logger().info("删除截图文件夹失败:{0}".format(error))
        else:
            return "删除截图文件夹成功"

    def del_report(self):
        """
        默认删除10日以前的测试报告
        :return:
        """
        try:
            if os.path.isdir(self.report_path):
                if len(os.listdir(self.report_path)) > settings.REPORT_SAVE_DATE:
                    os.chdir(self.report_path)  # 切换到report目录
                    report_path = os.getcwd()
                    for d in os.listdir(report_path)[0:]:
                        os.remove(d)
                        if len(os.listdir(report_path)) <= settings.REPORT_SAVE_DATE:
                            break
                else:
                    return "测试报告不够10日"
            else:
                return "测试报告目录不存在"
        except Exception as error:
            logger().info("删除测试报告失败:{0}".format(error))
        else:
            return "删除测试报告成功"

    def create_screen_catalog(self):
        """
        创建截图目录
        :return:
        """
        # 判断截图目录ScreenShot是否存在，如果存在就忽略，如果不存在就创建
        if os.path.exists(self.screen_path):
            pass
        else:
            os.mkdir("{0}".format(self.screen_path))

        dir_path = "{0}".format(self.screen_path)

        # 已当日命名的二级目录
        # 判断是否已经存在
        if os.path.exists(r"{0}\{1}".format(dir_path, self.directory_time)):
            pass
        else:
            os.mkdir(r"{0}\{1}".format(dir_path, self.directory_time))

        # 存放成功时截图的三级目录
        # 判断是否已经存在
        if os.path.exists(r"{0}\{1}\{2}".format(dir_path, self.directory_time, 'success')):
            pass
        else:
            os.makedirs(r"{0}\{1}\{2}".format(dir_path, self.directory_time, 'success'))
        dir_success = r"{0}\{1}\{2}".format(dir_path, self.directory_time, 'success')

        # 存放失败时截图的三级目录
        if os.path.exists(r"{0}\{1}\{2}".format(dir_path, self.directory_time, 'errorsdir')):
            pass
        else:
            os.mkdir(r"{0}\{1}\{2}".format(dir_path, self.directory_time, 'errorsdir'))
        dir_errors = r"{0}\{1}\{2}".format(dir_path, self.directory_time, 'errorsdir')
        return dir_success, dir_errors

    def get_date(self, text_type=1):
        """
        读取database里面的文本字典，默认读取标题字典
        :return:返回获取到的随机内容
        :param text_type:
        :return:
        """
        try:
            if text_type == 1:
                file_name = "title"
            else:
                file_name = "description"
            data_file = r"{0}\{1}\{2}".format(settings.DATABASE, "content", file_name)
            data_list = []
            with open(data_file, "r+", encoding="utf-8") as fr:
                for i in fr:
                    if i.strip() == "":
                        continue
                    else:
                        data_list.append(i.strip())
        except Exception as error:
            print("读取文件错误:{0}".format(error))
            logger().info("读取房源文件错误:{0}".format(error))
        else:
            return data_list[random.randrange(0, len(data_list))]

    def get_image(self):
        """
        读取图片
        :return:
        """
        try:
            image_list = []
            image_file = r"{0}\{1}".format(settings.IMG_PATH, "housing")
            # os.listdir()返回path指定的文件夹包含的文件或文件夹的名字的列表
            for i in os.listdir(image_file):
                if re.findall(r'.*.jpg', i):
                    path_jpg = r"{0}\{1}\{2}".format(settings.IMG_PATH, "housing", i)
                    image_list.append(path_jpg)
                else:
                    continue
        except Exception as error:
            print("获取图片失败:{0}".format(error))
            logger().info("获取图片错误:{0}".format(error))
        else:
            return random.sample(image_list, k=random.randrange(1, 5))


