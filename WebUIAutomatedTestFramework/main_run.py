#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： 青城子
# datetime： 2021/3/28 13:46
# ide： PyCharm

import time
import unittest

from config import settings
from HTMLTestRunnerdChineseScreenshot import HTMLTestRunner

from util.send_email import send_mail
from util.common_module import PublicTools


def run_test_suite():
    """
    运行测试用例集
    :return:
    """
    return unittest.defaultTestLoader.discover("./testsuite", pattern="*_test.py")


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    time_now = time.strftime("%Y-%m-%d %H:%M")
    file_name = r"{0}\{1}{2}".format(settings.REPORT_PATH, now, "_rest.html")
    with open(file_name, "wb") as fr:
        HTMLTestRunner(
            stream=fr,
            title="XO自动化测试报告",
            description="XO自动化测试报告的描述",
            verbosity=2,
        ).run(run_test_suite())
    # 发送邮件
    # send_mail(file_name)
    # 删除10日前的测试报告和截图文件夹
    pub_obj = PublicTools()
    pub_obj.del_screen()
    pub_obj.del_report()
