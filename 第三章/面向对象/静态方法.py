from datetime import datetime


# 定义个Person类
class Person:

    # 初始化方法  (给实例添加属性)
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 静态方法
    # 使用 @staticmethod 装饰过的方法，就叫静态方法，静态方法也是保存在类的身上
    # 静态方法只是单纯的定义在类中，它不会收到:self、cls参数，它收到的参数都是自定义参数
    # 由于静态方法没有收到 self、cls参数，所以其内部不会访问任务 类和实例相关的内容
    # 静态方法通常用于定义：与类相关的工具方法
    @staticmethod
    def is_adult(year):
        current_year = datetime.now().year
        # 计算年龄
        age = current_year - year
        # 返回结果（成年返回True ，未成年返回False）
        if age >= 18:
            return True
        else:
            return False

# 验证：静态方法也是保存在类的身上
# print(Person.__dict__)

# 静态方法需要类调用
p1 = Person.is_adult(1998)
print(p1)


