# Python中操作文件的标准流程：
# 1、创建 文件对象
# 2、操作文件（读取、写入等）
# 3、关闭文件

# 文件操作的核心 ---- open函数：它可以打开或者创建文件，且支持多种操作模式，返回值是 文件对象
# open函数最常用的三个参数如下：
# 1、file  要操作的文件路径
# 2、mode  文件的打开模式
# r     读取（默认值）
# w     写入、并先截断文件
# x     排它性创建，如果文件已存在，则创建失败
# a     打开文件用于写入，如果文件存在，则在文件末尾追加内容
# b     二进制模式
# t     文本模式（默认值）
# +     打开用于更新（读取与写入）
# 3、encoding  字符编码

# 读取操作1、使用文件对象的read方法，读取文件中的内容
# read方法说明：
# 1、read(size) 中的size是可选参数
#     若不传递size参数，表示：读取文件中所有的内容(注意内存占用)
#     若传递size参数，表示：读取文件中指定个数的字符，或指定大小的字节
# 2、read会从上一次read的位置继续读取（指针思想），若到达文件末尾后继续读取，将返回空字符串

# region Description
# 1、创建 文件对象
# file = open(file='a.txt',mode='rt',encoding='utf-8')
# file = open('a.txt','rt',encoding='utf-8')
# file = open('F:\\demo01.txt','rt',encoding='utf-8')
# file = open('F:/demo01.txt','rt',encoding='utf-8')
# file = open('C:\\Users\\34911\\Pictures\\Screenshots\\屏幕截图 2025-03-01 205421.png','rb')
# 2、操作文件（读取）
# 多次调用read去逐步读取文件
# result = file.read(2)
# result1 = file.read(3)
# result2 = file.read(5)
# print(result,end='')
# print(result1,end='')
# print(result2)

# 用循环配合多次read（对内存友好）
# while True:
#     result = file.read(10)
#     if result == '':
#         break
#     print(result,end='')
# 3、关闭文件
# file.close()
# endregion

# 读取操作2、使用文件对象的readline方法，读取文件中的一行
# readline 方法说明：
# 1、readline(size) 中的size是可选参数
#       若不传递 size 参数，表示：读取当前这一行所有的内容
#       若传递 size 参数，表示：读取当前行时，最多能读取的字符数，或字节数（size不是行数）
# 2、readline 方法，也是从上一次位置继续获取，若到达文件末尾后继续读取，也是返回空字符串

# region Description
# 1、创建 文件对象
# file = open('a.txt','rt',encoding='utf-8')
# 2、操作文件（读取）
# 依次调用readline逐行读取
# res1 = file.readline()
# res2 = file.readline()
# res3 = file.readline()
# res4 = file.readline()
# print(res1.strip())
# print(res2.strip())
# print(res3.strip())
# print(res4.strip())

# 通过循环配合readline逐行读取
# while True:
#     line = file.readline()
#     if line == '':
#         break
#     print(line.strip())
    # print(line,end='')
# 3、关闭文件
# file.close()
# endregion


# 读取操作3、使用for循环直接遍历文件对象
# region Description
# 1、创建 文件对象
# file = open('a.txt','rt',encoding='utf-8')
# 2、操作文件（读取）
# for line in file:
#     print(line.strip())
# 3、关闭文件
# file.close()
# endregion

# 读取操作4、使用文件对象的 readlines 方法,一次性按“行”读完，返回一个列表
# readlines 方法说明：
# 1、readlines(hint) 中的hint是可选参数
#       若不传递 hint 参数，表示：读取当前文件的所有行
#       若传递了hint 参数，表示：期望读取的 字符个数或字节数的上限 （hint不是行数）
# 2、注意：由于readlines是一次性读取文件的所有内容，所以不适合读取体积较大的文件

# region Description
# 1、创建 文件对象
# file = open('a.txt','rt',encoding='utf-8')
# 2、操作文件（读取）
# print(file.readlines())
# 3、关闭文件
# file.close()
# endregion

# 最佳实践：使用 with 上下文管理器，结合for循环遍历，逐行读取文件
with open('a.txt','rt',encoding='utf-8') as file:
    for line in file:
        print(line.strip())
