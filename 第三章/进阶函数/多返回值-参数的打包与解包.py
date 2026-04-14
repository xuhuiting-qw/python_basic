
# 一、函数的多返回值
def calculate(x, y):
    res1 = x + y
    res2 = x - y
    return res1, res2
# 默认返回的是一个元组
result = calculate(4,6)
print(result)
print()
# 二、参数的打包与解包
# 1、打包接受参数
# *args    打包所有的位置参数（会形成一个元组）
# **kwargs  打包所有的关键字参数（会形成一个字典）
def show_info(*args, **kwargs):
    print(args)
    print(kwargs)
#  打包接受参数
show_info(99, 30, 20, name='张三', age=18)
# 2、解包传递参数
# *变量名      将元组拆解成一个一个独立的位置参数
# **变量名     将字典拆解成一个一个的key=value 形式的关键字参数
def show_info1(num1, num2, num3, name, age):
    print(num1, num2, num3)
    print(name, age)

nums = [60, 30, 20]
person = {'name': '张三', 'age': 20}
# 解包传递参数
show_info1(*nums, **person)
print()

# 3、打包接受参数 和 解包传递参数 一起使用
def show_info2(*args, **kwargs):
    print(args)
    print(kwargs)
nums = [989, 303, 203]
person = {'name': '张三', 'age': 20}
show_info2(*nums,**person)