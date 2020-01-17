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


class LoginPage(BasePage):

    # 登录操作
    def login_for_pwd(self, pwd):
        self.wait_ele_visible(loc=Loc.pwd_input_loc, img_desc="密码输入框")
        self.input_text(loc=Loc.pwd_input_loc, value=pwd, img_desc="密码输入框")

        self.wait_ele_visible(loc=Loc.login_button_loc, img_desc="登录按钮")
        self.click_element(loc=Loc.login_button_loc, img_desc="登录按钮")

        return self

    def login_for_msg_code(self):
        self.wait_ele_visible(loc=Loc.msg_code_login_button_loc, img_desc="用短信验证码登录按钮")
        self.click_element(loc=Loc.msg_code_login_button_loc, img_desc="用短信验证码登录按钮")

        self.wait_ele_visible(loc=Loc.get_msg_code_button_loc, img_desc="获取验证码按钮")
        self.click_element(loc=Loc.get_msg_code_button_loc, img_desc="获取验证码按钮")

        msg_code = input("请输入短信验证码 --> :")
        self.wait_ele_visible(loc=Loc.msg_code_input_loc, img_desc="短信验证码输入框")
        self.input_text(loc=Loc.msg_code_input_loc, value=msg_code, img_desc="短信验证码输入框")

        self.wait_ele_visible(loc=Loc.login_button_loc, img_desc="登录按钮")
        self.click_element(loc=Loc.login_button_loc, img_desc="登录按钮")

        return self


if __name__ == '__main__':
    pass

