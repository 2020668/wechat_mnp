# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2020/01/17

E-mail:keen2020@outlook.com

=================================


"""

import os
import time
import datetime
import datedelta
import logging

from common import logger


def uninstall_uiautomator2():
    os.system("adb uninstall io.appium.uiautomator2.server")
    print("uninstall uiautomator2.server successfully")

    os.system("adb uninstall io.appium.uiautomator2.server.test")
    print("uninstall uiautomator2.server.test successfully")


def uninstall_appium_settings():
    os.system("adb uninstall io.appium.settings")
    print("uninstall appium.settings successfully")


def get_cmd_result(command):
    a = os.popen(command)
    info = a.readlines()  # 读取命令行输出到list
    for line in info:
        line = line.strip("\r\n")
        print(line)
        print(type(line))


def time_custom(before_year=None, before_month=None, before_day=None, before_hour=None, before_minute=None, now=None):
    """
    :param before_year: the year number before now, int, example 3
    :param before_month: the month number before now, int, example 2
    :param before_day: the day number before now, int, example 2
    :param before_hour: the hour number before now, int, example 2
    :param before_minute: the minute number before now, int, example 2
    :param now: anything or None
    :return: before time, example 2019-12-03 15:36
    """
    time_style = "%Y-%m-%d %H:%M"
    now = datetime.datetime.now()

    if before_year:
        delta = datedelta.datedelta(years=before_year)
        before = now - delta
        return before.strftime(time_style)
    if before_month:
        delta = datedelta.datedelta(months=before_month)
        before = now - delta
        return before.strftime(time_style)
    if before_day:
        delta = datedelta.datedelta(days=before_day)
        before = now - delta
        return before.strftime(time_style)
    if before_hour:
        delta = datetime.timedelta(hours=before_hour)
        before = now - delta
        return before.strftime(time_style)
    if before_minute:
        delta = datetime.timedelta(minutes=before_minute)
        before = now - delta
        return before.strftime(time_style)
    if now:
        return datetime.datetime.now().strftime(time_style)


if __name__ == '__main__':
    uninstall_uiautomator2()
    uninstall_appium_settings()

    # get_cmd_result("allure serve output/allure")
    # get_cmd_result("adb devices")
    # a = time_custom(now=2222)
    # print(a)

