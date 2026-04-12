
# 定义个Person类
class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self,msg):
        print(f'姓名：{self.name},年龄：{self.age}，我想说:{msg}')

# 定义一个Student类（子类，派生类）继承Person类（父类、超类、基类）
class Student(Person):
    def __init__(self, name, age, gender,sno):
        # 在子类中，有两种方式去调用父类的初始化方法，主要来实现继承属性
        # 方式一
        super().__init__(name, age, gender)
        # 方式二
        # Person.__init__(self,name, age, gender)
        self.sno = sno



s1 = Student('张三',18,'男','20260412123123')
print(s1.__dict__)
print(type(s1))
# 查找speak方法的过程 1、实例自身(s1) => 2、Student类 => 3、Person类
s1.speak('你好')




