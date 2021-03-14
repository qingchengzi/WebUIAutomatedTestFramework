#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tian'
__data__ = '2021/3/3 16:03'

import random
import time
import os
import shutil
import re

from config import setting

"""
公共方法类
"""


class PublicTools:
    """
     公共工具类
    """

    def __init__(self):
        self.current_time = time.strftime("%Y-%m-%d %H:%M:%S")  # 记录错误日志的时间
        self.report_path = setting.REPORT_PATH  # 测试报告目录
        self.screen_path = setting.SCREENS_PATH  # 截图目录

    def write_error_log(self, *args, **kwargs):
        """
        将错误信息写入到log日志中
        :param args:
        :param kwargs:
        :return:
        """
        print("到了啊中辣啊", args)
        if args:
            content_error_file = '{0}--->{1}\n'.format(self.current_time, args[0])
            print(content_error_file)
            file_dir = "{0}/log_error.txt".format(setting.LOG_PATH)
            with open(file_dir, "a+", encoding="utf-8") as wr:
                wr.write(content_error_file)
        else:
            print("日志写入失败")

    def read_database(self, text_type=1):
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

            data_file = "{0}\{1}\{2}".format(setting.DATABASE, "textcontent", file_name)
            data_list = []
            with open(data_file, "r+", encoding="utf-8") as fr:
                for i in fr:
                    if i.strip() == "":
                        continue
                    else:
                        data_list.append(i.strip())
        except Exception as error:
            self.write_error_log("读取database目录中的文件内容失败:{0}".format(error), )
        else:
            return data_list[random.randrange(0, len(data_list))]

    def get_image(self):
        """
        读取图片
        :return:
        """
        try:
            image_list = []
            image_file = "{0}\{1}".format(setting.IMG_PATH, "housingpictures")
            # os.listdir()返回path指定的文件夹包含的文件或文件夹的名字的列表
            for i in os.listdir(image_file):
                if re.findall(r'.*.jpg', i):
                    path_jpg = "{0}\{1}\{2}".format(setting.IMG_PATH, "housingpictures", i)
                    image_list.append(path_jpg)
                else:
                    continue
        except Exception as error:
            self.write_error_log("读取图片失败:{0}".format(error))
        else:
            return image_list

    def del_screen(self):
        """
        默认删除10日以前的截图文件夹
        :return:
        """
        try:
            if os.path.isdir(self.screen_path):  # 删除前先判断目录是否存在
                if len(os.listdir(self.screen_path)) > setting.SAVE_DATE:
                    os.chdir(self.screen_path)  # 切换到screenshot目录
                    scr_path = os.getcwd()
                    for d in os.listdir(scr_path)[0:]:
                        shutil.rmtree(d)
                        if len(os.listdir(scr_path)) <= setting.SAVE_DATE: break
            else:
                print("目录不存在")
        except Exception as error:
            self.write_error_log("删除截图文件夹失败:{0}".format(error), )
        else:
            return "删除截图文件夹成功"

    def del_report(self):
        """
        默认删除10日以前的测试报告
        :return:
        """
        try:
            if os.path.isdir(self.report_path):
                if len(os.listdir(self.report_path)) > setting.REPORT_SAVE_DATE:
                    os.chdir(self.report_path)  # 切换到report目录
                    report_path = os.getcwd()
                    for d in os.listdir(report_path)[0:]:
                        os.remove(d)
                        if len(os.listdir(report_path)) <= setting.REPORT_SAVE_DATE: break
            else:
                print("删除测试报告文件不存在")
        except Exception as error:
            self.write_error_log("删除测试报告文件夹失败:{0}".format(error), )
        else:
            return "删除测试报告文件夹成功"


if __name__ == '__main__':
    obj = PublicTools().write_error_log("{0}{1}".format("添加住宅出租房源失败:", 'ssssss'))
