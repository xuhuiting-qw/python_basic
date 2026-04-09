
# 定义元组
# 正/负索引
t1 = (0,50,'你好',46.3,None,True)
print(t1[0])
print(t1[-1])

# 元组中如果存放了可变类型（列表）,那么可变类型中的内容认可以修改
# 元组中的元素不可修改
t2 = (0,1.2,'你好',[10,20,30,40])
t2[-1][0] = 90
print(t2)

# 定义空元组
t3 = ()
t4 = tuple()

# 定义有内容的元组
t5 = (10,)
print(t5,type(t5))
print()

# 元组常用方法
# 1、使用index方法，获取指定元素在元素中第一次出现的位置
t1 = (11,23,55,11)
print(t1.index(23))
# 2、使用count方法，获取指定元素在元组中出现的次数
print(t1.count(11))

# 内置函数
# 1、max函数，获取最大值
print(max(t1))
# 2、min函数，获取最小值
print(min(t1))
# 3、len函数，获取元组长度
print(len(t1))
# 4、sorted函数，排序。会返回一个新列表
t2 = sorted(t1,reverse=True)
print(t1)
print(t2)
# 5、sum函数，对元组的数据求和
print(sum(t1))
