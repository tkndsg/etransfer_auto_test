#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from time import sleep

from pages.pay_info_page import PayInfoPage
from pages.home_page import HomePage
from testcases.driver import Driver


class TestPayInfoPage:
    def setup_class(self):
        self.driver = Driver().login()
        self.home_page = HomePage(self.driver)
        self.pay_info_page = PayInfoPage(self.driver)

    def test_goto_pay_info_page(self):
        self.home_page.goto_pay_info_page("tuition", "first")

    def test_check_pay_info_page(self):
        school_name = self.pay_info_page.find_school_name()
        assert "预计此次汇款比银行便宜" in self.pay_info_page._driver.page_source
        assert school_name in self.pay_info_page._driver.page_source

    def test_input_amount(self):
        # self.pay_info_page.click_input_box()
        # sleep(3)
        self.pay_info_page.input_amount("5000")
        sleep(1)

    def test_submit_amount(self):
        self.pay_info_page.click_submit_button()
        assert "学校收款账户信息" in self.pay_info_page._driver.page_source

    def teardown_class(self):
        self.pay_info_page.close_browser()
