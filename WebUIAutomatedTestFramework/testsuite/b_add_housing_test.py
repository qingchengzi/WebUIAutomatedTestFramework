#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： 青城子
# datetime： 2021/3/28 23:19 
# ide： PyCharm

"""
进入后台-->房源租售管理中添加房源等功能
"""

import unittest
from selenium import webdriver

from page import housing_rental_page

com_list = []


def setUpModule():
    obj_page = housing_rental_page.HousingPage()
    obj_page.open_page()
    # 登录进入后台
    obj_page.login_successfully()
    com_list.append(obj_page.driver)
    com_list.append(obj_page)


def tearDownModule():
    com_list[0].quit()


class AddHousing(unittest.TestCase):
    """房源租售管理中添加房源"""

    @classmethod
    def setUpClass(cls):
        cls.obj_driver = com_list[0]
        cls.obj_page = com_list[1]

    def test_01_a_residential_rental(self):
        """进入住宅出租页面"""
        raw_text = "住宅出租"
        rest = self.obj_page.residential_rental()
        self.assertEqual(rest, raw_text)

    def test_02_b_add_housing(self):
        """添加住宅出租房源"""
        raw_text = "添加房源成功"
        rest = self.obj_page.the_new_housing()
        self.assertEqual(raw_text, rest)

