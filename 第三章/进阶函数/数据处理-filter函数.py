
# filter函数：从一组数据中，筛选出符合条件的元素（过滤），并组成一个组新的数据
# 语法格式：filter(过滤函数,可迭代对象)

# 筛选数值
# 筛选出大于30的数据
nums = [10,50,30,60]
result = list(filter(lambda x: x > 30, nums))
print(result)

# 筛选成年人
person = [
    {'name':'张三','age':18},
    {'name':'李四','age':13},
    {'name':'王五','age':20},
    {'name':'李六','age':15}
]
result1 = list(filter(lambda x: x['age'] >= 18, person))
print(result1)

# 过滤非字符串
names = ['张三','','李四',None,'王五']
result2 = filter(lambda x: x, names)
print(list(result2))

# 注意点：
# 1、延迟执行：filter不会立刻计算，只有在“需要结果”时才执行计算
# 2、返回的是迭代器对象，且一旦遍历完成，就会被“耗尽”
# 3、filter可能会影响元素数量
# filter函数特殊用法：如果不传递过滤函数，那么自动会过滤掉“假值”

data = [0, 1, None, '', 'hello', [], (), 5]
result3 = list(filter(None, data))
print(result3)
