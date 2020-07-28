#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from pages.base_page import BasePage


class HomePage(BasePage):
    # PO预设

    _tuition = ("xpath", "//*[text()='交学费']")
    _bond = ("xpath", "//*[text()='保证金']")
    _insurance = ("xpath", "//*[text()='保险']")
    _rent = ("xpath", "//*[text()='交房租']")
    _search_box = ("xpath", "//*[@class='el-input__inner']")
    # _search_box = ("xpath", "//*[text()='搜索你的学校开始汇款']")
    _school_list_first = ("xpath", "//*[text()='The University of Sydney']")

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

    def select_first_school(self):
        self.find_element(*self._school_list_first).click()


