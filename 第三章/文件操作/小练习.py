import os.path
import time

# 练习1、将一个二进制文件复制到指定位置
source = 'img.jpg'
target = 'F:/demo'

# 如果目标目录不存在，就是创建一个
# if not os.path.isdir(target):
#     os.makedirs(target)
#
# with open(source,'rb') as file1,open(target + '/' + source,'wb') as file2:
#     while True:
#         data = file1.read(1024)
#         if not data:
#             break
#         file2.write(data)
#     print('复制完毕')

# 练习2：日志记录
#  1、用户输入用户名和密码后，程序进行校验
#  2、用户名不存在，提示“用户名未注册”，并记录日志
#  3、用户名存在，但密码错误，提示“密码错误”，并记录日志
#  4、用户名和密码均正确，提示“登录成功”，并记录日志

user = {
    '张三':'1234',
    '李四':'8888',
    '王五':'45678',
}
# 提示输入信息
username = input('请输入用户名：')
password = input('请输入密码：')

now = time.strftime('%Y-%m-%d %H:%M:%S')

if username not in user:
    print('用户名未注册')
    with open('log.txt','at',encoding='utf-8') as file:
        file.write(f'{now} :  {username},用户名未注册 \n')
elif user[username] != password:
    print('密码错误')
    with open('log.txt','at',encoding='utf-8') as file:
        file.write(f'{now} :  {username},密码错误 \n')
else :
    print('登录成功')
    with open('log.txt', 'at+', encoding='utf-8') as file:
        file.write(f'{now} :  {username},登录成功 \n')




