
# 装饰器：
# 1、包含 __call__方法的类,就是类装饰器
# 2、像调用函数一样，去调用类装饰器的实例对象，就会触发 __call__方法的调用
# 3、__call__方法通常接收一个函数作为参数，并且会返回一个新函数
class SayHello:
    def __call__(self,func):
        def w(*args, **kwargs):
            print('你好，我要开始计算了')
            return func(*args, **kwargs)
        return w

# 使用@语法糖使用类装饰器
@SayHello()     # 类装饰器  类似 say = SayHello() result  = say(add)
def add(x, y):
    print(f'输出{x}和{y}的相加计算结果')
    return x + y

# 使用SayHello 去装饰 add 函数 （手动装饰）
# say = SayHello()
# result  = say(add)
# print(result(10, 20))

# 推荐使用 @SayHello()
print(add(10, 30))
print()

# 带参数的类装饰器
class SayHello1:
    def __init__(self,msg):
        self.msg = msg

    def __call__(self,func):
        def w(*args, **kwargs):
            print(f'你好，我要开始{self.msg}计算了')
            return func(*args, **kwargs)
        return w

@SayHello1('加法')
def add1(x, y):
    print(f'输出{x}和{y}的相加计算结果')
    return x + y

print(add1(20, 30))
print()

# 多个类装饰器的使用
class Test1:
    def __call__(self,func):
        def w(*args, **kwargs):
            print('我是Test1追加的逻辑')
            return func(*args, **kwargs)
        return w

class Test2:
    def __call__(self,func):
        def w(*args, **kwargs):
            print('我是Test2追加的逻辑')
            return func(*args, **kwargs)
        return w
@Test1()
@Test2()
def add2(x, y):
    print(f'输出{x}和{y}的相加计算结果')
    return x + y

print(add2(20, 30))