
# map函数：对一组数据中的每一个元素，统一执行某种操作(加工),并生成一组新数据
# 语法格式：map(操作函数，可迭代对象)

# 统一数据处理
nums = [20,40,60,80]
# map函数的返回值是一个迭代器对象，需要手动遍历或者手动转换类型
result = map(lambda x: x * 2, nums)
print(list(result))

# 字符串转换
# 转成大写
names = ('python', 'java', 'js')
result1 = map(lambda x: x.upper(), names)
print(tuple(result1))

# 类型转换
# 将字符串转成int类型
str_number = {'1', '2', '3', '4'}
result2 = map(int, str_number)
print(set(result2))
# 返回的是迭代器对象，且一旦遍历完成，都会被“耗尽”
print(set(result2))
# 此写法不会被“耗尽”
result3 = set(map(int, str_number))
print(result3)
print(result3)

# 注意点：
# 1、延迟执行：map不会立刻计算，只有在“需要结果”时才执行计算
# 2、返回的是迭代器对象，且一旦遍历完成，就会被“耗尽”
# 3、map不会影响元素数量