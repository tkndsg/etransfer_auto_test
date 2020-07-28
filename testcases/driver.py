from selenium import webdriver
from pages.base_page import BasePage

class Driver:

    def __init__(self, browser="chrome"):
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "ie":
            self.driver = webdriver.Ie()
        elif browser == "safari":
            self.driver = webdriver.Safari()
        else:
            raise ValueError("browser parameter error")
        # 最大窗口

        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def login(self):
        cookies = {
            "xxx": "xxx",
            "xxx": "xxx",
            "xxx": "xxx",
        }
        page = BasePage(self.driver)
        page.get("https://edu-alpha.xcurrency.com/", cookies=None)
        return self.driver

    def quit(self):
        self.driver.quit()
