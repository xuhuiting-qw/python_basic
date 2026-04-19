# 知识点1、能被for循环遍历的对象，被称为：可迭代对象(iterable)
# 知识点2、可迭代对象(iterable) 能调用__iter__方法
# region
names = ['张三','李四','王五']
city = ('北京','上海')
names.__iter__()
# endregion

# 知识点3、调用__iter__ 方法会得到：迭代器(iterator)
# 备注1、__iter__ 是一个魔法方法，当调用iter函数时，__iter__会自动调用
# 备注2、可迭代对象.__iter__() 等价于  iter(可迭代对象)
# 备注3、如果iter(obj)能得到一个迭代器(iterator),那obj就是可迭代对象
print(names.__iter__())
print(iter(city))

# 知识点4、迭代器(iterator)拥有__next__方法，每次调用都会根据当前的状态，返回下一个元素
# 备注1、迭代器.__next__() 等价于 next(迭代器)
names = ['张三','李四','王五']
it = iter(names)
print(next(it))
print(next(it))
print(next(it))
print()

# 编写for循环遍历names列表
# for item in names:
#     print(item)

# for循环背后的逻辑
# 第一步：调用 可迭代对象的__iter__方法获取到一个迭代器(iterator)
it = iter(names)
# 第二步：开始无限循环
while True:
    try:
        # 第三步：使用next(迭代器) 获取下一个元素
        item = next(it)
        print(item)
    except StopIteration:
        # 第四步：捕获StopIteration 异常，结束循环
        break

# 知识点5、迭代器(iterator) 也拥有 __iter__方法，并且其返回值就是迭代器本身
# 设计的原因是：让for循环也能遍历迭代器(即：为了让iter(迭代器)不出错)
names = ['张三','李四','王五']
it = iter(names)
print(it)
print(iter(it))

# 知识点：迭代器协议：
# 1、能被iter()接收
# 2、能被next() 一步一步取值






