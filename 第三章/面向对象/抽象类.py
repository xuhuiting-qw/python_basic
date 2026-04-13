from abc import ABC, abstractmethod


# 抽象类：是一种不能实例化的类，通常作为规范，让子类去继承并实现其中定义的抽象方法
# MustRun类一旦继承了ABC类，那么就是抽象类
class MustRun(ABC):
    # @abstractmethod 注解 抽象方法
    @abstractmethod
    def run(self):
        pass

    # 普通方法
    def speak(self):
        print(f'我叫{self.name}')

class Person(MustRun):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def run(self):
        print(f'我叫{self.name}，我在努力的奔跑！')

p1 = Person('张三',18)
p1.run()
p1.speak()
