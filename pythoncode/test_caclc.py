# -*- coding:utf-8 -*-
import pytest
import yaml
from pythoncode.calc import Calculator

# yaml文件中获取测试数据
with open("./calc.yml", 'r', encoding='utf-8')as f:
    all_dates = yaml.safe_load(f)
    add_date = all_dates["dates"]["add"]
    add_ids = all_dates["dates"]["add_ids"]
    sub_date = all_dates["dates"]["sub"]
    sub_ids = all_dates["dates"]["sub_ids"]
    mul_date = all_dates["dates"]["mul"]
    mul_ids = all_dates["dates"]["mul_ids"]
    div_date = all_dates["dates"]["div"]
    div_ids = all_dates["dates"]["div_ids"]
    other_date = all_dates["dates"]["other_date"]
    other_date_ids = all_dates["dates"]["other_date_ids"]
    print(other_date_ids, "+++++++++++++++++++++++++++++++")
print("读取文件-------------------------")


class TestCalc:

    # 类级别setup
    def setup_class(self):
        print("测试开始")
        # 实例化
        self.calc = Calculator()
        print(all_dates["dates"]['add'])
        print(all_dates['dates']['add_ids'])

    # 类级别teardown
    def teardown_class(self):
        print("测试结束")

    # 加法正向测试
    @pytest.mark.add
    @pytest.mark.parametrize(
        'a, b, c',
        add_date,
        ids=add_ids
    )
    def test_add(self, a, b, c):
        results = self.calc.add(a, b)
        assert c == results

    @pytest.mark.sub
    @pytest.mark.parametrize(
        "a, b, c",
        sub_date,
        ids=sub_ids
    )
    def test_sub(self, a, b, c):
        results = self.calc.sub(a, b)
        assert c == results

    # 乘法测试
    @pytest.mark.mul
    @pytest.mark.parametrize(
        "a, b, c",
        mul_date,
        ids=mul_ids
    )
    def test_mul(self, a, b, c):
        results = self.calc.mul(a, b)
        # 断言 round保留两位小数
        assert c == round(results, 2)

    # 除法测试
    @pytest.mark.div
    @pytest.mark.parametrize(
        "a, b, c",
        div_date,
        ids=div_ids
    )
    def test_div(self, a, b, c):
        try:
            results = self.calc.div(a, b)

        except ZeroDivisionError:
            print(c)
        else:
            # 断言 round保留两位小数
            assert c == results

    @pytest.mark.test_other
    @pytest.mark.parametrize("a,b,c", other_date, ids=other_date_ids)
    def test_other(self, a, b, c):
        # 能转为int类型即可以进行运算
        try:
            int(a) and int(b)
        except ValueError:
            print(c)
        else:
            results = self.calc.add(a, b)
            assert c == results
