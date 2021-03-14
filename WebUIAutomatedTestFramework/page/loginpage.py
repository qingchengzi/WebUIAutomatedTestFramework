#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tian'
__data__ = '2021/3/4 11:36'

import time

from base.base_page import BasePage
from config import setting

"""
将登录页面的定位元素，传入到BasePage类中进行定位及获取driver操作
"""


class LoginPage(BasePage):
    """
    后台登录页面元素定位操作
    """

    def open_admin_page(self):
        """
        打开Fdd后台，返回页面title
        :return:
        """
        try:
            self.navigate(self.url, path=setting.COMMON_PARAMETERS.get("log_pag_path"))
            self.screen_shot(type_str="进入后台登录页面", path="//button[@id='login_submit']")  # 截图功能
        except Exception as error:
            self.obj_com.write_error_log("{0}{1}".format("直接点击登录按钮错误:", error))
            self.screen_shot(error_type=True)
        return self.print_current_title()

    def user_and_password_all_null(self):
        """
         登录页面什么都不输入直接点击登录
        :return:
        """
        try:
            self.by_css("#login_submit").click()
            self.default_stop_time()
        except Exception as error:
            self.obj_com.write_error_log("{0}{1}".format("直接点击登录按钮错误:", error))
            self.screen_shot(error_type=True)
        return self.by_xpath("//ul[@id='parsley-id-5']//li[@class='parsley-required']").text.strip()

    def input_username_password_and_username_error(self, username, password):
        """
        输入错误的用户名和密码登录失败
        :return:
        """
        try:
            self.default_stop_time()
            self.by_xpath("//input[@placeholder='账号']").clear()
            self.by_xpath("//input[@placeholder='账号']").send_keys(username)
            self.default_stop_time()
            self.by_xpath("//input[@placeholder='密码']").clear()
            self.by_xpath("//input[@placeholder='密码']").send_keys(password)
            self.default_stop_time()
            self.by_css("#login_submit").click()
            self.default_stop_time()
            text = self.by_xpath("/html/body/div[3]/div/div/div[2]").text
            self.by_xpath("//button[@class='close j_close']").click()
        except Exception as error:
            self.obj_com.write_error_log("{0}{1}".format("登录后台输入无效账号和密码出错:", error))
            self.screen_shot(error_type=True)
        else:
            return text

    def input_username_password_and_username(self, username, password):
        """
        输入正确的用户名和密码登录成功
        :return:
        """
        try:
            self.default_stop_time()
            self.by_xpath("//input[@placeholder='账号']").clear()
            self.by_xpath("//input[@placeholder='账号']").send_keys(username)
            self.default_stop_time()
            self.by_xpath("//input[@placeholder='密码']").clear()
            self.by_xpath("//input[@placeholder='密码']").send_keys(password)
            self.default_stop_time()
            self.by_css("#login_submit").click()  # 点击登录
            self.default_stop_time()
        except Exception as error:
            self.obj_com.write_error_log("{0}{1}".format("登录后台错误:", error))
            self.screen_shot(error_type=True)
        else:
            self.screen_shot(type_str="后台登录成功")  # 后台登录成功后进行截图
            return self.by_xpath("//h2[contains(text(),'tianx')]").text.strip()

    def quit_browser(self):
        """
        :return:
        """
        self.close_browser()

    @property
    def check_write_log(self):
        """
        调试成功截图和失败截图
        :return:
        """
        print("进入啊啊")
        try:
            a = 1 + "5"
            print("注册")
        except Exception as error:
            print(error)
            self.obj_com.write_error_log("{0}{1}".format("直接点击登录按钮错误:", error))
            self.screen_shot(type_str="后台登录成功")


if __name__ == '__main__':
    obj = LoginPage()
    obj.check_write_log
