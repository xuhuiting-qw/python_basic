# 定义个Person类
class Person:
    # 初始化方法  (给实例添加属性)
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 自定义方法
    # speak方法收到的参数是：调用speak方法的实例对象(self),其他参数
    # speak方法只有一份，保存在Person类身上的，所有Person类的实例对象，都可以调用到speak方法
    def speak(self,msg):
        print(f'姓名：{self.name},年龄：{self.age}，我想说:{msg}')

# 验证：speak方法是存在Person类身上的
print(Person.__dict__)

p1 = Person('张三',18,'男')
# 验证一下，Person实例对象身上没有speak方法
# 但是Person实例对象可以调用speak方法
# 当执行p1.speak()的时候，查找speak方法的过程：1、实例对象自身(p1) => 2、实例的"缔造者"的身上
p1.speak('好好学习！')



