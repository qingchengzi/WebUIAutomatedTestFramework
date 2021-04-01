#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： 青城子
# datetime： 2021/3/28 16:55 
# ide： PyCharm

import time

from page.base import BasePage


class LoginPage(BasePage):

    def ledger_input(self, *args):
        rest_text = None
        try:
            for i in args[0]:
                self.by_xpath("//input[@placeholder='账号']").clear()
                self.default_time()
                self.by_xpath("//input[@placeholder='账号']").send_keys(i.get("username"))
                self.default_time()
                self.by_xpath("//input[@placeholder='密码']").clear()
                self.by_xpath("//input[@placeholder='密码']").send_keys(i.get("password"))
                self.default_time()
                self.by_css("#login_submit").click()
                self.default_time()
                rest_text = self.by_xpath("/html/body/div[3]/div/div/div[2]").text
                self.by_xpath("//button[@class='close j_close']").click()
        except Exception as error:
            print("错误的error", error)
            self.screen_shot(error_type=True)
            self.log_obj().info("登录异常测试用例执行错误:{0}".format(error))
            return "登录功能异常用例失败"
        return rest_text

    def login_successfully(self):
        try:
            self.by_xpath("//input[@placeholder='账号']").clear()
            self.default_time()
            self.by_xpath("//input[@placeholder='账号']").send_keys(self.username)
            self.default_time()
            self.by_xpath("//input[@placeholder='密码']").clear()
            self.by_xpath("//input[@placeholder='密码']").send_keys(self.pwd)
            self.default_time()
            self.by_css("#login_submit").click()
            time.sleep(5)
        except Exception as error:
            print("错误的error", error)
            self.screen_shot(error_type=True)
            self.log_obj().info("登录失败:{0}".format(error))
            return "登录失败"
        else:
            self.screen_shot(type_str="登录成功")
            return self.by_xpath("//h2[contains(text(),'tianx')]").text.strip()

    def click_login(self):
        """
        什么都不输入直接点击登录
        :return:
        """
        self.by_css("#login_submit").click()
        self.default_time()
        rest_text = self.by_xpath("//ul[@id='parsley-id-5']//li[@class='parsley-required']").text.strip()
        self.default_time()
        return rest_text

