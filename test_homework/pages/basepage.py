from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ""
    # 复用浏览器
    def __init__(self,driver_base=None):

        if driver_base == None:
            option = Options()
            option.debugger_address= "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=option)
        else:
            self.driver: WebDriver = driver_base

        if self._base_url != "":
            self.driver.get(self._base_url)

        self.driver.implicitly_wait(5)

    def find(self,by, value):
        return self.driver.find_element(by, value)

    def finds(self, by, value):
        return self.driver.find_elements(by, value)