
# 1、在python文件中，一个.py文件就是一个模块(Module)
# 2、模块中可以包含：变量、函数、类等很多内容
# 3、通常把能够实现某一特定功能的代码，集中放在一个模块中(模块就类似于一个工具箱)
# 4、模块可以提高代码的可维护性 与 可复用性，还可以避免命名冲突

# 模块的分类：
# python 中的模块分为三类，分别是：标准库模块、自定义模块、第三方模块

# 命名注意点：
# 1、要符合标识命名规则
# 2、模块名(.py文件)区分大小写
# 3、不要与标准模块同名(一旦同名，python会优先引入标准库模块)

# 常见模块导入方式
# 1、import 模块名
# import order
# import pay

# 2、 import 模块名 as 别名
# import order as o
# import pay as p

# 3、from 模块名 import 具体内容1，具体内容2,.....    (引入部分内容)
# from order import max_order_amount,show_info
# from pay import timeout,show_info
# print(max_order_amount)
# print(timeout)
# show_info()

# 4、from 模块名 import 具体内容1 as 别名，具体内容2 as 别名,.....
# from order import max_order_amount as max_amt,show_info as show1
# from pay import timeout as tm,show_info as show2
# print(max_amt)
# print(tm)
# show2()
# show1()

# 5、from 模块名 import *  (不推荐这么写)
from order import *
from pay import *

# 关于 __all__
# 1、在python模块中，可以通过__all__来控制[from 模块名 import * ] 能导入那些内容
# 2、__all__ 的值可以是：元组、列表


# 关于__name__:
# __name__是每个Python模块(.py文件) 都拥有的一个内置变量
# 它的具体值取决于模块的运行方式
# 1、作为主程序直接运行, __name__ 的值是 __main__
# 2、作为模块被导入到其他程序中运行,__name__的模块的文件名(不带.py)


