import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from test_homework.pages.basepage import BasePage
from test_homework.pages.contactpage import ContactPage


class DepartmentPage(BasePage):
    _department_name = (By.CSS_SELECTOR, "[name='name']")
    _click_department = (By.CSS_SELECTOR, ".js_toggle_party_list")
    _choice_department = (By.CSS_SELECTOR, "[class ='qui_dropdownMenu ww_dropdownMenu member_colLeft js_party_list_container']")
    _determine_button = (By.CSS_SELECTOR, "#__dialog__MNDialog__ [d_ck='submit']")
    _cancel_button = (By.CSS_SELECTOR, "#__dialog__MNDialog__ [d_ck='cancel']")

    def add_department(self,name):
        # self.driver.find_element(By.CSS_SELECTOR, "[name='name']").send_keys("业务部")
        # 点击打开下拉框
        # self.driver.find_element(By.CSS_SELECTOR, ".js_toggle_party_list").click()
        # print("已经打开下拉框")
        # 点击下拉框中的“练习”部门
        # ele = self.driver.find_element(By.ID,"1688854132851225_anchor")
        # sel = Select(ele)
        # sel.select_by_value("aaa")
        # Select(self.driver.find_element(By.ID,"1688854132851225_anchor")).select_by_value("练习")
        # 上面已经定义变量了，这里直接传入变量名并加上*号对定义的元组进行解包
        self.find(*self._department_name).send_keys(name)
        self.find(*self._click_department).click()
        dep = self.find(*self._choice_department).click()

        # 因为添加部门列表列表后，位置会发生变动，所以加了一层判断
        # 当dep非空的时候，点击dep中的第一个元素
        if dep is not None:
            dep[0].click()
        # return self是为了实现返回当前页面时依然可以实现链式调用
        return self

    def save_department(self):
        self.find(*self._determine_button).click()
        return ContactPage(self.driver)

    def cancel_department(self):
        self.find(*self._cancel_button).click()
        return ContactPage(self.driver)


