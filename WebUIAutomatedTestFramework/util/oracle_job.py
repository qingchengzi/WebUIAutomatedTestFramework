#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： 青城子
# datetime： 2021/4/1 21:03 
# ide： PyCharm

import os

from threading import Thread
from apscheduler.schedulers.blocking import BlockingScheduler  # 后台运行

from config import settings

sc = BlockingScheduler()

# 每天晚上23点55分50秒执行python main_run.py文件
@sc.scheduled_job('cron', day_of_week='*', hour=23, minute='55', second='50')
def foo():
    """定时任务的逻辑实现"""
    os.chdir(settings.BASE_DIR)
    scr_path = os.getcwd()
    print(scr_path)
    a = "python main_run.py"
    os.system(a)


def start_task():
    # 启动一个线程
    sc.start()
    t = Thread(target=foo)
    t.start()


if __name__ == '__main__':
    start_task()
