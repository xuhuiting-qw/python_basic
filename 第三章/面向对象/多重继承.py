# 概念：多重继承：是指一个类同时继承多个父类，从而拥有多个父类的属性和方法
# 定义个Person类
class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self):
        print(f'姓名：{self.name},年龄：{self.age}')


class Worker:
    def __init__(self, company):
        self.company = company

    def do_work(self):
        print(f'我在{self.company}上班')


class Student(Person, Worker):
    def __init__(self, name, age, gender, company, sno):
        Person.__init__(self, name, age, gender)
        Worker.__init__(self, company)
        self.sno = sno

    def study(self):
        print(f'我在努力的学习')


s1 = Student('张三', 18, '男', '奶茶店', '1235689')
print(s1.__dict__)
s1.speak()
s1.do_work()
s1.study()

# 类的__mro__属性：用于记录属性和方法的查找顺序
print(Student.__mro__)