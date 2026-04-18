#1、在Python中 ，包含[__init__.py]的文件夹就是一个包(package)
# 2、我们通常会把  某个特定功能相关的所有模块 放入一个包中
# 3、使用包可以进一步提升代码的可维护性、可复用性，便于管理大型项目


# 包和模块之间的关系：
# 1、一个模块就是一个.py文件，包是用来管理模块的目录(文件夹)
# 2、一个包中可以有多个模块，也可以有多个子包

# 包分为三类：标准库包、自定义包、第三方包

# 包命名注意点：
# 1、要符合标识符命名规则
# 2、包名区分大小写（建议全部使用小写字母）
# 3、不要与标准库包同名

# 1、import 包名.模块名
# import trade.order
# import trade.pay

# trade.order.create_order()
# trade.pay.wechat_pay()


# 2、 import 包名.模块名 as 别名
# import trade.order as td
# import trade.pay as tp
#
# td.create_order()
# tp.wechat_pay()

# 3、from 包名.模块名 import 具体内容1，具体内容2,.....    (引入部分内容)
# from trade.order import max_order_amount,create_order
# from trade.pay import timeout,wechat_pay

# print(max_order_amount)
# wechat_pay()

# 4、from 包名.模块名 import 具体内容1 as 别名，具体内容2 as 别名,.....
# from trade.order import max_order_amount as max_od
# from trade.pay import wechat_pay as wp
# print(max_od)
# wp()


# 5、from 包名.模块名 import *  (不推荐这么写)
# from trade.order import *
# from trade.pay import *

# print(timeout)
# print(max_order_amount)

# 6、from 包名 import 模块名
# from trade import order, pay

# order.create_order()
# pay.wechat_pay()

# 7、from 包名 import 模块名 as 别名
# from trade import order as od, pay as p

# od.create_order()
# p.wechat_pay()

# 关于__init__.py文件：
# 1、__init__.py 是包的初始化文件，在包被导入时，__init__.py会被自动调用
# 2、__init__.py 中可以编写一个包的初始化逻辑
# 3、__init__.py 中所定义的内容 会被 【from 包名 import *】 形式全部引入
# 4、__init__.py 中也可以使用__all__ 来控制保重的那些模块可以被 【from 包名 import *】引入

# 8、from 包名 import *
# from trade import *
# print(order.max_order_amount)

# 9、import 包名
# import trade
# trade.order.create_order()

# 测试引入子包
from trade.hello.h1 import say_hello
say_hello()










