import time
import random

from selenium import webdriver
from selenium.webdriver.support.ui import Select

from util.common_class import  PublicTools

obj_com = PublicTools()

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://adm.testfdd.com/Home/Login")

driver.find_element_by_xpath("//input[@placeholder='账号']").clear()
driver.find_element_by_xpath("//input[@placeholder='账号']").send_keys("tianx")
driver.find_element_by_xpath("//input[@placeholder='密码']").clear()
driver.find_element_by_xpath("//input[@placeholder='密码']").send_keys("12345678t%")
driver.find_element_by_xpath("//*[@id='login_submit']/span").click()
time.sleep(10)
# 点击添加房源租售管理
driver.find_element_by_xpath('//*[@id="sidebar-menu"]/div/ul/li[1]/a').click()
time.sleep(10)
# 点击住宅出租
driver.find_element_by_xpath('//*[@id="sidebar-menu"]/div/ul/li[1]/ul/li[3]').click()
time.sleep(3)
# 点击新增房源
driver.find_element_by_xpath('//*[@id="j-search-form"]/div[10]/button[2]').click()
time.sleep(5)
# 选择发布语言
driver.find_element_by_xpath('//*[@id="sl_lang_chosen"]/ul/li/input').click()
time.sleep(3)
# 选择中文
driver.find_element_by_xpath('//*[@id="sl_lang_chosen"]/div/ul/li[1]').click()
time.sleep(5)
Select(driver.find_element_by_xpath('//*[@id="sl_baselang"]')).select_by_value("zh-cn")
time.sleep(5)
li = [1, 2, 3, 9]
li = li[random.randrange(1, len(li))]
Select(driver.find_element_by_xpath('//*[@id="BuildingTypeId"]')).select_by_value(str(li))
time.sleep(5)
title_text = obj_com.read_database()
# 输入标题
driver.find_element_by_xpath('//*[@id="TitleCn"]').send_keys(title_text)
time.sleep(5)
# 输入简介
describe = obj_com.read_database(text_type=2)
driver.find_element_by_xpath('//*[@id="IntrCn"]').send_keys(describe)
time.sleep(5)
driver.find_element_by_xpath('//*[@id="j-update-form"]/div[2]/div[10]/div[1]/div/a').click()
time.sleep(5)
# 选择发布人

rest_checkbox = driver.find_elements_by_xpath('//*[@id="agent_check_table"]/div[1]/table/tbody/tr/td[1]/input')
time.sleep(5)
rest_checkbox[random.randrange(len(rest_checkbox))].click()
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]').click()
time.sleep(5)
windows_size = driver.get_window_size()
width = windows_size.get('width')
js = "var q=document.documentElement.scrollTop={0}".format(int(width/3))
driver.execute_script(js)
time.sleep(5)
img_list = obj_com.get_image()
random_img = random.sample(img_list, k=random.randrange(1, 5))

for i in range(len(random_img)):
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="rhouse_imgurl"]/input').send_keys(random_img[i])
time.sleep(10)
# 选择区域
li = [1, 114, 125]
print("到了啊啊",random.sample(li, k=1)[0])
Select(driver.find_element_by_xpath('//*[@id="RegionId"]')).select_by_value(str(random.sample(li, k=1)[0]))
time.sleep(5)
# 来到底部
element = driver.find_element_by_tag_name("body")
driver.execute_script("arguments[0].scrollIntoView(true);", element)
# 点击保存
driver.find_element_by_xpath("//button[@id='btn_save']").click()
time.sleep(10)
add_title_text = driver.find_element_by_xpath('//*[@id="j_list"]/div/div/div/ul/li[1]/div[2]/div[1]/span').text
time.sleep(5)
print("这里的标题",title_text)
print("新增的标题啊,",add_title_text)
driver.quit()
