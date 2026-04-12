
from datetime import datetime

# 定义个Person类
class Person:
    max_age = 120
    planet = '地球'
    # 初始化方法  (给实例添加属性)
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # speak方法、run方法 都属于 实例方法
    def speak(self,msg):
        print(f'姓名：{self.name},年龄：{self.age}，我想说:{msg}')

    # 使用 @classmethod 装饰过的方法 就叫类方法
    # 类方法收到的参数：当前类本身(cls)、自定义的参数
    # 因为收到了cls参数，所以类方法中是可以访问类属性
    # 类方法通常用于实现：与类相关的逻辑。例如：操作类级别的信息和一些工厂方法
    @classmethod
    def change_planet(cls,data):
        cls.planet = data
        print(f'我是test1，数据是:{data}')

    @classmethod
    def create(cls,info_str):
        # 从info_str 中获取到有效信息
        name,year,gender = info_str.split('-')
        # 获取当前年份
        current_year = datetime.now().year
#        计算年龄
        age = current_year - int(year)
#         创建并返回Person类的实例
        return cls(name,age,gender)

# 类方法需要类调用
Person.change_planet('月球')

# 类方法通常用于实现：与类相关的逻辑。例如：操作类级别的信息和一些工厂方法
# 1、操作类级别的信息
Person.change_planet('火星')
p1 = Person('张三',18,'男')
print(p1.planet)

# 2、工厂方法之一
p3 = Person.create('王五-2003-女')
print(p3.__dict__)
