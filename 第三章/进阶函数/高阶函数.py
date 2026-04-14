
# 高阶函数：一个函数的参数是函数或者返回值是函数时，那么该函数就是高阶函数

# 1、代码的复用性高：可以把行为“独立出去”，传入不同函数实现不同逻辑
# 2、能让函数更加灵活、更加通用
# 3、高阶函数：是装饰器、闭包的基础

def info(msg):
    return '【提示】：'+msg
def warn(msg):
    return '【警告】：'+msg
def error(msg):
    return '【错误】：'+msg
# 参数为函数----高阶函数
def log(func,text):
    print(func(text))
log(info,'保存成功')
log(warn,'空间不足')
log(error,'保存错误')
