from annotationlib import type_repr

# 字典的定义
# 字典中的key不能重复，重复了会覆盖
# 定义一个有内容的字典
d1 = {'张三':45,'李四':56.3,'王五':89}
print(d1,type(d1))
# 定义空字典
d1 = {}
d2 = dict()
print(d1,type(d1))
print(d2,type(d2))

print()


# 字典的CURD
d1 = {'张三':45,'李四':56.3,'王五':89}
# 新增
d1['李六'] = 90
print(d1)
print()
# 查询
# 1、第一种方法   注意：此方法若key不存在，则会报错
print(d1['张三'])
# 2、第二种方法 使用get方法  若key不存在会返回默认值，若无默认值则会返回None
print(d1.get('李四'))
print(d1.get('hello'))
print(d1.get('hello', 111))
print()
#修改  注意若该key存在则是修改，不存在则是新增
d1['张三'] = 99
print(d1)
print()
# 删除
d1 = {'张三':45,'李四':56.3,'王五':89}
# 1、使用del删除   删除指定键值对，key不存在不会报错
del d1['王五']
print(d1)
# 2、使用pop删除   删除指定键值对，并返回value（若key不存在会返回默认值）
print(d1.pop('李四'))
print(d1.pop('hello',123))
print()
# 3、使用clear删除  会清空字典
d1.clear()
print(d1)
print()



# 字典的常用方法
d1 = {'张三': 45, '李四': 56.3, '王五': 89}
# 1、字典.keys() ----获取字典中所有的key 返回类型是dict_keys
# dict_keys(dict_values/dict_items 类似) 类型没有下标，可以通过for循环一次取出
result1 = d1.keys()
print(result1, type(result1))
# 借助内置函数list函数，可以将dict_key转换成list
l1 = list(result1)
print(l1, type(l1))
# 2、字典.values() ----获取字典中所有的value 返回类型是dict_values
result2 = d1.values()
print(result2, type(result2))
# 3、字典.items() ----获取字典中所有的键值对（每组键值对以元组的形式呈现） 返回类型是dict_items
result3 = d1.items()
print(result3, type(result3))
print()

# 字典的循环  只能用for循环
d1 = {'张三': 45, '李四': 56.3, '王五': 89}
for key in d1:
    print(f'{key}同学的成绩是{d1[key]}')

for key in d1.keys():
    print(f'{key}同学的成绩是{d1[key]}')

