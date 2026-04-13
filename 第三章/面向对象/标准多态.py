
# 多态的概念：同一个方法名，在不同的对象上调用时，能呈现出不同的行为
# Python中支持 标准多态、鸭子多态
# 标准多态（三个条件） ： 有继承关系、有方法重写、有类型限制
class Animal:
    def speak(self):
        print('我是一只动物！')

class Dog(Animal):
    def speak(self):
        print('我是一只小狗！')

class Cat(Animal):
    def speak(self):
        print('我是一只小猫！')

class Pig:
    def speak(self):
        print('我是一只小猪！')

# 传入实例对象必须是Animal类或者是它的子类
def make_sound(animal:Animal):    # 类型注解
    # 多态的体现
    animal.speak()

a1 = Animal()
d1 = Dog()
c1 = Cat()
p1 = Pig()
make_sound(a1)
make_sound(d1)
make_sound(c1)
#  此写法不推荐。在其他语言中会报错
# make_sound(p1)












