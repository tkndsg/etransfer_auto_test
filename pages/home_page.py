#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from pages.base_page import BasePage
from pages.pay_info_page import PayInfoPage


class HomePage(BasePage):
    # PO预设

    _tuition = ("xpath", "//*[text()='交学费']")
    _bond = ("xpath", "//*[text()='保证金']")
    _insurance = ("xpath", "//*[text()='保险']")
    _rent = ("xpath", "//*[text()='交房租']")
    _search_box = ("xpath", "//*[@class='el-input__inner']")
    # _search_box = ("xpath", "//*[text()='搜索你的学校开始汇款']")
    _first_option = ("xpath", "//*[@class='channel-name el-col el-col-24']")

    def click_tuition_tab(self):
        self.find_element(*self._tuition).click()

    def click_bond_tab(self):
        self.find_element(*self._bond).click()

    def click_insurance_tab(self):
        self.find_element(*self._insurance).click()

    def click_rent_tab(self):
        self.find_element(*self._rent).click()

    def click_search_box(self):
        self.find_element(*self._search_box).click()

    def search_box_input(self, school_name="悉尼大学"):
        self.find_element(*self._search_box).send_keys(school_name)

    def select_first_option(self):
        self.find_elements(*self._first_option)[4].click()

    def goto_pay_info_page(self, pay_type="tuition", option="first"):
        if pay_type == "tuition":
            self.click_tuition_tab()
        elif pay_type == "bond":
            self.click_bond_tab()
        elif pay_type == "insurance":
            self.click_insurance_tab()
        elif pay_type == "rent":
            self.click_rent_tab()

        self.click_search_box()

        if option == "first":
            self.find_elements(*self._first_option)[4].click()
        elif 1 <= int(option) <= 10:
            pass
        else:
            pass
        return PayInfoPage(self._driver)




