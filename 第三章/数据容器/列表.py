from unittest import result

# 定义有内容的列表
list1 = [12, 23, 45]
list2 = ['你好', '你不好']
list3 = [13, '你不好', True, None]
list4 = [13, '你不好', True, None, [12, '111']]
# 定义空列表 （列表中的数据，后期会通过特定的写法填充）
list5 = []
list6 = list()
print(list1, type(list1))
print(list2, type(list2))
print(list3, type(list3))
print(list4, type(list4))
print(list5, type(list5))
print(list6, type(list6))
print()

# 正/负索引
list7 = [10, '你好', False, None]
print(list7[0])
print(list7[-1])

print()

# 新增操作
# 1、 列表.append(元素)    -----在列表的尾部追加一个元素
nums1 = [10, 50, 30, 20]
nums1.append(60)
print(nums1)
# 列表.insert(下标,元素)--------在列表指定的下标位置添加一个元素
nums2 = [10, 50, 30, 20]
nums2.insert(2, 60)
print(nums2)
# 列表.extend(可迭代对象)----------将可迭代对象中的内容一次取出，追加到列表的尾部
nums3 = [10, 50, 30, 20]
nums3.extend(range(1, 4))
print(nums3)
nums3.extend([0, 2, 3])
print(nums3)

print()

# 列表.pop(下标)---------删除指定的位置元素，并将删除的元素返回
det_num1 = [10, 50, 30, 20, 50]
result1 = det_num1.pop(1)
print(det_num1)
print(result1)
# 列表.remove(值)-------删除列表中第一次出现的指定值
det_num2 = [10, 50, 30, 20, 50]
det_num2.remove(50)
print(det_num2)
# 列表.clear() ---------删除列表中的所有元素（变成一个空列表）
det_num3 = [10, 50, 30, 20, 50]
det_num3.clear()
print(det_num3)
# del 列表[下标]-------删除指定位置的元素
det_num4 = [10, 50, 30, 20, 50]
del det_num4[4]
print(det_num4)
print()

# 使用index方法，查找指定元素在列表中第一次出现的下标，并返回下标
fruits = ['苹果', '桃子', '草莓', '凤梨', '苹果']
result2 = fruits.index('桃子')
print(result2)
# 使用count方法，计算列表中某元素出现的次数，并返回出现次数
result3 = fruits.count('苹果')
print(result3)
# 使用reverse方法，对列表进行反转（会改变原列表）
nums = [20, 12, 50, 23, 36]
nums.reverse()
print(nums)
# 使用sort方法，对列表进行排序（默认是从小到达排序），将reverse参数值设为True，就是从大到小排序
# 正序排序
nums.sort()
print()
# 倒序排序
nums.sort(reverse=True)
print(nums)
print()

# 使用内置函数 sorted函数,返回一个排序后的新容器
nums = [20, 17, 50, 23, 36]
# 正序排序
nums_new = sorted(nums)
print(nums)
print(nums_new)
# 使用内置函数 len函数，返回容器中的元素总数量
print(len(nums))
# 使用内置函数 max函数，返回容器中的最大值
print(max(nums))
# 使用内置函数 min函数，返回容器中的最小值
print(min(nums))
# 使用内置函数 sum函数，对容器中的数据进行求和（元素只能是数值）
print(sum(nums))

print()

# 定义一个成绩列表
score_list = [63, 50, 20, 23, 23.3]

# while 循环
index = 0
while index < len(score_list):
    print(score_list[index])
    index += 1
print()
# 1、for循环遍历列表
for item in score_list:
    print(item)
print()
# 2、通过range函数和 len函数按照索引遍历
for index in range(len(score_list)):
    print(score_list[index])
print()
# 3、通过enumerate函数，同时获取索引值和元素
# enumerate的start参数，可以让计数从指定值开始（不改变列表本身的索引）
for index, item in enumerate(score_list, start=5):
    print(index, item, score_list[0])

print()

# 实现一个成绩统计程序，可以对多名学生的成绩，进行统计和分析
# 用户可以连续输入学生成绩，知道用户输入"结束"字符串
print("学生成绩统计，当输入 '结束' 时，输入完毕")
score_list1 = []
while True:
    result = input("请输入学生成绩：")
    if result == '结束':
        print('输入完毕，开始统计！')
        break
    else:
        score_list1.append(int(result))

if score_list1:
    # 合格人数
    pass_count = 0
    # 优秀人数
    excellent_count = 0
    # 统计平均分
    avg = sum(score_list1) / len(score_list1)
    for item in score_list1:
        if item >= 60:
            pass_count += 1
        if item >= 90:
            excellent_count += 1
    #  合格率
    pass_rate = pass_count / len(score_list1) * 100
    #  优秀率
    excellent_rate = excellent_count / len(score_list1) * 100
    print(f'学生成绩：{score_list1},平均分：{avg},合格率：{pass_rate:.1f}%,优秀率：{excellent_rate:.1f}%')
else:
    print('没有输入任何成绩！')
