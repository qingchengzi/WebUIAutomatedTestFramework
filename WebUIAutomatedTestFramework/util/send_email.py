#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： 青城子
# datetime： 2021/3/28 15:12 
# ide： PyCharm

import yagmail

from config import settings


def send_mail(report):
    """
    password是126邮箱中的授权码，不是邮箱的登录密码
    :param report:
    :return:
    """
    yag = yagmail.SMTP(user=settings.USER, password=settings.AUTH_CODE, host=settings.HOST)
    subject = "主题，自动化测试报告"
    contents = "正文，请查看附件"
    yag.send("352932341@qq.com", subject, contents, report)
    print("发送邮件成功")
