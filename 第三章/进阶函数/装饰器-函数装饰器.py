# 装饰器：
# 1、装饰器是一种 可调用对象（通常是函数），它能接收一个函数作为参数，并且会返回一个新函数
# 2、装饰器可以在不修改原函数代码的前提下，增强或者改变原函数的功能

# 实际应用：在不改变原函数的前提下，给函数统一加上：日志、计时、校验、缓存等功能

# 关键点：
# 1、接受被装饰的函数，同时返回新函数
# 2、装饰器"吐出来"的是 w 函数，以后别人调用的也是w函数
# 3、为了保证参数的兼容性，w函数要通过 *args 和**kwargs接收参数
# 4、w 函数中主要做的是 调用原函数（被装饰的函数）、执行其逻辑，但要记得将原函数的返回值return出去

# 需求：在不修改add函数的前提下，给add函数增加一些额外的功能，例如 计算前打印一句欢迎语
# 此时 say_hello 就是一个装饰器
def say_hello(func):
    def w(*args, **kwargs):
        print('你好，我要开始计算了')
        return func(*args, **kwargs)
    return w

@say_hello        # 类似这一步  result = say_hello(add)
def add(x, y):
    print(f'输出{x}和{y}的相加计算结果')
    return x + y
# 手动装饰
# result = say_hello(add)
# print(result(9, 10))
# 推荐   @say_hello 装饰器
print(add(10, 20))
print()

# 进阶：带参数的装饰器 (三层嵌套，外层是接收配置，中间层接收函数，内层接收具体参数)
def say_hello1(msg):
    def outer(func):
        def w(*args, **kwargs):
            print(f'你好，我要开始{msg}计算了')
            return func(*args, **kwargs)
        return w
    return outer


@say_hello1('加法')  # 将 add1 函数 交给了返回的函数(outer函数)
def add1(x, y):
    print(f'输出{x}和{y}的相加计算结果')
    return x + y

@say_hello1('减法')
def sub(x, y):
    print(f'输出{x}和{y}的相减计算结果')
    return x - y

print(add1(10, 15))
print(sub(10, 15))
print()

# 进阶：多个装饰器一起使用
def test2(func):
    print('我是test2装饰器')
    def w(*args, **kwargs):
        print('test2追加的逻辑')
        return func(*args, **kwargs)
    return w

def test1(func):
    print('我是test1装饰器')
    def w(*args, **kwargs):
        print('test1追加的逻辑')
        return func(*args, **kwargs)
    return w

@test1
@test2
def add2(x, y):    #  add2 = test1(test2(add2))
    print(f'输出{x}和{y}的相加计算结果')
    return x + y

#  test2 先工作，再是test1工作，再是先被test2追加逻辑，之后被test2追加逻辑的整体再被test1追加逻辑
print(add2(10, 50))
