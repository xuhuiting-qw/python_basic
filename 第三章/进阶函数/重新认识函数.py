
# 1、函数也是对象
a1 = 100  #  int类的实例对象

def welcome():    # welcome函数是function类的实例对象
    print('你好！')
print(type(a1))
print(type(welcome))
print()
# 2、函数也可以动态添加属性
welcome.desc = '这是一个打招呼的函数！'
welcome.version = 1.0
print(welcome.desc)
print(welcome.version)
print()
# 3、函数可以赋值给变量
say_hello = welcome
say_hello()
print(say_hello.desc)
print()
# 4、可变参数 vs 不可变参数
# 不可变参数    data 指向堆中的内存地址变化（重新创建了一个值为888的内存地址）
a = 666
def we(data):
    print('函数调用前', data, id(data))
    data = 888
    print('函数调用后', data, id(data))

print('函数调用前', a, id(a))
we(a)
print('函数调用后', a, id(a))
print()
# 可变参数  b 在堆中指向的内存地址没有变化
b = [10,20,30]
def we1(data):
    print('函数调用前', data, id(data))
    data[2] = 888
    print('函数调用后', data, id(data))
print('函数调用前', b, id(b))
we1(b)
print('函数调用后', b, id(b))
print()
# 5、函数也可以作为参数
def we2():
    print('你好')
def caller(f):
    print('caller函数被调用了')
    f()
caller(we2)
print()
# 6、函数也可以作为返回值  we3函数中定义了一个show_msg函数，并将show_msg函数返回了所以we3的返回值是一个show_msg的函数
def we3():
    print('你好')
    def show_msg(msg):
        print(msg)
    return show_msg
result = we3()
# result 是一个函数
result('被调用了！')
