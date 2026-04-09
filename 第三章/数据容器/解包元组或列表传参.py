
# 定义函数时，使用*args 将收到的多个参数打包成一个元组
def test(*args):
    print(f'收到的参数是：{args},参数类型是：{type(args)}')

tuple1 = ('你好','hello')
# 函数调用时，使用*对 列表/元组 进行解包后，在传递参数
test(tuple1)  # 这种写法相当于 test('你好','hello')