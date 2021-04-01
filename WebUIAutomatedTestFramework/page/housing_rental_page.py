#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： 青城子
# datetime： 2021/3/28 23:27 
# ide： PyCharm

import time
import random

from config import settings
from page.base import BasePage


class HousingPage(BasePage):
    """
    房源租售管理页面
    """

    def __init__(self):
        super().__init__()
        # 房源类型
        self.housing_type = [1, 2, 3, 9]
        # 获取标题
        self.title_text = self.obj_com.get_date()
        # 房源描述
        self.describe = self.obj_com.get_date(text_type=2)
        # 房源金额
        money = settings.PROPERTY_PARAMETERS.get("money")
        self.money = money[random.randrange(0, len(money))]
        # 房源面积
        area = settings.PROPERTY_PARAMETERS.get("area")
        self.area = area[random.randrange(0, len(area))]
        # 房源图片
        self.img_list = self.obj_com.get_image()
        # 区域
        self.city_list = settings.PROPERTY_PARAMETERS.get("city_type")  # 城市
        self.random_city = self.city_list[random.randrange(len(self.city_list))]

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
            print("进入房源页面错误:{0}".format(error))
            self.screen_shot(error_type=True)
            self.log_obj().info("进入房源页面错误:{0}".format(error))
        else:
            self.screen_shot(type_str="房源租售登录成功")

    def residential_rental(self):
        """
        进入房源租售管理，住宅出租页面
        :return:
        """
        try:
            self.by_xpath('//*[@id="sidebar-menu"]/div/ul/li[1]/a').click()  # 点击房源租售管理
            self.default_time()
            self.by_xpath('//*[@id="sidebar-menu"]/div/ul/li[1]/ul/li[3]/a').click()  # 点击住宅出租  # 点击住宅出租
            self.default_time()
            self.screen_shot(type_str="进入住宅出租页面")  # 截图功能
            time.sleep(5)
        except Exception as error:
            print("进入住宅出租页面报错:{0}".format(error))
            self.screen_shot(error_type=True)
            self.log_obj().info("进入住宅出租页面报错:{0}".format(error))
            return "进入住宅出租页面错误"
        else:
            return self.get_title()

    def the_new_housing(self):
        """
        新增住宅出租房源
        :return:
        """
        try:
            # 点击添加房源按钮
            self.by_xpath('//*[@id="j-search-form"]/div[10]/button[2]').click()
            time.sleep(10)
            # 选择发布语言//*[@id="sl_lang_chosen"]/ul/li/input
            self.by_xpath('//*[@id="sl_lang_chosen"]/ul/li/input').click()
            self.default_time()
            # 选择中文
            self.by_xpath('//*[@id="sl_lang_chosen"]/div/ul/li[1]').click()
            # 再次点击选择发布语言文本框
            self.by_xpath('//*[@id="sl_lang_chosen"]/ul/li/input').click()
            self.default_time()
            # 选择英文
            self.by_xpath('//*[@id="sl_lang_chosen"]/div/ul/li[2]').click()
            self.default_time()
            # 选择基础语言(中文)
            self.by_select_menu_value('//*[@id="sl_baselang"]', "zh-cn")
            self.default_time()
            # 随机选择发布房源类型
            self.by_select_menu_value('//*[@id="BuildingTypeId"]', random.sample(self.housing_type, k=1)[0])
            self.default_time()
            # 输入房源标题
            self.by_xpath('//*[@id="TitleCn"]').send_keys(self.title_text)
            # 输入房源描述
            self.default_time()
            self.by_xpath('//*[@id="IntrCn"]').send_keys(self.describe)
            self.default_time()
            # 选择发布人
            self.by_xpath('//*[@id="j-update-form"]/div[2]/div[10]/div[1]/div/a').click()
            self.default_time()
            # 随机选择发布人
            obj_checkbox = self.bys_xpath_plural('//*[@id="agent_check_table"]/div[1]/table/tbody/tr/td[1]/input')
            obj_checkbox[random.randrange(len(obj_checkbox))].click()
            self.default_time()
            self.by_xpath('/html/body/div[3]/div/div/div[3]/button[2]').click()
            # 滚动条下拉当前浏览器1/3的位置
            self.default_time()
            windows_size = self.get_window_size()
            width = windows_size.get("width")
            self.scrollbar_custom(int(width / 3))
            self.default_time()
            # 选择房源图片
            for i in range(len(self.img_list)):
                self.default_time()
                self.by_xpath('//*[@id="rhouse_imgurl"]/input').send_keys(self.img_list[i])
            self.default_time()
            self.by_select_menu_value('//*[@id="RegionId"]', self.random_city)
            self.default_time()
            # self.scrollbar_custom(height_size=350)
            # self.default_time()
            self.by_xpath('//*[@id="Price"]').send_keys(self.money)
            self.default_time()
            self.by_xpath('//*[@id="Area"]').send_keys(self.area)
            # 滚动条下拉到底部
            self.default_time()
            self.scrollbar_custom(height_size=int(width))
            self.default_time()
            self.by_xpath("//button[@id='btn_save']").click()
            time.sleep(10)
        except Exception as error:
            print("添加房源错误:{0}".format(error))
            self.log_obj().info("新增房源错误:{0}".format(error))
            return "添加房源失败"
        else:
            self.screen_shot(type_str="添加房源成功")
            return "添加房源成功"
