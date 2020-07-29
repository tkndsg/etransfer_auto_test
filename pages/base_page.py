import logging
import time
import os

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


LOCATOR_LIST = {
    'css': By.CSS_SELECTOR,
    'id': By.ID,
    'name': By.NAME,
    'xpath': By.XPATH,
    'link_text': By.LINK_TEXT,
    'partial_link_text': By.PARTIAL_LINK_TEXT,
    'tag': By.TAG_NAME,
    'class_name': By.CLASS_NAME,

}


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def get(self, url, cookies=None):
        self._driver.get(url)
        if cookies:
            for k, v in cookies.items():
                self._driver.add_cookie({"name": k, "value": v})
            self._driver.get(url)

    # 执行js
    def run_script(self, js=None, elm=None):
        if js is None:
            raise ValueError("Please input js script")
        else:
            if elm is None:
                self._driver.execute_script(js)
            else:
                self._driver.execute_script(js, elm)

    # 定位单个元素
    def find_element(self, locator, value, timeout=10):
        try:
            try:
                timeout_int = int(timeout)
            except TypeError:
                raise ValueError("Type 'timeout' error, must be type int() ")
            try:
                locator = (LOCATOR_LIST[locator], value)
            except KeyError:
                raise KeyError(
                    "Please use a locator：'id_'、'name'、'class_name'、'css'、'xpath'、'link_text'、'partial_link_text'.")
            element =  WebDriverWait(self._driver, timeout_int).until(
                EC.presence_of_element_located(locator))
            # return self._driver.find_element(*locator)
            return element
        except:
            for i in range(timeout_int):
                element = self._driver.find_element(*locator)
                if element.is_displayed() is True:
                    return element
                else:
                    time.sleep(1)
            else:
                # 截图
                self.screenshot()
                # 记录日志
                logger.info("timeout, element {} not found!".format(value))
                return None

    # 定位多个元素
    def find_elements(self, locator, value, timeout=5):
        try:
            try:
                timeout_int = int(timeout)
            except TypeError:
                raise ValueError("Type 'timeout' error, must be type int() ")
            try:
                locator = (LOCATOR_LIST[locator], value)
            except KeyError:
                raise KeyError(
                    "Please use a locator：'id_'、'name'、'class_name'、'css'、'xpath'、'link_text'、'partial_link_text'.")
            WebDriverWait(self._driver, timeout_int).until(
                EC.presence_of_all_elements_located(locator))
            return self._driver.find_elements(*locator)
        except:
            # 截图
            self.screenshot()
            # 记录日志
            logger.info("timeout, element {} not found!".format(value))
            return None

    # 上滑动页面，看下方的内容
    def slip_down(self, step="300", times=1):
        scrip_content = "window.scrollBy(0," + step + ")"
        for i in range(times):
            self._driver.execute_script(scrip_content)
            time.sleep(1)

    def slip_up(self, step="300", times=1):
        step = str(abs(int(step)) * -1)  # 确保输入啥都是负数
        self.slip_down(step, times)

    # 点击单选按钮
    def radio_checked(self, radio_name, radio_value):
        try:
            for element in radio_name:
                value = str(element.get_attribute("value"))
                if value == radio_value:
                    return element
        except Exception as msg:
            return logging.info(msg)

    # 截图
    def screenshot(self, name="对象未找到的截图"):
        new_name = name + time.strftime("%Y-%m-%d %H_%M_%S", time.localtime()) + ".jpg"
        img_path = '../images/' + new_name
        return self._driver.get_screenshot_as_file(img_path)

    # 接受弹框
    def alert_accept(self):
        alert = self._driver.switch_to.alert
        alert.accept()

    # 判断是否包含提示信息
    def tips_text_in_element(self, locator, value, tips=None):
        try:
            try:
                locator = (LOCATOR_LIST[locator], value)
            except KeyError:
                raise KeyError(
                    "Please use a locator：'id_'、'name'、'class_name'、'css'、'xpath'、'link_text'、'partial_link_text'.")
            print(locator, tips)
            WebDriverWait(self._driver, 5, 1).until(
                EC.presence_of_element_located(locator))
            tips_text = WebDriverWait(self._driver, 5, 1).until(
                EC.text_to_be_present_in_element(locator, tips))
            if tips_text:
                return tips
        except:
            logger.info("timeout, element {} not found!".format(value))
            return None

    def is_element_exist(self, by, locator):
        flag = None
        time.sleep(1)
        try:
            self._driver.find_element(by, locator)
            flag = True
        except NoSuchElementException:
            flag = False
        finally:
            return flag

    def back_to_last_page(self):
        self._driver.back()

    def quit_browser(self):
        time.sleep(3)
        self._driver.quit()


