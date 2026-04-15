from functools import reduce

# reduce函数：将一组数据不断 "合并"，最终归并成一个结果
# 语法： reduce(合并函数,可迭代对象,初始值)
# 备注：reduce函数需要从functools模块中引入才能使用

# 数值统计
nums = [1, 2, 3, 4, 5]
# 1+2    3+3   6+4  10+5   计算过程
result = reduce(lambda x, y: x + y, nums)
print(result)
# 从 10 开始相加   10+1  11+2  13+3  16+4  20+5
result1 = reduce(lambda x, y: x + y, nums,10)
print(result1)

# 字符串的拼接
str_list = ['ab','cd','ef']
result2 = reduce(lambda x, y: x + y, str_list)
print(result2)
