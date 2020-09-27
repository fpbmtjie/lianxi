"""
写一些Bicycle类，有run（骑行）方法，调用时显示骑行历程为传入的数字
再写一个电动车类，继承自自行车类，添加电池电量valume属性，参数传入
同时写两个方法
1、fill_charge（vol）用来充电，vlo为点亮
2、run（km）方法用于骑行，每骑行10km消耗1度，
当电量耗尽时调用Bicy的run方法骑行，通过传入的骑行里程数，显示骑行结果
"""


class Bicycle:
    # 骑行方法
    def run(self, km):
        print(f"一共骑行了{km}km")


# 再写一个电动车类继承自Bicycle
class EBicycle(Bicycle):
    # 类属性，类体内，方法之外
    # volume=100
    # 构造方法
    def __init__(self, valume):
        # 实例属性，类体内，方法之内，并以“self.变量名”的方式定义变量
        self.valume = valume

        # 局部属性只在当前方法使用
        # a=1

    def fill_charge(self, vol):
        vo = vol+self.valume
        print(f"当前电量为{vo}度")

    def run(self, km):
        # 有电时能骑行的距离
        e_km = self.valume*10
        if km-e_km <= 0 :
            print(f"骑行了{km}米")
        else:
            print(f"一共骑了{km}km，用脚骑了{km-e_km}km")
            # 第一种父类调用
            # bike = Bicycle()
            # bike.run(km-e_km)
            # 第二种调用父类方法，一般使用这种
            super().run(km-e_km)


# 类的实例化
bike = Bicycle()
bike.run(50)
ebike = EBicycle(20)
ebike.fill_charge(50)
ebike.run(1000)
