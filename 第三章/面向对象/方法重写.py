
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

    # 方法重写：当子类中定义了一个与父类相同的方法，那么子类中的方法就会覆盖父类中的方法
    def speak(self,msg):
        super().speak(msg)
        print(f'姓名：{self.name},年龄：{self.age}，学号:{self.sno},我想说:{msg}')

s1 = Student('张三',18,'男','20260412123123')
s1.speak('你好')