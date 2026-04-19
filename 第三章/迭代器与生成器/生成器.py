# 一、生成器
# 1、生成器函数：函数体中如果出现了yield关键字，那该函数是 生成器函数
# 2、生成器对象：调用 生成器函数 时，其函数不会立刻执行，而且返回一个生成器对象
# 备注 ：不管能否执行到yield所在的位置，只要函数中有yield关键字，那该函数，就是生成器函数

def demo():
    print('demo函数开始执行')
    yield '我是第一个yield返回的数据'
    print('开始执行demo函数逻辑')
    yield  '我是第二个yield返回的数据'
    print("返回的结果是100")
    return '100'

d = demo()
# print(d)

# 二、写在生成器函数中的代码，需要通过生成器对象来执行：
# 1、调用生成器对象的 __next__ 方法 ，会让生成器函数中的代码开始执行
# 2、当生成器函数中的代码开始执行后，遇到yield会“暂停”执行，并且其内部会记录“暂停”的位置
# 3、后续调用__next__方法时，都会从上一次“暂停”的位置，继续运行，直到再次回到yield
# 4、遇到return 会抛出StopIteration 异常，并将return 后面的表达式，作为异常信息
# 5、yield后面所写的表达式，会作为本次__next__方法的返回值
# result1 = next(d)
# print(result1)
# result2 = next(d)
# print(result2)
# try:
#     result3 = next(d)
# except StopIteration as e:
#     print(e)

# 三、生成器对象是一种特殊的迭代器(本质是通过yield自动实现了迭代器协议)
# 验证 ： 生成器对象d 和迭代器一样，也有用__iter__和__next__方法
# print(iter(d))
d1 = demo()
for item in d1:
    print(item)
print()

# 四、yield 也能写在循环里
def create_car(total):
    for index in range(total):
        yield f'这是第{index+1}台车'

# 生成器对象
# cars = create_car(5)
# for item in cars:
#     print(item)
# print()

# 五、yield from 能把一个 可迭代对象 里的东西依次 yield出去(代替 for+yield)
def nums():
    nums1 = [10,20,30,50]
    yield from nums1

n = nums()
print([x for x in n])
print()

# 六、使用生成器.send(值) 可以让生成器继续执行的同时，给上一次yield传值
# 备注1、next() 只能取值 ， send() 既能取值 也能送值
# 备注2：第一次启动生成器，不能传值
def demo2():
    print('demo函数开始执行')
    a = yield '我是第一个yield返回的数据'
    print(a)
    b = yield  '我是第二个yield返回的数据'
    print(b)
    return '100'

d = demo2()
print(next(d))
# 给 a 传值
print(d.send(120))
# 给 b 传值
try:
    print(d.send(888))
except StopIteration as e:
    print(e)
print()

# 用生成器实现遍历Person类的实例
class Person:
    def __init__(self,name,age,gender,address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.__attr = [name,age,gender,address]


    def __iter__(self):
        # yield self.name
        # yield self.age
        # yield self.gender
        # yield self.address
        yield from self.__attr

p = Person('张三', 20, '男', '湖北武汉')
print([n for n in p])
print()

def fibo(total):
    pre = 1
    cur = 1

    for index in range(total):
        if index < 2:
            yield 1
        else:
            value = pre + cur
            pre = cur
            cur = value
            yield value

f1 = fibo(5)
# for item in f1:
#     print(item)
print()
# 无论是迭代器，还是生成器对象，都可以用list、tuple、set等直接拿到其里面的所有内容(注意：容易挤爆内存)

# 生成器表达式：一种类似列表推导式的语法，快速创建生成器对象的方式
# 语法格式： (表达式 for 变量 in 可迭代对象)
# 什么时候适合用生成器表达式？ ----- 当每个结果，只依赖当前这一个元素时

nums1 = [10,20,30,50,60]

# 列表推导式:
result4 = [n * 2 for n in nums1]
print(result4)

# 生成器表达式
result5 = (n * 2 for n in nums1)
print(list(result5))





