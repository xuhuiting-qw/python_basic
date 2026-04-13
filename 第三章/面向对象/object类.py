
# Python中，所有的类都继承了object类，即：object类是所有类的父类
class Person:
    def __init__(self, name, age, idcard):
        self.name = name
        self.age = age
        self.idcard = idcard

# 验证  所有类继承了object类
print(issubclass(Person,object))
print(issubclass(int,object))

# 因为object类是所有类的父类，所以Python中的所有对象，都间接是object类的实例
p1 = Person('张三',78,'123456789')
print(isinstance(p1, Person))
print(isinstance(p1, object))


# 所有对象都继承了object类所提供的：各种属性和方法，从而保证了每个对象都具备统一的基本能力
print(p1.__dict__)   # 对象身上自己的东西
print(dir(p1))       # 对象可以访问到的东西（自己的和继承过来的）