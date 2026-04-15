
# 列表推导式：用一条简洁语句，从可迭代对象中，生成新列表的语法结构
# 备注：列表推导式本质上是对for循环+append() 的一种简写形式
# 语法：[表达式 for 变量 in 可迭代对象]
# Python中没有元组推导式

# 需求：让列表中的每个元素，都变为原来的2倍，得到的是一个新列表

nums = [10,20,30,50]
# 方式一：用map函数
result1 = list(map(lambda x: x * 2, nums))
print(result1)

# 方式二：用for循环+append()
result2 = []
for n in nums:
    result2.append(n*2)
print(result2)

# 方式三：使用列表推导式
result3 = [n * 2 for n in nums]
print(result3)

# 待条件的列表推导式
result4 = [n * 2 for n in nums if n > 20]
print(result4)

# 字典推导式
names = ['张三', '李四', '王五']
scores = [90, 80, 88]
result5 = {names[i]: scores[i] for i in range(len(names))}
print(result5)

# 集合推导式
# 给每个人名后面加 ！
names1 = ['张三', '李四', '王五']
result6 = {n + '!' for n in names1}
print(result6)


