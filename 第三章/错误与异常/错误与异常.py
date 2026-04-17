
# 错误：代码本身有语法问题，解释器无法执行代码  ------无法通过异常处理机制解决
# 异常：代码在语法上面没有问题，但在执行过程中出现了问题----可以通过异常处理机制解决

# 一些开发中常见的异常
# 1、ZeroDivisionError:当除数为0时触发
# num = 100
# result = num / 0

# 2、TypeError:当操作的数据类型不正确或者不兼容时触发
# result1 = 'hello' + 1

# 3、AttributeError:当对象没有指定的属性或者方法时触发
# 演示1
# nums = [0,1,2,3]
# nums.add(40)
# 演示2
# class Person:
#     def __init__(self,name):
#         self.name = name
# p1 = Person('张三')
# print(p1.name)
# print(p1.age)

# 4、IndexError : 索引越界
# num1 = [0, 2, 3]
# print(num1[3])

# 5、NameError : 当使用了不存在的变量是触发
# print(a)

# 6、KeyError : 当访问字典中不存在的 key 时触发
# p1 = {'name':'张三'}
# print(p1['name'])
# print(p1['age'])

# 7、ValueError : 当值不合法，但类型正确时触发
# int('hello')
