from qiyeweixin.packages.basepage import BasePage
from qiyeweixin.packages.mainpage import MainPage
from appium import webdriver

class App(BasePage):
    def start(self):
        if self.driver == None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "127.0.0.1：7555"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.WwMainActivity"
            caps["noReset"] = "true"
            # 动态页面需要
            caps['settings[waitForIdleTimeout]'] = 1

            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self.driver.launch_app()
        self.driver.implicitly_wait(10)
        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def end(self):
        pass

    # 前往通讯录界面
    def goto_mainpage(self):
        return MainPage(self.driver)