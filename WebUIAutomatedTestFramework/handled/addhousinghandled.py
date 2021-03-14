#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tian'
__data__ = '2020/4/13 12:20'

from page.housing_rental_page import HousingPage
from config import setting


class HousingHandled:
    """
    房源租售管理页面的操作
    """

    def __init__(self):
        self.obj = HousingPage()
        self.obj.open_admin_page()
        self.obj.log_background()

    def residential_rental(self):
        return self.obj.ResidentialRental()

    def screening_of_city(self):
        """
        筛选城市
        :return:
        """
        flage, city_name, random_city = self.obj.screening_of_city_page()
        random_city = setting.PROPERTY_PARAMETERS.get("locations").get(random_city)
        if flage:
            return "正常"
        else:
            if city_name == random_city:
                return "正常"

    def the_new_housing(self):
        """
        新增住宅出租房源
        :return:
        """
        return self.obj.add_housing()

    def quit_browser(self):
        self.obj.quit_close_browser()
