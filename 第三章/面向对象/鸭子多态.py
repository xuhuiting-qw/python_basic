
# 核心理念：如果一个东西看起来像鸭子，叫起来也像鸭子，那它就是鸭子
# 鸭子类型是一种编程风格，它不检查对象的类型，只关注对象能否“做某件事”（是否有对应的方法）

# 鸭子多态  很灵活，没有很多限制，有相同的方法即可
class Dog:
    def speak(self):
        print('我是一只小狗！')

class Cat:
    def speak(self):
        print('我是一只小猫！')

class Pig:
    def speak(self):
        print('我是一只小猪！')

def make_sound(animal):
    animal.speak()

d1 = Dog()
c1 = Cat()
p1 = Pig()
make_sound(d1)
make_sound(c1)
make_sound(p1)


