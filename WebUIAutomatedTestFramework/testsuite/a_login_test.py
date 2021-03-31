#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： 青城子
# datetime： 2021/3/28 16:49 
# ide： PyCharm


import unittest
import ddt

from selenium import webdriver
from page import login_page

user_list = (
    {"case1": "输入错误用户名和密码", "username": "admin33", "password": "12345689x", "rest": "用户名或密码错误"},
    {"case2": "输入正确用户名，错误密码", "username": "tianx", "password": "123456999x", "rest": "用户名或密码错误"},
    {"case3": "输入错误的用户名，正确密码", "username": "tianx", "password": "123456999x", "rest": "用户名或密码错误"},
)


@ddt.ddt
class Register(unittest.TestCase):
    """后台登录测试用例集"""

    @classmethod
    def setUpClass(cls):
        cls.obj_page = login_page.LoginPage()
        cls.obj_page.open_page()

    @classmethod
    def tearDownClass(cls):
        """登录页面所有用例执行完毕后操作"""
        cls.obj_page.quit_browser()

    def test_01_open_login_page(self):
        """打开港湾置业后台登录页面"""
        open_title = "HARBOR PROPERTY MANAGEMENT SYSTEM"
        self.assertEqual(self.obj_page.get_title(), open_title)

    @StopIteration
    @ddt.data(user_list)
    def test02_input_error_username_and_pwd(self, item):
        """登录功能输入错误的用户名和密码"""
        rest_text = self.obj_page.ledger_input(item)
        self.assertEqual(rest_text, "用户名或密码错误")

    @StopIteration
    def test_03_input_all_null(self):
        """什么都不输入直接点击登录"""
        rest_text = self.obj_page.click_login()
        self.assertEqual(rest_text, "请输入账号")

    def test04_login_successfully(self):
        """登录成功"""
        rest_text = self.obj_page.login_successfully()
        self.assertEqual(rest_text, "tianx")
