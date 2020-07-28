#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from pages.base_page import BasePage


class HomePage(BasePage):
    # PO预设
    _insurance = ("xpath", "//*[text()='保险']")

    def click_insurance_tab(self):
        self.find_element(*self._insurance).click()
