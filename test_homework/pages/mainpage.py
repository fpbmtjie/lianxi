from selenium.webdriver.common.by import By

from test_homework.pages.basepage import BasePage
from test_homework.pages.contactpage import ContactPage


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    def go_to_contactpage(self):
        self.driver.find_element(By.ID,"menu_contacts").click()
        return ContactPage(self.driver)