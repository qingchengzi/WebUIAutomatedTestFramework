#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tian'
__data__ = '2021/3/4 11:17'

import unittest

from handled.loginhandle import LoginHandle


class Register(unittest.TestCase):
    """港湾置业后台登录测试用例集"""

    def test_01_open_login_page(self):
        """打开港湾置业后台登录页面"""
        open_title = "HARBOR PROPERTY MANAGEMENT SYSTEM"
        login_title = self.obj_hand.open_admin_page()
        self.assertEqual(login_title, open_title)

    @StopIteration
    def test_02_username_password_all_null(self):
        """用户名和密码都为空"""
        raw_text = "请输入账号"
        rest_text = self.obj_hand.user_and_password_null()
        self.assertEqual(rest_text, raw_text)

    @StopIteration
    def test_03_username_password_input_error(self):
        """输入错误的用户名和密码"""
        raw_text = "用户名或密码错误"
        rest_user = self.obj_hand.user_and_password_error()
        self.assertEqual(rest_user, raw_text)

    @StopIteration
    def test_04_input_error_username_correct_password(self):
        """输入错误的用户名，正确密码"""
        raw_text = "用户名或密码错误"
        rest_user = self.obj_hand.input_error_user_and_correct_password()
        self.assertEqual(rest_user, raw_text)

    @StopIteration
    def test_05_input_correct_username_error_password(self):
        """输入正确的用户名，错误的密码"""
        raw_text = "用户名或密码错误"
        rest_user = self.obj_hand.input_error_password_and_correct_username()
        self.assertEqual(rest_user, raw_text)

    def test_06_input_correct_username_password(self):
        """输入正确的用户名和密码登录成功"""
        raw_text = "tianx"
        rest_user = self.obj_hand.input_current_password_and_username()
        self.assertEqual(rest_user, raw_text)

    @classmethod
    def setUpClass(cls):
        """登录页面测试用例执行之前初始化操作"""
        cls.obj_hand = LoginHandle()

    @classmethod
    def tearDownClass(cls):
        """登录页面所有用例执行完毕后操作"""
        cls.obj_hand.quit_browser()
