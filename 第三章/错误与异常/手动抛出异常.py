
# 当程序遇到不符合预期情况时，可以使用 raise 语句手动触发(抛出)异常

print('欢迎使用年龄判断系统')
try:
    age = int(input('请输入你的年龄：'))
    if 18 <= age <= 120:
        print('成年')
    elif 0 <= age < 18:
        print('未成年')
    else:
        # print('输入年龄有误')
        raise ValueError('输入年龄有误，需要0~120的整数')
except Exception as e:
    print('异常信息',e)

