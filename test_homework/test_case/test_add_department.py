from selenium import webdriver

from test_homework.pages.mainpage import MainPage


class TestAddDepartment:
    def setup(self):
        self.mainpage = MainPage()

    def test_add_department(self):
        # self.mainpage = MainPage()
        department_list = self.mainpage.go_to_contactpage().go_to_departmentpage().add_department("业务部").save_department().get_department_list()
        assert "业务部" not in department_list

    def test_cancel_department(self):
        department_list = self.mainpage.go_to_contactpage().go_to_departmentpage().add_department("人事部1").cancel_department().get_department_list()
        assert "人事部2" not in department_list