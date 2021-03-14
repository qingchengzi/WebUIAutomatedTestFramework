#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tian'
__data__ = '2021/3/4 11:30'

import time

from page.loginpage import LoginPage
from config import setting


class LoginHandle:
    """
    登录页面的逻辑处理
    """

    def __init__(self):
        self.obj_login = LoginPage()
        self.username = setting.COMMON_PARAMETERS.get("admin")
        self.pass_wrod = setting.COMMON_PARAMETERS.get("password")
        print(self.username)
        print(self.pass_wrod)

    def open_admin_page(self):
        """
        登录页面是否打开正常
        :return: 正常返回True
        """
        return self.obj_login.open_admin_page()

    def user_and_password_null(self):
        """
        用户名和密码为空
        :return:
        """
        return self.obj_login.user_and_password_all_null()


    def user_and_password_error(self):
        """
        用户名和密码都输入错误
        :return:
        """
        return self.obj_login.input_username_password_and_username_error('xiangxiang', '123456896%%')


    def input_error_user_and_correct_password(self):
        """
        输入错误的用户名、正确的密码
        :return:
        """
        return self.obj_login.input_username_password_and_username_error('tianxiang2009', self.pass_wrod)


    def input_error_password_and_correct_username(self):
        """
        输入正确的用户名，错误密码
        :return:
        """
        return self.obj_login.input_username_password_and_username_error(self.username, '123456789x%')

    def input_current_password_and_username(self):
        """
        输入正确的用户名和密码登录成功
        """
        return self.obj_login.input_username_password_and_username(self.username, self.pass_wrod)

    def quit_browser(self):
        """
        关闭浏览器
        :return:
        """
        self.obj_login.quit_browser()


if __name__ == '__main__':
    LoginHandle().input_current_password_and_username()
