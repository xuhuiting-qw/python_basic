#coding=utf-8

'''
这是一段多行注释
注释注释
'''
print(25)
# 这是一段单行注释
print(25)

NAME = "张三"

age = 18
h = 65.312






#result 无类型  '张三'有类型-字符串
result = type('张三')
print(result)
print(type(18))
print(type(18.235))

# 当数字很大时，可以石用下划线将数字进行分组，只起到方便阅读数字的作用，对代码运行无影响
count = 300_000
house_price = 10_000_000

# python中整数没有上限值，但实际上会取决于执行代码的计算机的内存和处理能力
a = 9 ** 9999
# print(a)   # 此时运行会报错，因为python是将数字转为字符串，再打印出来，python中字符串的默认限制是4300位


# 浮点型的科学计数法表示
speed_of_sound = 3.4e+2  # 3.4 * 10的2次方  e/E 一个意思
world_population = 7.8e9  # 7.8 * 10的9次方

one_ml = 1e-3 # 1 * 10的-3次方

# 单/双引号 不能直接换行(要用圆括号才能换行)
message1 = '这是一串代码'
message2 = ("这是一"
            "串代码")

# 三个单/双引号，可以直接换行，也可以作为多行注释使用，还能作为文档字符串使用
message3 = """这是一
串代码"""

# 格式化输出
name1 = '张三'
gender = '男'
age1 = 18
weight1 = 63.3
# 1、直接用加号拼接  只用能字符串进行拼接
info1 = '姓名：' + name1 + ',性别：' + gender

# 2、使用占位符
# %s占位字符串，%f占位浮点数，%d占位十进制整数，%i占位整数（%s是万能的，执行时会尝试将数据类型转为字符串）
info2 = '姓名：%s,性别：%s,年龄：%i,体重：%f' % (name1, gender, age1, weight1)

# 3、使用f-string
info3 = f'姓名：{name1},性别：{gender},年龄：{age1},体重：{weight1}'

# 占位符精度控制
name_s = '张三'
print('姓名是%4s' % name_s) # 右边对齐，且用空格补全，总长度为4
print('姓名是%-4s' % name_s) # 在左边对齐，且用空格补全
print('姓名是%1s' % name_s) # 不起作用
print('姓名是%.1s' % name_s) # 最多输出1个字符
print('姓名是%4.1s' % name_s) # 最多输出1个字符，右对齐且补全三个空格

weight_f = 65.35
print('姓名是%7.2f' % weight_f) # 右边对齐，且用空格补全，
print('姓名是%-7.2f' % weight_f) # 在左边对齐，且用空格补全
print('姓名是%7f' % weight_f) # 不起作用，n的默认值为6
print('姓名是%.1f' % weight_f) # 保留一位小数，进行四舍五入
print('姓名是%7.0f' % weight_f) # 不要小数，右对齐且补全5个空格，总长度为7(整数+小数点+小数)

weight_d = 68.35
print('姓名是%7d' % weight_d) # 右边对齐，且用空格补全，只对整数位做操作，舍弃小数位
print('姓名是%-7d' % weight_d) # 在左边对齐，且用空格补全
print('姓名是%1d' % weight_d) # 不起作用
print('姓名是%.1d' % weight_d) # 不起作用
print('姓名是%.5d' % weight_d) # 长度是5，需要用三个0来补全
print('姓名是%7.5d' % weight_d) # 长度是5，需要用三个0来补全，右对齐且用两个空格补全



print('ab\tcd'.expandtabs(4)) # 确保制表位是4位
print('我\t是'.expandtabs(4)) # 一个中文两个字符




# 使用str() 将指定数据转换为字符串
# 使用int() 将指定数据转换为整型  （会自动去除数字两边空格，数字中间空格不行； int('15.6') 不能转换）
# 使用float() 将指定数据转换为浮点型  （会自动去除数字两边空格，数字中间空格不行）

# 布尔类型是int类型的子类型，底层的本质是1表示True,0表示 False
# print(int(True))
# print(int(False))


# and返回的不一定是布尔值，返回的是某个参与计算的值本身
# 规则：and会先看左边，左边为假的话，直接返回左边，否则返回右边
# 备注：若参与and运算的值不是布尔值，那么python会自动转为布尔值，在进行逻辑操作


# print(2 - 2 and True)
# print('' and True)
# print(True and 8 / 4)
# print(3 + 3 and 3 * 4)
# print(True and False)


# or返回的不一定是布尔值，返回的是某个参与计算的值本身
# 规则：or会先看左边，左边为真的话，直接返回左边，否则返回右边
# 备注：若参与or运算的值不是布尔值，那么python会自动转为布尔值，在进行逻辑操作

# print(2 - 2 or True)
# print('你好' or '')
# print(False or 8 / 4)
# print(3 + 3 or 3 * 4)
#
# not用于取反
# 备注：若参与not运算的值不是布尔值，那么python会自动转为布尔值，再进行逻辑操作
# not返回的值，一定是布尔值


# # 使用input()获取用户输入
# name_i = input("请输入你的姓名：")
# age_i = input("请输入你的年龄：")
# # input()获取的内容全部是字符串类型
# print(type(name_i))
# print(f'{name_i} ，你明年的年龄是{int(age_i) + 1}')


# # 双分支
# i = int(input("请输入一个数字："))
# if i >  14 :
#     print(f"{i} 是大于 14")
#     if True:
#         print('成功执行该代码')
# elif i<=13:
#     print(f'{i} 是小于14')
# elif i == 14:
#     print(f'{i} 是等于14')

# 九九乘法表
# for row in range(1, 10):
#     for n in range(1, row + 1):
#         print(f'{row} * {n} = {row * n}',end = '\t')
#     print()

# 定义函数
def we():
    print('调用了该函数')
# 调用函数
we()


def he(num,ange):
    print(f'第一个参数是：{num}')
    print(f'第二个参数是：{ange}')
#  位置参数
he(1,15.3)
# 关键字参数 不用担心参数顺序
# 使用关键字参数时，位置参数必须在关键字参数之前
he(ange='hello',num=15)


def wee(name,num,ange='默认值'):
    print(f'名字是；{name},数量是：{num},还有一个参数:{ange}')
wee('张三',14)
wee('张三',num=15,ange='你好啊！')
# print函数底层给end函数设置了默认值
print('123',end='!!')
print()


# 可变位置参数
# 定义函数（使用*args去接受）
def test(*args):
    print(args)
test('张三',18,65.3)

# 可变关键字参数
# 定义函数（使用**kwargs）
def test1(**kwargs):
    print(kwargs)
test1(name='张三',age_s=18,he=65.3)

def test2(*args,c='你好',**kwargs):
    print(args)
    print(c)
    print(kwargs)
test2('张三',18,65.3,name='张三',age_s=18,he=65.3)
print()
print()
print()

def add(n1, n2):
    return n1 + n2
print(add(3,4))
print(type(add(3,4)))



r = 100
def test_1(b):
    global r
    r = 300
    print(r,b)
test_1(1)
print(r)
print()
print()




# 使用递归求一个数的阶乘
# n! = n* (n-1)!

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
print(factorial(5))


def add(n1, n2):
    """
    计算两个数相加结果
    :param n1:
    :param n2:
    :return:二者相加的结果
    """
    return n1 + n2

add(1,2)

print()


# 健身挑战赛
def total(*nums):
    """
    计算运动量总数
    :param nums: 每次的运动量
    :return: 返回总值
    """
    return sum(nums)


def avg(totals, days=4):
    """
    计算平均值
    :param totals: 总运动量
    :param days: 天数 默认4天
    :return: 返回平均值
    """
    return totals / days

def success(totals,goal=120):
    """
    挑战赛结果
    :param totals: 运动总量
    :param goal: 目标运动量
    :return: 返回挑战赛结果
    """
    if totals>=goal:
        return '恭喜！挑战成功！'
    else:
        return '很遗憾，挑战失败！'

def main(title,day,goal):
    print(f'【{title}】挑战【{day}】天,请输入每天的运动量：')
    num1 = int(input('第一天：'))
    num2 = int(input('第二天：'))
    num3 = int(input('第三天：'))
    num4 = int(input('第四天：'))
    num5 = int(input('第五天：'))
    totals = total(num1,num2,num3,num4,num5)
    avg_day = avg(totals,day)
    results = success(totals,goal)
    print(f'运动总量：{totals},平均每天运动：{avg_day:.1f},挑战结果是：{results}')

main('跳绳',5,120)




