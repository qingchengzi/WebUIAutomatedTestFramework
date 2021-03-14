import random
from config import setting

city_list = setting.PROPERTY_PARAMETERS.get("city_type")  # 城市
random_city = city_list[random.randrange(len(city_list))]
print(random_city)








# li = ["tian", "xiang"]
# print(li[random.randrange(0,len(li))])
# print(li[random.randrange(1,len(li))])
# random_k = random.randrange(1, len(li))
# print(random_k)
# rest_li = random.sample(li, k=random_k)
# print(rest_li)
# from util.common_class import PublicTools
# from config import setting
# obj_com = PublicTools()
#
# img_list = obj_com.get_image()
# list_len = random.sample(img_list, k=random.randrange(1, 5))
# for i in range(len(list_len)):
#     print(list_len[i])
# li = [1, 2, 3, 9]
# print(random.sample(li, k=1)[0])



# def fun(*args):
#     print(args[0])
#     print(args[1])
#
#
# fun('//*[@id="sl_baselang"]', "zh-cn")
