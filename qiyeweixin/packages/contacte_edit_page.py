from appium.webdriver.common.mobileby import MobileBy

from qiyeweixin.packages.basepage import BasePage

# 编辑成员信息页面



class ContactEditPage(BasePage):
    _edit_name = (MobileBy.XPATH, "//*[contains(@text,'姓名')]/../*[contains(@text,'必填')]")
    _gender_nan = (MobileBy.XPATH, "//*[contains(@text,'男')]")
    _female_ele = (MobileBy.XPATH, "//*[contains(@text,'女')]")
    _male_ele = (MobileBy.XPATH, "//*[contains(@text,'男')]")
    _phone_number = (MobileBy.XPATH, "//*[contains(@text,'手机号')]")
    _save_ele = (MobileBy.ID, "com.tencent.wework:id/hxt")

    def edit_name(self, name):
        self.find(self._edit_name).send_keys(name)
        return self

    def edit_gender(self,gender):
        self.find_click(self._gender_nan)
        if gender == "女":
            self.find_click(self._female_ele)
        else:
            self.find_click(self._male_ele)
        return self

    def edit_phone(self, phone):
        self.find(self._phone_number).send_keys(phone)
        return self

    def click_save(self):
        from qiyeweixin.packages.manberpage import MenberPage
        self.find_click(self._save_ele)
        return MenberPage(self.driver)



