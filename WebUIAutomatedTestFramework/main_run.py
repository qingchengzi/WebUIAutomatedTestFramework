#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tian'
__data__ = '2021/3/3 15:06'

import time
import unittest

from HTMLTestRunnerSavrShot import HTMLTestRunner  # 失败时截图的测试报告

from util import send_email
from util.common_class import PublicTools
from config import setting


def run_test_suite():
    """
    运行测试用例集
    :return:
    """
    return unittest.defaultTestLoader.discover("./testsuite", pattern="*_test.py")


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    time_now = time.strftime("%Y-%m-%d %H:%M")
    file_name = "{0}\{1}{2}".format(setting.REPORT_PATH, now, "_rest.html")
    print(file_name)
    with open(file_name, 'wb') as f:
        HTMLTestRunner(
            stream=f,
            title="港湾置业后台测试报告",
            description="港湾置业后台功能测试报告",
            verbosity=2,
        ).run(run_test_suite())

    # 发送邮件
    # send_email.main_email()
    # 删除10日前的测试报告和截图
    pub_obj = PublicTools()
    pub_obj.del_report()
    pub_obj.del_screen()
