import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from test_homework.pages.basepage import BasePage



class ContactPage(BasePage):
    _js_create_dropdown = (By.CSS_SELECTOR, ".js_create_dropdown")
    _adddepart = (By.CSS_SELECTOR, ".js_create_party")
    _dapartment_list = (By.CSS_SELECTOR, ".jstree-anchor")
    def go_to_departmentpage(self):
        from test_homework.pages.departmentpage import DepartmentPage
        print("准备点击++++")
        # WebDriverWait(self.driver,10).until(ec.element_to_be_clickable(self._js_create_dropdown))
        self.find(*self._js_create_dropdown).click()
        # self.driver.find_element(By.CSS_SELECTOR, ".js_create_dropdown").click()
        print("++++++++++")
        self.find(*self._adddepart).click()
        print("点击添加部门")


        return DepartmentPage(self.driver)

    def get_department_list(self):
        # 获取所有部门
        department_list = self.finds(*self._dapartment_list)
        return [departmen_name.text for departmen_name in department_list]
