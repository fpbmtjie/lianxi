from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from qiyeweixin.packages.addresslistpage import AddresslistPages
from qiyeweixin.packages.basepage import BasePage


# 通讯录界面
class MainPage(BasePage):
    _addresslist_ele = (MobileBy.XPATH, "//*[@text='通讯录']")
    def goto_addresslistpage(self):
        sleep(2)
        self.find_click(self._addresslist_ele)
        return AddresslistPages(self.driver)