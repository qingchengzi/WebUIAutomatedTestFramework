#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tian'
__data__ = '2020/4/14 9:45'

import time
import random

from base.base_page import BasePage
from config import setting


class HousingPage(BasePage):
    """
    登录后台后进入房源租售管理模块
    """

    def __init__(self):
        super(HousingPage, self).__init__()
        self.city_list = setting.PROPERTY_PARAMETERS.get("city_type")  # 城市
        self.random_city = self.city_list[random.randrange(len(self.city_list))]
        # 住宅出租房源类型
        self.housing_list = [1, 2, 3, 9]
        self.random_housing = self.housing_list[random.randrange(len(self.housing_list))]
        # 添加房源时基础语言
        self.lang_list = setting.PROPERTY_PARAMETERS.get("language")
        self.random_lang = self.lang_list[random.randrange(len(self.lang_list))]
        # 房源标题
        self.rest_title = self.obj_com.read_database()  # 获取随机标题
        # 房源租金
        price_list = ["785", "678", "578", "999", "100", "2890"]
        self.price_lang = price_list[random.randrange(len(price_list))]
        # 房源面积
        area_list = ['56', '88', '99', '50', "125", "567"]
        self.area_lang = area_list[random.randrange(len(area_list))]

    def open_admin_page(self):
        """
        打开Fdd后台，返回打开后页面title
        :return:
        """
        self.navigate(url=setting.COMMON_PARAMETERS.get("url"), path=setting.COMMON_PARAMETERS.get("log_pag_path"))

    def log_background(self):
        """
        登录后台
        :return:
        """
        try:
            user_name = setting.COMMON_PARAMETERS.get("admin")
            pass_word = setting.COMMON_PARAMETERS.get("password")
            self.default_stop_time()
            self.by_xpath("//input[@placeholder='账号']").clear()
            self.by_xpath("//input[@placeholder='账号']").send_keys(user_name)
            self.default_stop_time()
            self.by_xpath("//input[@placeholder='密码']").clear()
            self.by_xpath("//input[@placeholder='密码']").send_keys(pass_word)
            self.default_stop_time()
            self.by_xpath("//button[@id='login_submit']//span").click()
            self.default_stop_time()
        except Exception as error:
            self.obj_com.write_error_log("{0}{1}".format("登录后台错误:", error))
            self.screen_shot(error_type=True)

    def ResidentialRental(self):
        """
        进入房源租售管理，住宅出租页面
        :return:
        """
        try:
            time.sleep(10)
            self.by_xpath('//*[@id="sidebar-menu"]/div/ul/li[1]/a').click()  # 点击房源租售管理
            self.default_stop_time()
            self.by_xpath('//*[@id="sidebar-menu"]/div/ul/li[1]/ul/li[3]').click()  # 点击住宅出租  # 点击住宅出租
            time.sleep(5)
            self.screen_shot(type_str="进入住宅出租页面")  # 截图功能
            self.default_stop_time()
            return self.print_current_title()
        except Exception as error:
            self.obj_com.write_error_log("{0}{1}".format("点击住宅出租错误:", error))
            self.screen_shot(error_type=True)

    def screening_of_city_page(self):
        """
        搜索查询：条件城市选择金边、房源选择独栋别墅
        :return:
        """
        flage = False
        city_name = False
        try:
            # 随机选择金边、西哈努克、柴桢省中的一个城市
            time.sleep(10)
            # 随机选择地区
            self.by_select_menu_value('//*[@id="j-search-form"]/div[1]/select', self.random_city)
            self.default_stop_time()
            # 随机选择房源分类
            self.by_select_menu_value('//*[@id="j-search-form"]/div[2]/select', self.random_housing)
            self.default_stop_time()
            # 房源状态，默认选择已审核
            self.by_select_menu_value('//*[@id="j-search-form"]/div[3]/select', 2)
            self.default_stop_time()
            self.by_xpath('//*[@id="j-search-form"]/div[10]/button[1]').click()
            self.default_stop_time()
            # 符合搜索条件的房源和无房源的处理
            # 判断页面是否出现【没有数据】提示信息，如果有说明搜索无数据
            if self.is_element_exist('//*[@id="j-no-data-holder"]'):
                rest_text = self.by_xpath('//*[@id="j-no-data-holder"]').text
                if rest_text.strip() == "没有数据":
                    flage = True
            else:
                city_name = self.by_xpath(
                    '//*[@id="j_list"]/div/div/div/ul/li[1]/div[2]/div[4]/span[1]/span[1]').text  # 筛选成功后获取页面上的城市
        except Exception as error:
            self.obj_com.write_error_log("{0}{1}".format("筛选搜索房源错误:", error))
            self.screen_shot(error_type=True)

        return flage, city_name, self.random_city

    def add_housing(self):
        """
        新增房源
        :return:
        """
        try:
            # 添加新增房源
            self.by_xpath('//*[@id="j-search-form"]/div[10]/button[2]').click()
            self.default_stop_time()
            # 选择发布语言
            self.by_xpath('//*[@id="sl_lang_chosen"]/ul/li/input').click()
            self.default_stop_time()
            # 选择中文
            self.by_xpath('//*[@id="sl_lang_chosen"]/div/ul/li[1]').click()
            self.default_stop_time()
            self.by_select_menu_value('//*[@id="sl_baselang"]', "zh-cn")
            self.default_stop_time()
            # 选择房源类型
            housing_type = [1, 2, 3, 9]
            self.by_select_menu_value('//*[@id="BuildingTypeId"]', random.sample(housing_type, k=1)[0])
            self.default_stop_time()
            # 输入房源标题
            title_text = self.obj_com.read_database()
            self.by_xpath('//*[@id="TitleCn"]').send_keys(title_text)
            self.default_stop_time()
            # 输入房源简介
            describe = self.obj_com.read_database(text_type=2)
            self.by_xpath('//*[@id="IntrCn"]').send_keys(describe)
            self.default_stop_time()
            # 选择房源发布人
            self.by_xpath('//*[@id="j-update-form"]/div[2]/div[10]/div[1]/div/a').click()
            self.default_stop_time()
            # 发布人列表中随机选择发布人
            rest_checkbox = self.bys_xpath_plural('//*[@id="agent_check_table"]/div[1]/table/tbody/tr/td[1]/input')
            self.default_stop_time()
            rest_checkbox[random.randrange(len(rest_checkbox))].click()
            self.by_xpath('/html/body/div[3]/div/div/div[3]/button[2]').click()
            self.default_stop_time()
            # 滚动条下拉1/3的位置
            windows_size = self.get_window_size()
            width = windows_size.get("width")
            self.scrollbar_custom(int(width / 3))
            # 上传图片
            img_list = self.obj_com.get_image()
            random_img = random.sample(img_list, k=random.randrange(1, 5))
            for i in range(len(random_img)):
                self.default_stop_time()
                self.by_xpath('//*[@id="rhouse_imgurl"]/input').send_keys(random_img[i])
            self.default_stop_time()
            # 选择区域
            self.by_select_menu_value('//*[@id="RegionId"]', self.random_city)
            self.default_stop_time()
            # 滚动条下拉到底部
            self.scrollbar_custom(int(width))
            self.default_stop_time()
            self.by_xpath("//button[@id='btn_save']").click()
            time.sleep(10)
        except Exception as error:
            self.obj_com.write_error_log("{0}{1}".format("添加住宅出租房源失败:", error))
            self.screen_shot(error_type=True)
        else:
            return "添加房源成功"

    def quit_close_browser(self):
        """
        退出浏览器
        :return:
        """
        self.close_browser()
