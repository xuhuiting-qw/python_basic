# 定义个Person类
class Person:
    # max_age、plant 都是类属性，类属性是保存在类身上的
    # 类属性可以通过类访问，也可以通过实例访问
    # 类属性通常用于保存:公共数据
    max_age = 120
    plant = '地球'

    # 初始化方法  (给实例添加属性)
    def __init__(self, name, age, gender):
        self.name = name
        self.gender = gender
        # 限制age的最大值
        if age <= Person.max_age:
            self.age = age
        else:
            self.age = Person.max_age

# 验证：类属性是保存在类身上的
print(Person.__dict__)

p1 = Person('张三',18,'男')
# 验证：实例对象是没有类属性的
print(p1.__dict__)

# 验证：类属性可以通过类访问，也可以通过实例访问
print(Person.max_age)
print(p1.max_age)
# 测试年龄超出范围
p2 = Person('李四',135,'男')
print(p2.__dict__)






