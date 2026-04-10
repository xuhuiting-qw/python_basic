
# 定义有内容的可变集合 无序/
set1 = {10,10,30,50,60}
set2 = {'你好','你好','hello','hello！'}
# 此时  1和True都表示1，会去除一个
set3 = {10,1,True,None,15.6,'你好'}
print(set1,type(set1))
print(set2,type(set2))
print(set3,type(set3))
print()

# 定义一个不可变集合
frozenset1 = frozenset({10,10,30,50,60})
frozenset2 = frozenset({'你好','你好','hello','hello！'})
# 此时  1和True都表示1，会去除一个
frozenset3 = frozenset({10,1,True,None,15.6,'你好'})
print(frozenset1,type(frozenset1))
print(frozenset2,type(frozenset2))
print(frozenset3,type(frozenset3))
print()
# frozenset 接受的参数，可以是任意可迭代对象，但最终返回的一定是不可变集合
frozenset4 = frozenset([10,20,'hello'])
frozenset5 = frozenset('hello!')
print(frozenset4)
print(frozenset5)
print()

# 定义空集合
# 不能直接写{}来定义空集合，因为直接写{}定义的是：空字典
s1 = set()
print(s1,type(s1))
print()


# 新增
# 1、add(元素):向集合中添加元素
s1 = {10,20,30,40}
s1.add(100)
print(s1)
# 2、update(元素)：向集合中批量添加可迭代对象
s2 = {10,20,30,40,50}
s2.update([99,90])
print(s2)
s2.update((54,66))
print(s2)
s2.update({101,201})
print(s2)
print()

# 删除
s3 = {20,30,50,60,80,90,100}
# 1、remove(元素)：从集合中移除指定元素(若元素不存在，会报错)
s3.remove(30)
print(s3)
# 2、discard(元素)：从集合中移除指定元素(若元素不存在，不会报错)
s3.discard(0)
print(s3)
# 3、pop(元素)：从集合中任意删除一个元素，返回该元素
result1 = s3.pop()
print(s3)
print(result1)
# 4、clear()：清空集合
s3.clear()
print(s3)
print()

# 修改
# remove+add 方法
s4 = {20,30,50,60,80,90,100}
# 将20修改为99
s4.remove(20)
s4.add(99)
print(s4)

# 查
# 判断 30元素是否在集合中
result2 = 30 in s4
print(result2)
# 判断 20元素是否不在集合中
result3 = 20 not in s4
print(result3)





