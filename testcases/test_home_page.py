#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from pages.home_page import HomePage
from testcases.driver import Driver


class TestHomePage:
    def setup(self):
        self.driver = Driver().login()
        self.home_page = HomePage(self.driver)

    def test_switch_tab_to_insurance(self):
        self.home_page.click_insurance_tab()

    def teardown(self):
        self.driver.quit()

