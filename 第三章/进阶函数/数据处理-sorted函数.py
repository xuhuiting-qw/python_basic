
# sorted函数：对一组数据进行排序，返回一组新数据
# 语法：sorted(可迭代对象,key=xxx,reverse = xxx)

# 按照字符串的长度去排序
names = ['python', 'sql', 'java']
result = sorted(names, key=lambda x: len(x))
print(result)
# 更推荐写法
result1 = sorted(names, key=len,reverse=True)
print(result1)

# 根据字典中的某个字段进行排序
# 根据年龄排序
person = [
    {'name': '张三', 'age': 18},
    {'name': '李四', 'age': 13},
    {'name': '王五', 'age': 20},
    {'name': '李六', 'age': 15}
]
result2 = sorted(person, key=lambda x: x['age'])
print(result2)

# max函数，min函数 也可以传递key参数，用于设置筛选依据
# 筛选年龄最大的学生
result3 = max(person, key=lambda x: x['age'])
print(result3)
