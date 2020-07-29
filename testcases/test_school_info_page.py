#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from time import sleep

import pytest

from pages.pay_info_page import PayInfoPage
from pages.home_page import HomePage
from pages.school_info_page import SchoolInfoPage
from testcases.driver import Driver


class TestSchoolInfoPage:
    def setup_class(self):
        self.driver = Driver().login()
        self.home_page = HomePage(self.driver)
        self.pay_info_page = PayInfoPage(self.driver)
        self.school_info_page = SchoolInfoPage(self.driver)

    @pytest.mark.run(order=1)
    def test_goto_school_page(self):
        self.home_page.goto_pay_info_page().goto_school_info("5000")

    @pytest.mark.run(order=2)
    def test_input_payment_account(self):
        self.school_info_page.input_payment_account("good school")

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("school_info, assert_content", [
        (["", "", "", "", "", ""], ["请按照院校要求填写"]),
        (["Boxhill ", "666", "欧洲", "欧洲", "1", ""], ["长度应在 8~11 个字符以内"]),
        (["Boxhill School", "6666666666666666666", "欧洲的收款银行", "欧洲博斯希尔", "12345678", "敷衍附言"], ["SWIFT code"])
    ])
    def test_combo_input_school_info(self, school_info, assert_content):
        self.school_info_page.combo_input_school_info(school_info=school_info)
        for content in assert_content:
            assert content in self.school_info_page._driver.page_source
        sleep(1)

    def test_click_school_info_button(self):
        self.school_info_page.click_school_info_button()
        assert "学生资料" in self.driver.page_source

    def teardown_class(self):
        self.school_info_page._driver.quit()
