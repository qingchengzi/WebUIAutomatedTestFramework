#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tian'
__data__ = '2020/4/13 12:06'

import unittest

from handled.addhousinghandled import HousingHandled


class AddHousing(unittest.TestCase):
    """房源租售管理中添加房源"""

    @classmethod
    def setUpClass(cls):
        """添加房源前执行"""
        cls.obj_handled = HousingHandled()

    @classmethod
    def tearDownClass(cls):
        """添加房源后执行"""
        cls.obj_handled.quit_browser()

    def test_01_a_residential_rental(self):
        """港湾置业登录后台后进入住宅出租页面"""
        raw_text = "住宅出租"
        rest = self.obj_handled.residential_rental()
        self.assertEqual(rest,raw_text)

    def test_02_b_add_housing(self):
        """添加房源"""
        raw_text = "添加房源成功"
        rest = self.obj_handled.the_new_housing()
        self.assertEqual(rest, raw_text)

    def test_03_c_screening_of_city(self):
        """住宅出租页面地区筛选查看房源"""
        raw_text = "正常"
        rest = self.obj_handled.screening_of_city()
        self.assertEqual(rest, raw_text)


if __name__ == '__main__':
    unittest.main()
