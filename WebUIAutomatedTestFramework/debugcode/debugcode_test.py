#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tian'
__data__ = '2021/3/4 10:13'

import unittest


class TestStringMethods(unittest.TestCase):
    """
    调试框架流程是否正常的类
    """
    def test_lower(self):
        """
        判断foo.lower()是否等于FOO
        :return:
        """
        self.assertEqual("foo".lower(),"FOO")

    def test_islower(self):
        """
        判断foo是否小写
        :return:
        """
        self.assertTrue("foo".islower())