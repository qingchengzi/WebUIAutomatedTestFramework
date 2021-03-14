#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tian'
__data__ = '2021/3/4 13:58'

import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select  # 下拉菜单
from selenium.webdriver import ActionChains  # 鼠标事件

from config import setting
from util.common_class import PublicTools


class BasePage:
    """
    元素定位基类
    """

    def __init__(self):
        self.obj_com = PublicTools()  # 公共类，写入日志，截图方法等
        self.url = setting.COMMON_PARAMETERS.get("url")
        self.if_headers_browser = setting.HEADLESS_BROWSER  # 谷歌无头和phantomjs选择
        self.img_time = time.strftime("%Y-%m-%d %H_%M_%S")  # 生成截图图片时间
        self.directory_time = time.strftime("%Y-%m-%d")  # 当日截图目录名称
        self.root_directory = setting.BASE_DIR  # 根目录
        self.screen_directory = setting.SCREENS_PATH  # 截图目录
        self.driver = self.get_driver()

    def get_driver(self):
        """
        获取浏览器的driver
        :return:
        """
        if setting.INTERFACE:
            driver = self.headless_browser()
        else:
            driver = self.open_browser()
        return driver

    def headless_browser(self):
        """
        无头浏览器，默认为谷歌无头浏览器
        :return:
        """
        if self.if_headers_browser:  # 谷歌无头浏览器
            ch_options = Options()
            ch_options.add_argument("--headless")  # 添加无头参数
            ch_options.add_argument("--disable-gpu")  # 添加无头参数
            driver = webdriver.Chrome(options=ch_options)
            driver.implicitly_wait(10)
            driver.maximize_window()
            return driver
        else:  # phantomjs无头浏览器
            ph_driver = webdriver.PhantomJS(executable_path=r"C:\Python37\phantomjs.exe")
            ph_driver.maximize_window()
            ph_driver.implicitly_wait(10)
            return ph_driver

    def open_browser(self):
        """
        有界面浏览器
        :return:
        """
        chrome_driver = webdriver.Chrome()
        chrome_driver.maximize_window()
        chrome_driver.implicitly_wait(10)
        return chrome_driver

    def navigate(self, url=None, path=None):
        """
         ui打开web页面
        :param url:
        :param path:
        :return:
        """
        if url and path:
            url = "{0}{1}".format(url, path)
            self.driver.get(url)
        elif url:
            self.driver.get(url)
        else:
            self.driver.get(self.url)

    def wait_for(self):
        self.driver.implicitly_wait(setting.SCREENS_PATH)

    def print_current_title(self):
        """
        获取当前页面的title
        :return: title
        """
        return self.driver.title

    def print_current_url(self):
        """
        获取当前的url
        :return: url
        """
        return self.driver.current_url

    def get_cookie(self):
        """
        获取cookies
        :return:
        """
        return self.driver.get_cookies()

    def add_cookie(self, cookies=None, url=None):
        """
        指url中添加cookies
        :param cookies:
        :param url:
        :return:
        """
        self.driver.get(url)
        self.driver.add_cookie(cookie_dict=cookies)

    def close_browser(self):
        """
        关闭浏览器
        :return:
        """
        self.driver.quit()

    def get_window_size(self):
        """
        获取浏览器页面的高宽
        :return:
        """
        return self.driver.get_window_size()

    def scrollbar_bottom(self):
        """
        浏览器下拉到最底部
        :return:
        """
        element = self.by_tag_name("body")
        self.driver.execute_script("arguments[0].scrollIntoView(false);", element)

    def scrollbar_top(self):
        """
        浏览器纵向滚动条拉会到最顶部
        :return:
        """
        element = self.by_tag_name("body")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def scrollbar_custom(self, height_size=550):
        """
        自定义纵向浏览器滚动条高度，默认下拉到高度550的位置
        :param height_size:
        :return:
        """
        js = "var q=document.documentElement.scrollTop={0}".format(height_size)
        self.driver.execute_script(js)

    def horizontal_scroll_bar(self):
        """
        浏览器横向滚动条操作
        :return:
        """
        window_size = self.driver.get_window_size()  # 获取当前浏览器打开页面的宽高
        width = window_size.get('width')
        js = "window.scrollTo({0},0);".format(width)  # 0横向距离，纵向距离(一般默认0)
        self.driver.execute_script(js)

    def by_css(self, *args, **kwargs):
        """
        css定位
        :param args:
        :param kwargs:
        :return:
        """
        return self.driver.find_element_by_css_selector(args[0])

    def bys_css_plural(self, *args, **kwargs):
        """
        css复数定位
        :param args:
        :param kwargs:
        :return:
        """
        return self.driver.find_elements_by_css_selector(args[0])

    def by_xpath(self, *args, **kwargs):
        """
         xpath定位
        :param args:
        :param kwargs:
        :return:
        """
        return self.driver.find_element_by_xpath(args[0])

    def bys_xpath_plural(self, *args, **kwargs):
        """
        xpath复数定位
        :param args:
        :param kwargs:
        :return:
        """
        return self.driver.find_elements_by_xpath(args[0])

    def by_tag_name(self, *args, **kwargs):
        """
        tag定位
        :param args:
        :param kwargs:
        :return:
        """
        return self.driver.find_element_by_tag_name(args[0])

    def bys_tag_plural(self, *args, **kwargs):
        """
        tag复数定位
        :param args:
        :param kwargs:
        :return:
        """
        return self.driver.find_elements_by_tag_name(args[0])

    def by_id(self, *args, **kwargs):
        """
        id定位
        :param args:
        :param kwargs:
        :return:
        """
        return self.driver.find_element_by_id(args[0])

    def bys_id_plural(self, *args, **kwargs):
        """
        id复数定位
        :param args:
        :param kwargs:
        :return:
        """
        return self.driver.find_elements_by_id(args[0])

    def by_frame(self, *args, **kwargs):
        """
        切换到frame框架中
        :param args:
        :param kwargs:
        :return:
        """
        return self.driver.switch_to_frame(args[0])

    def by_quit_frame(self, *args, **kwargs):
        """
        退出frame
        :param args:
        :param kwargs:
        :return:
        """
        return self.driver.switch_to.default_content()

    def print_window_handles(self):
        """
        窗口中所有的标签列表
        :return:
        """
        return self.driver.window_handles

    def switch_to_window_handles(self, index=0):
        """
        在浏览器中打开多个选项卡时，切换浏览器选项卡的handles
        :param index:
        :return:
        """
        return self.driver.switch_to_window(self.driver.window_handles[index])

    def textbox(self, *args, **kwargs):
        """
        文本框输入内容
        :param args:
        :param kwargs:
        :return:
        """
        js = " var sum=document.getElementById({0});sum.value={1}".format(args[0], args[1])
        self.driver.execute_script(js)

    def create_screens_hot_directory(self, *args, **kwargs):
        """
        创建截图需要的目录
        :return:
        """
        # 创建截图首层目录
        try:
            if os.path.exists(self.screen_directory):  # 判断保存截图的目录screenshot是否存在
                pass
            else:  # 截图目录不存在，就创建screenshot目录
                os.mkdir("{0}".format(self.screen_directory))
        except Exception as er:
            error_str = "{0}:{1}".format("进入截图目录失败", er)
            self.obj_com.write_error_log(error_str)

        dir_path = "{0}".format(self.screen_directory)

        # 创建截图二级目录
        try:
            if os.path.exists("{0}\{1}".format(dir_path, self.directory_time)):
                """
                判断screenshot目录下是否存在(2020-04-15)格式命名的目录
                """
                pass
            else:  # 如果没有就创建二级目录
                os.mkdir("{0}\{1}".format(dir_path, self.directory_time))
        except Exception as er:
            error_str = "{0}:{1}".format("进入每日截图目录失败", er)
            self.obj_com.write_error_log(error_str)

        # 创建三级存放成功时截图的目录
        try:
            if os.path.exists("{0}\{1}\{2}".format(dir_path, self.directory_time, 'success')):
                pass
            else:
                os.makedirs("{0}\{1}\{2}".format(dir_path, self.directory_time, 'success'))
        except Exception as er:
            error_str = "{0}{1}".format("进入每日成功截图目录失败", er)
            self.obj_com.write_error_log(error_str)

        direct_success = "{0}\{1}\{2}".format(dir_path, self.directory_time, 'success')

        # 创建三级存放失败时截图的目录
        if args[0]:
            try:
                if os.path.exists("{0}\{1}\{2}".format(dir_path, self.directory_time, 'errordir')):
                    pass
                else:
                    os.mkdir("{0}\{1}\{2}".format(dir_path, self.directory_time, 'errordir'))
            except Exception as er:
                error_str = "{0}:{1}".format("进入每日错误目录失败", er)
                self.obj_com.write_error_log(error_str)
        direct_error = "{0}\{1}\{2}".format(dir_path, self.directory_time, 'errordir')
        return direct_success, direct_error

    def screen_shot(self, type_str=None, path=None, error_type=None):
        """
        截图功能
        :param type_str:
        :param path:
        :param error_type:
        :return:
        """
        direct_success, direct_error = self.create_screens_hot_directory(error_type)
        # 用例执行成功时页面的截图
        if type_str:
            image_page = "{0}\{1}{2}.png".format(direct_success, type_str, self.img_time)
        else:
            image_page = "{0}\{1}.png".format(direct_success, self.img_time)

        if path:  # 根据path判断截取指定区域的截图还是可见区域的截图
            erwima = self.by_xpath(path)
            erwima.screenshot(image_page)  # 截取指定区域的图
        elif not error_type:
            self.driver.save_screenshot(image_page)  # 截取可见区域的图

        if error_type:
            # 代码执行错误时，进行截图
            image_page_error = "{0}\{1}.png".format(direct_error, self.img_time)
            self.driver.save_screenshot(image_page_error)

    def by_select_menu_index(self, *args):
        """
        select下拉菜单,必须使用xpath定位,通过索引定位
        :param args:
        :return:
        """
        Select(self.driver.find_element_by_xpath(args[0])).select_by_index(args[1])

    def by_select_menu_value(self, *args):
        """
        select下拉菜单,必须使用xpath定位,通过索引定位
        :param args:
        :return:
        """
        Select(self.driver.find_element_by_xpath(args[0])).select_by_value(str(args[1]))

    def default_stop_time(self):
        """
        默认time.sleep()暂停3秒
        :return:
        """
        time.sleep(setting.STOP_TIME)

    def is_element_exist(self, *args, aligntype=1):
        """
        find_elements_by_xpath找不到定位元素会返回空列表
        :param args: 定位元素
        :param aligntype: 默认xpath定位
        :return:
        """
        if aligntype == 1:
            s = self.driver.find_elements_by_xpath(args[0])
            if len(s) == 0:
                return False
            elif len(s) == 1:
                return True
            else:
                return True
        else:
            s = self.driver.find_elements_by_css_selector(args[0])
            if len(s) == 0:
                return False
            elif len(s) == 1:
                return True
            else:
                return True

    def mouse_left_click_double_click(self, *args, **kwargs):
        """
        鼠标左键双击,传入参数必须为xpath定位
        :param args:
        :param kwargs:
        :return:
        """
        elements = self.by_xpath(args[0])
        ActionChains(self.driver).double_click(elements).perform()

    def mouse_right_click(self, *args, **kwargs):
        """
        鼠标右击点击
        :param args:
        :param kwargs:
        :return:
        """
        elements = self.by_xpath(args[0])
        ActionChains(self.driver).context_click(elements).perform()

    def mouse_suspended(self, *args, **kwargs):
        """
        鼠标悬浮
        :param args:
        :param kwargs:
        :return:
        """
        elements = self.by_xpath(args[0])
        ActionChains(self.driver).move_to_element(elements).perform()

    def mouse_to_drag_and_drop(self, *args, **kwargs):
        """
        鼠标拖拽
        :param args:
        :param kwargs:
        :return:
        """
        time.sleep(setting.STOP_TIME)
        self.by_xpath(args[0]).click()  # 先点击
        start = self.by_tag_name(args[1])  # 拖拽开始
        end = self.by_tag_name(args[2])  # 拖拽结束
        ActionChains(self.driver).drag_and_drop(start, end).perform()
