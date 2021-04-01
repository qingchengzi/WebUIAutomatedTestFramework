#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： 青城子
# datetime： 2021/3/28 13:04 
# ide： PyCharm

import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select  # 下拉菜单
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains  # 鼠标事件

from config import settings

from util.common_module import PublicTools
from util.LogHandler import logger


class BasePage:
    """
    基础Page层，封装一些常用方法
    """

    def __init__(self):
        self.obj_com = PublicTools()
        self.driver = self.get_driver()
        self.log_obj = logger
        # 生成截图图片时间
        self.img_time = time.strftime("%Y-%m-%d %H_%M_%S")
        self.url = settings.URL
        self.username = settings.USERNAME
        self.pwd = settings.PASSWORD

    def get_driver(self):
        """
        获取浏览器的driver
        :return:
        """
        if settings.INTERFACE:
            driver = self.open_browser()
        else:
            driver = self.headless_browser()
        return driver

    def headless_browser(self):
        """
        无头浏览器，默认为谷歌无头浏览器
        :return:
        """
        if settings.HEADLESS_BROWSER:  # 谷歌无头浏览器
            ch_options = Options()
            ch_options.add_argument("--headless")  # 添加无头参数
            ch_options.add_argument("--disable-gpu")  # 添加无头参数
            driver = webdriver.Chrome(options=ch_options)
            driver.implicitly_wait(10)
            # driver.maximize_window() # 对谷歌浏览器无效
            driver.set_window_size(settings.WIDTH, settings.HEIGHT)
            return driver
        else:  # phantomjs无头浏览器
            ph_driver = webdriver.PhantomJS(executable_path=r"C:\Python\Python37\Scripts\phantomjs\bin\phantomjs.exe")
            ph_driver.maximize_window()  # 浏览器最大化
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

    def open_page(self, url=None):
        if url is None:
            self.driver.get(self.url)
        else:
            self.driver.get(url)

    def get_title(self):
        """
        获取title
        :return:
        """
        return self.driver.title

    def get_current_url(self):
        """
        获取当前windows的url
        :return:
        """
        return self.driver.current_url

    def get_window_size(self):
        """
        获取浏览器页面的高宽
        :return:
        """
        return self.driver.get_window_size()

    def get_cookie(self):
        """
        获取cookies
        :return:
        """
        return self.driver.get_cookies()

    def get_current_windows_handle(self):
        """
        获取当前窗口对象
        :return:
        """
        return self.driver.current_window_handle

    def add_cookie(self, cookies=None, url=None):
        """
        指url中添加cookies
        :param cookies:
        :param url:
        :return:
        """
        self.driver.get(url)
        self.driver.add_cookie(cookie_dict=cookies)

    def refresh(self):
        """
        刷新页面
        :return:
        """
        self.driver.refresh()

    def quit_browser(self):
        """
        关闭浏览器
        :return:
        """
        self.driver.quit()

    def by_id(self, id_):
        """
        id定位
        :param id_:
        :return:
        """
        return self.driver.find_element_by_id(id_)

    def bys_id_plural(self, *args):
        """
        id复数定位
        :param args:
        :return:
        """
        return self.driver.find_elements_by_id(args[0])

    def by_css(self, css_):
        """
        css定位
        :param css_:
        :return:
        """
        return self.driver.find_element_by_css_selector(css_)

    def by_css_plural(self, *args):
        """
        css复数定位
        :param args:
        :return:
        """
        return self.driver.find_elements_by_css_selector(args[0])

    def by_name(self, *args):
        """
        name定位
        :param args:
        :return:
        """
        return self.driver.find_element_by_name(args[0])

    def by_name_plural(self, *args):
        """
        name复数定位
        :param args:
        :return:
        """
        return self.driver.find_elements_by_name(args[0])

    def by_tag_name(self, tag_):
        """
        tag定位
        :param tag_:
        :return:
        """
        return self.driver.find_element_by_tag_name(tag_)

    def bys_tag_plural(self, tag_):
        """
        tag复数定位
        :param tag_:
        :return:
        """
        return self.driver.find_elements_by_tag_name(tag_)

    def by_class_name(self, class_):
        """
        cass定位
        :return:
        """
        return self.driver.find_element_by_class_name(class_)

    def by_class_name_plural(self, class_):
        """
        cass定位
        :return:
        """
        return self.driver.find_elements_by_class_name(class_)

    def by_link_text(self, text_):
        """
        link定位
        :param text_:
        :return:
        """
        self.driver.find_element_by_link_text(text_)

    def by_partial_link_text(self, text_):
        """
        文本链接长时使用，模糊link定位
        :param text_:
        :return:
        """
        self.driver.find_element_by_partial_link_text(text_)

    def by_xpath(self, xpath_):
        """
        xpath定位
        :param xpath_:
        :return:
        """
        return self.driver.find_element_by_xpath(xpath_)

    def bys_xpath_plural(self, xpath_):
        """
        xpath复数定位
        :return:
        """
        return self.driver.find_elements_by_xpath(xpath_)

    def get_attribute(self, *args):
        """
        获取标签中的属性值
        :param args:args[0]需要获取标签的xpath定位，args[1]需要获取属性的name例如：value=1 就是value
        :return:返回获取定位标签中，指定属性name的值。
        """
        obj_element = self.by_xpath(args[0])
        return obj_element.get_attribute(args[1])

    def by_frame(self, *args):
        """
        切换到frame框架中
        :param args:
        :return:
        """
        return self.driver.switch_to_frame(args[0])

    def by_quit_frame(self):
        """
        退出frame
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

    def textbox(self, *args):
        """
        文本框输入内容
        :param args:
        :return:
        """
        js = " var sum=document.getElementById({0});sum.value={1}".format(args[0], args[1])
        self.driver.execute_script(js)

    def default_time(self):
        """
        默认time.sleep()暂停3秒
        :return:
        """
        time.sleep(settings.STOP_TIME)

    def by_select_menu_value(self, *args):
        """
        select下拉菜单,Select()参数为select标签的定位对象,通过value属性来定位
        :param args:args[0]select标签的xpath定位，arg[1]通过value值定位下拉选项
        :return:
        """
        obj_select = self.by_xpath(args[0])
        Select(obj_select).select_by_value(str(args[1]))

    def by_select_menu_index(self, *args):
        """
        select下拉菜单,必须使用xpath定位,通过索引定位
        :param args:
        :return:
        """
        Select(self.driver.find_element_by_xpath(args[0])).select_by_index(args[1])

    def mouse_left_click_double_click(self, *args):
        """
        鼠标左键双击,传入参数必须为xpath定位
        :param args:
        :return:
        """
        elements = self.by_xpath(args[0])
        ActionChains(self.driver).double_click(elements).perform()

    def mouse_right_click(self, *args):
        """
        鼠标右击点击
        :param args:
        :return:
        """
        elements = self.by_xpath(args[0])
        ActionChains(self.driver).context_click(elements).perform()

    def mouse_suspended(self, *args):
        """
        鼠标悬浮
        :param args:
        :return:
        """
        elements = self.by_xpath(args[0])
        ActionChains(self.driver).move_to_element(elements).perform()

    def mouse_to_drag_and_drop(self, *args):
        """
        鼠标拖拽
        :param args:
        :return:
        """
        time.sleep(settings.STOP_TIME)
        self.by_xpath(args[0]).click()  # 先点击
        start = self.by_tag_name(args[1])  # 拖拽开始
        end = self.by_tag_name(args[2])  # 拖拽结束
        ActionChains(self.driver).drag_and_drop(start, end).perform()

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

    def scrollbar_top(self):
        """
        浏览器纵向滚动条拉会到最顶部
        :return:
        """
        element = self.by_tag_name("body")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def scrollbar_bottom(self):
        """
        浏览器下拉到最底部
        :return:
        """
        element = self.by_tag_name("body")
        self.driver.execute_script("arguments[0].scrollIntoView(false);", element)

    def screen_shot(self, type_str=None, path=None, error_type=None):
        """
        截图功能
        :param type_str:
        :param path:
        :param error_type:
        :return:
        """
        direct_success, direct_error = self.obj_com.create_screen_catalog()
        # 用例执行成功时页面的截图
        if type_str:
            image_page = r"{0}\{1}{2}.png".format(direct_success, type_str, self.img_time)
            # 判断截取指定区域的图片，还是可见区域的图片
            if path:
                # 截取指定区域的图片
                designated_area = self.by_xpath(path)
                designated_area.screenshot(image_page)
            else:
                # 截取可见区域的图片
                self.driver.save_screenshot(image_page)

        if error_type:
            # 代码执行错误时，进行截图
            image_page_error = r"{0}\{1}.png".format(direct_error, self.img_time)
            self.driver.save_screenshot(image_page_error)
