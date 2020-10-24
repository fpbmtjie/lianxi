from appium.webdriver.common.mobileby import MobileBy

from qiyeweixin.packages.basepage import BasePage



class MenberPage(BasePage):
    _add_menber = (MobileBy.ID, "com.tencent.wework:id/i66")
    _toast = (MobileBy.XPATH, "//*[@class='android.widget.Toast']")
    def goto_contacteditpage(self):
        from qiyeweixin.packages.contacte_edit_page import ContactEditPage
        self.find_click(self._add_menber)
        return ContactEditPage(self.driver)

    def get_toast(self):
        mytoast = self.find(self._toast).text
        return mytoast