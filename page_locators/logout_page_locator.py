# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/10/19

E-mail:keen2020@outlook.com

=================================


"""

from appium.webdriver.common.mobileby import MobileBy


class LogoutPageLocator(object):

    # 我
    me_button_loc = MobileBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId('com.tencent.mm:id/dkb').text('我')"



