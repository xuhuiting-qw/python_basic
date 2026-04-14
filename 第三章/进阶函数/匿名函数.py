
# 匿名函数：就是没有名字的函数，无需使用def关键字来定义
# 语法：Python中使用lambda关键字来定义匿名函数 ，格式为 lambda 参数 : 表达式
# 场景：当一个函数只用一次，只做一点点小事，使用匿名函数会更简洁

# 匿名函数
add = lambda x, y : x + y
add1 = lambda x : x + 2
add2 = lambda : '我是add2函数'
result = add(30,100)
result1 = add1(30)
result2 = add2()
print(result)
print(result1)
print(result2)
print()

# 使用匿名函数实现计算效果
def calculate(func, a, b):
    print('计算结果为:', func(a, b))

calculate(lambda x, y: x + y, 22, 44)
calculate(lambda x, y: x - y, 22, 44)

# 注意点
# 1、只能写一行，不能写多行代码
# 2、不能写代码块(if，for，while)
# 3、冒号右边必须是表达式，且只能写一个表达式
# 4、表达式结果自动作为返回值
is_adult = lambda age: '成年' if age >= 18 else '未成年'
print(is_adult(18))
print(is_adult(15))
