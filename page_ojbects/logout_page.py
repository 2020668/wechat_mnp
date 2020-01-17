# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2020/01/17

E-mail:keen2020@outlook.com

=================================


"""

from common.basepage import BasePage
from page_locators.login_page_locator import LoginPageLocator as Loc
from common.tools import uninstall_appium_settings, uninstall_uiautomator2
from data.common_data import CommonData as Cd
import time


class LogoutPage(BasePage):

    # 登录操作
    def logout(self, pwd):
        self.wait_ele_visible(loc=Loc.pwd_input_loc, img_desc="密码输入框")
        self.input_text(loc=Loc.pwd_input_loc, value=pwd, img_desc="密码输入框")

        self.wait_ele_visible(loc=Loc.login_button_loc, img_desc="登录按钮")
        self.click_element(loc=Loc.login_button_loc, img_desc="登录按钮")

        return self


if __name__ == '__main__':
    pass

