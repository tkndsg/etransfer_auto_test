#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from time import sleep

from pages.base_page import BasePage


class SchoolInfoPage(BasePage):
    _school_info_input = ("xpath", "//div[@class='x-input el-input']//input[@class='el-input__inner']")
    _school_info_button = ("xpath", "//button[@class='el-button x-button orders-next el-button--default']")

    def input_payment_account(self, content):
        self._driver.find_elements(*self._school_info_input)[0].click()
        self._driver.find_elements(*self._school_info_input)[0].clear()
        self._driver.find_elements(*self._school_info_input)[0].send_keys(content)

    def input_school_info(self, index, content):
        self._driver.find_elements(*self._school_info_input)[index].click()
        self._driver.find_elements(*self._school_info_input)[index].clear()
        if content:
            self._driver.find_elements(*self._school_info_input)[index].send_keys(content)

    def combo_input_school_info(self, input_num=None, school_info=None):
        if not school_info:
            school_info = ["Boxhill School", "6666666666666666666", "欧洲的收款银行", "欧洲博斯希尔", "12345678", "敷衍附言"]
        if not input_num:
            input_num = len(self._driver.find_elements(*self._school_info_input))
        for i in range(input_num):
            self.input_school_info(i, school_info[i])

    def click_school_info_button(self):
        self._driver.find_element(*self._school_info_button).click()

    def goto_student_info_page(self):
        pass

