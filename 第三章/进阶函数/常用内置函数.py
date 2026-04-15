import time

# 一、输入与输出
# 1、输出指定内容  print()
# 完整参数  print(*objects,sep=' ',end='\n',file=sys.stdout,flush = False)
# 参数详解：
# 1.objects：要输出的内容
# 2.sep：分隔符
# 3.end: 结束符
# 4.file 输出位置
# 5.flush ： 是否立即刷新
print(10, 23, 11, sep='--', end='!')
# 打印到了当前目录的 a.txt文件里面
f = open('a.txt', 'w', encoding='utf-8')
print("hello", file=f)
print()

# 第一种进度条
print('加载中',end='',flush=True)
for n in range(8):
    print('.',end='',flush=True)
    time.sleep(1)
print('完成',end='',flush=True)
# 第二种进度条
for index in range(101):
    print(f'\r已加载{index}%',end='')
    time.sleep(0.1)
print()
# 2、获取用户输入  input()

# 二、类型转换
# int()   转为整数
# float()  转为浮点数
# str()   转为字符串
# bool()  转为布尔值
# list()   转为列表
# tuple()  转为元组
# set()    转为集合
# dict()   转为字典

# 三、数学相关
# abs()    取绝对值
print(abs(-1.2))
print()
# round()   四舍五入  银行家舍入法:小于5舍,大于5入,等于5看奇偶(奇入偶舍)
print(round(5.5))
print(round(4.5))
# 保留两位小数
print(round(7.235, 2))
print()
# pow()  次方
print(pow(2,3))  # 2的3次方
print(pow(2,3,5))  # 2的3次方 对5取模
print()
# divmod()  商和余数
print(divmod(10,3))
# max()   最大值
# min()  最小值
# sum()   求和
# map()   加成一组数据
# filter()  按条件过滤数据(支持key函数)
# reduce()  合并计算
# sorted()  排序(支持key函数)

# 四、数据容器相关
# len()  获取容器元素个数
# range()  生成一个数字序列(支持步长)
# enumerate()    给序列添加索引
# zip()     将多个序列一一配对
names = ['张三', '李四', '王五']
scores = [90, 80, 88]
result = list(zip(names,scores))
print(result)

# 五 类型判断与对象相关
# type()   查看类型
# isinstance()  判断类型
# issubclass()  判断两个类的继承关系
# id()        查看对象内存地址

# 六 逻辑判断相关
# all()   全为真返回True
l1 = [10,0,20,30]
print(all(l1))
# any()   有一个为真即可
print(any(l1))

# 七 字符串辅助相关
# ord()   获取字符的Unicode编码
# chr()   将Unicode编码转为字符



