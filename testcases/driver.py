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

        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def login(self):
        cookies = {
            "_ga": "GA1.2.266127702.1595935415",
            "_gid": "GA1.2.1081634098.1595935415",
            "_gat": "1",
            "name": "t64Q4XSx",
            "x-nSFu6": "bb3a03ef54104d33568c6331547da704",
            "x-EEGmc": "ba6e1e988c7c45e57a5437479bc239a2",
            "beegosessionID": "35be7a7302bf0787c1dc4cbfebfe29a0"
        }
        page = BasePage(self.driver)
        page.get("https://edu-alpha.xcurrency.com/", cookies=cookies)
        return self.driver

    def quit(self):
        self.driver.quit()
