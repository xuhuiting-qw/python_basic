
class Person:
    def __init__(self, name, age, idcard):
        self.name = name       # 公有属性：当前类中、子类中、类外部 都可以访问
        self._age = age        # 受保护的属性：在当前类中、子类中，可以访问
        self.__idcard = idcard # 私有属性：在当前类中访问

    # 受保护属性和私有属性同理
    # 注册age属性getter方法，当访问Person实例的age属性时。下面的age方法就会被自动调用
    @property
    def age(self):
        return self._age

    # 注册age属性setter方法，当修改Person实例的age属性时。下面的age方法就会被自动调用
    @age.setter
    def age(self,value):
        self._age = value

p1 = Person('张三', 18, '男')
print(p1.name)
print(p1.age)
p1.age = 33
print(p1.age)