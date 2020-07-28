#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from pages.base_page import BasePage


class PayInfoPage(BasePage):
    _amount_input_box = ("xpath", "//*[@class='x-money-input__inner']")
    _pay_to_school_name = ("xpath", "//*[@class='step-title-desc']")
    _submit_button = ("xpath", "//*[@class='el-button x-button orders-next el-button--default']")

    def click_input_box(self):
        self.find_element(*self._amount_input_box).click()

    def input_amount(self, amount):
        self.find_element(*self._amount_input_box).send_keys(amount)

    def find_school_name(self):
        return self.find_element(*self._pay_to_school_name).text

    def click_submit_button(self):
        self.find_element(*self._submit_button).click()

