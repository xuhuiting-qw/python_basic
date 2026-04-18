# 支付超时时间
timeout = 1800

# 微信支付
def wechat_pay():
    print('微信支付')

# 支付宝支付
def ali_pay():
    print('支付宝支付')

# 提示函数
def show_info():
    print('我是支付模块的提示！')

# print('我是pay模块打印的内容',__name__)

# 测试代码
if __name__ == '__main__':
    # 如果主程序不是这个pay文件，那么下面执行代码不会触发
    wechat_pay()
    print()