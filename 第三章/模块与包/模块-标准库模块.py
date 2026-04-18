#标准库模块：随着Python一起安装在我们电脑上的那些模块
# 有一些标准库模块是用c语言实现的，这些用c语言实现的模块，又称：内置模块

import copy    # 拷贝对象(深拷贝、浅拷贝)
import os      # 操作系统相关操作(文件、文件夹、路径系统层面的操作)
import random  # 随机数相关(生成随机数、随机选择、洗牌)
# 以下模块是内置模块
import time    # 时间相关操作(获取时间、延时、格式化时间等)
import math    # 数学相关
import sys     # Python解释器相关操作

# 创建一个文件夹
# os.mkdir('demo')

# 随机选择一个人
names = ['张三','李四','王五']
print(random.choice(names))

# 洗牌
names = ['张三','李四','王五']
random.shuffle(names)
print(names)

# 休眠
# time.sleep(2)
# print('ok')

# 获取当前时间
print(time.strftime('%H:%M:%S'))
print(time.strftime('%p %I:%M:%S'))

# 开平方
print(math.sqrt(4))
# 取绝对值
print(math.fabs(-11))

# 获取python解释器的版本
print(sys.version)

