import pytest

from qiyeweixin.packages.app import App


class TestAddMenber:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_mainpage()

    def teardown(self):
        pass

    @pytest.mark.parametrize("name, gender, phone", [
        ("qqqq", "男", "13377772222"),
        ("eee", "女", "13327772222"),
        ("rrr", "女", "13337772222")
    ])
    def test_addmenber(self, name, gender, phone):
        # name = "www"
        # phone = 13899997777
        # gender = "男"
        mytoast = self.main.goto_addresslistpage().goto_menberpage().goto_contacteditpage().edit_name(name).edit_gender(gender).edit_phone(phone).click_save().get_toast()
        assert "添加成功" == mytoast