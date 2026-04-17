
# 无论是否发生异常，try-except 后面的代码都会继续执行
# 直接写except 会捕获到python中所有的异常---实际开发中不会这样做
# print('欢迎使用本程序')
# try:
#     a = int(input('请输入第一个数:'))
#     b = int(input('请输入二个数:'))
#     result = a / b
#     print(f'{a}除以{b}的结果是{result}')
# except:
#     print('程序出现异常')
# print('*****后续处理逻辑******')

# 异常处理（捕获指定的类型的异常）
# 多个 except  从上往下匹配，匹配成功后不再向下匹配
# 获取异常的具体信息
# print('欢迎使用本程序')
# try:
#     print(x)
#     a = int(input('请输入第一个数:'))
#     b = int(input('请输入二个数:'))
#     result = a / b
#     print(f'{a}除以{b}的结果是{result}')
# except ZeroDivisionError:
#     print('程序出现异常: 0不能作为除数')
# except ValueError as v:
#     print('程序出现异常: 输入的必须是数字')
# except Exception as e:
#     print('异常信息：',e)
#     print('异常类型：',type(e))
#     print('异常参数：',e.args)
#     print('异常文件：',e.__traceback__.tb_frame.f_code.co_filename)
#     print('异常的具体行为:',e.__traceback__.tb_lineno)
#     # 通过 traceback 来回溯异常
#     # import traceback
#     # print(traceback.format_exc())
# print('*****后续处理逻辑******')


# 一个except 也可以捕获不同的异常
# print('欢迎使用本程序')
# try:
#     print(x)
#     a = int(input('请输入第一个数:'))
#     b = int(input('请输入二个数:'))
#     result = a / b
#     print(f'{a}除以{b}的结果是{result}')
# except (ZeroDivisionError,ValueError,Exception) as e:
#     if isinstance(e,ZeroDivisionError):
#         print('程序出现异常: 0不能作为除数')
#     elif isinstance(e,ValueError):
#         print('程序出现异常: 输入的必须是数字')
#     else:
#         print('异常信息：', e)
# print('*****后续处理逻辑******')

# 完整写法
# 1、try       : 尝试去做可能会出现异常的事情
# 2、except    : 出现异常时的处理(出现异常时怎么补救)
# 3、else      : 如果一切顺利(没有异常出现)要做的事
# 4、finally   : 无论有没有异常，都要做的事
print('欢迎使用本程序')
try:
    a = int(input('请输入第一个数:'))
    b = int(input('请输入二个数:'))
    result = a / b
    print(f'{a}除以{b}的结果是{result}')
except (ZeroDivisionError,ValueError,Exception) as e:
    if isinstance(e,ZeroDivisionError):
        print('程序出现异常: 0不能作为除数')
    elif isinstance(e,ValueError):
        print('程序出现异常: 输入的必须是数字')
    else:
        print('异常信息：', e)
else:
    print('代码一切顺利')
finally:
    print('无论有没有异常，都要做的事')
print('*****后续处理逻辑******')



