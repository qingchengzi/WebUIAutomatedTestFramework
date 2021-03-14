#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tian'
__data__ = '2021/3/1 17:45'

import unittest

from selenium import webdriver

from HTMLTestRunner3_selenium import HTMLTestRunner


class myTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.PhantomJS(executable_path=r"C:\Python37\phantomjs.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_case_01(self):
        title = self.driver.title
        print("打印了")
        self.assertEqual(title, "百度一下，你就知道")

    def test_case_02(self):
        title = self.driver.title
        print("打印了阿22")
        self.assertEqual(title, "百度一下， 我还是不晓得")

    def setUp(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    suite = unittest.makeSuite(testCaseClass=myTestCase)
    with open("report.html", "wb") as f:
        HTMLTestRunner(
                stream=f,
                tester="tian",
                title="selenium测试报告",
                verbosity=2  # 更详细和直观打印用例名称和执行结果

        ).run(suite)
