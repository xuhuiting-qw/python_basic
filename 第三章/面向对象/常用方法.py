
# 定义个Person类
class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self,msg):
        print(f'姓名：{self.name},年龄：{self.age}，我想说:{msg}')

# 定义一个Student类继承Person类
class Student(Person):
    def __init__(self, name, age, gender,sno):
        super().__init__(name, age, gender)
        self.sno = sno

p1 = Person('李四',20,'男')
s1 = Student('张三',18,'男','20260412123123')
# 1、isinstance(instance,Class) : 判断某个对象是否为指定类或其子类的实例
print(isinstance(s1, Student))
print(isinstance(p1, Person))
# 2、issubclass(Class1,Class2) :判断某个类是否是另一个类的子类
print(issubclass(Student, Person))
print(issubclass(Person, Student))
