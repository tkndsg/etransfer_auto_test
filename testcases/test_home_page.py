#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from time import sleep
import pytest
from pages.home_page import HomePage
from testcases.driver import Driver


class TestHomePage:
    def setup_class(self):
        self.driver = Driver().login()
        self.home_page = HomePage(self.driver)

    @pytest.mark.run(order=1)
    def test_whole_page(self):
        self.home_page.slip_down("1000", 5)
        self.home_page.slip_up("1000", 5)
        assert "我的订单", "加入我们" in self.home_page._driver.page_source

    @pytest.mark.run(order=2)
    def test_switch_tab_to_bond(self):
        self.home_page.click_bond_tab()
        assert "选择保证金机构开始汇款" in self.home_page._driver.page_source

    @pytest.mark.run(order=3)
    def test_switch_tab_to_insurance(self):
        self.home_page.click_insurance_tab()
        assert "选择保险机构开始汇款" in self.home_page._driver.page_source

    @pytest.mark.run(order=4)
    def test_switch_tab_to_rent(self):
        self.home_page.click_rent_tab()
        assert "请输入住房机构名称开始汇款" in self.home_page._driver.page_source

    @pytest.mark.run(order=5)
    def test_switch_tab_to_tuition(self):
        self.home_page.click_tuition_tab()
        assert "搜索你的学校开始汇款" in self.home_page._driver.page_source

    def test_click_search_box(self):
        self.home_page.click_search_box()
        assert "博斯希尔中学" in self.home_page._driver.page_source
        self.home_page.search_box_input("悉尼大学")
        self.home_page.select_first_school()
        assert "The University of Sydney" in self.home_page._driver.page_source
        sleep(1)

    def teardown_class(self):
        self.driver.quit()

