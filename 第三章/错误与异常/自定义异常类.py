# 1、由开发人员自己定义一个异常类，用来表示代码中 “更具体、更有业务含义”的异常
# 2、具体规则: 定义一个类(类名通常以Error结尾)，继承Exception 类或它的子类

class SchoolNameError(Exception):
    def __init__(self,msg):
        super().__init__('校名异常' + msg)


def school_len(name):
    if len(name) >10:
        raise SchoolNameError('长度过长')
    else:
        print('是合法的')

try:
    school_len('12345678910')
except SchoolNameError as e:
    print(f'程序异常:{e}')
