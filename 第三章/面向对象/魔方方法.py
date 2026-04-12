
# 概念：魔法方法：以__xxx__命名的方法
# 特点：不需要我们手动调，Python会在特定的场景下，去自动调用
class Person:
    def __init__(self, name, age, idcard):
        self.name = name
        self.age = age
        self.idcard = idcard

    # 当执行print(Person的实例对象) 或 str(Person的实例对象)时调用
    def __str__(self):
        return f'{self.name}-{self.age}-{self.idcard}'

p1 = Person('张三',18,'123456')
print(p1)

