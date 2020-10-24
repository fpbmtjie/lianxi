from appium.webdriver.common.mobileby import MobileBy

from qiyeweixin.packages.basepage import BasePage
from qiyeweixin.packages.manberpage import MenberPage


class AddresslistPages(BasePage):
    def goto_menberpage(self):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()' 
                                 '.scrollable(true).instance(0))' 
                                 '.scrollIntoView(new UiSelector()' 
                                 '.text("添加成员").instance(0));').click()
        return MenberPage(self.driver)
