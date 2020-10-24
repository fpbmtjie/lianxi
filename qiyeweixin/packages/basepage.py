from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver:WebDriver=None):
        self.driver = driver

    def find(self, ele):
        return self.driver.find_element(*ele)

    def find_click(self, ele):
        return self.find(ele).click()