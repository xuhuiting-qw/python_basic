
class Person:
    def __init__(self, name, age, idcard):
        self.name = name       # 公有属性：当前类中、子类中、类外部 都可以访问
        self._age = age        # 受保护的属性：在当前类中、子类中，可以访问
        self.__idcard = idcard # 私有属性：在当前类中访问

    def speak(self):
        print(f'姓名：{self.name},年龄：{self._age},身份证号:{self.__idcard}')

class Student(Person):
    def hello(self):
        print(f'我是一名学生，姓名：{self.name},年龄：{self._age},身份证号:{self.__idcard}')


p1 = Person('张三',20,'420985200302067852')
p1.speak()
# idcard  是私有属性，子类中不能访问，以下示例会报错
# s1 = Student('李四',30,'420985200302062356')
# s1.hello()


print(p1.name)
# 在类的外部，如果强制访问【受保护的属性】也可以访问到，但十分不推荐
print(p1._age)
# 在类的外部，如果强制访问【私有属性】不能访问到，以下示例会报错
# print(p1.__idcard)