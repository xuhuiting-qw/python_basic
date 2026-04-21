# 进程之间不共享内容，因此也就不共享任何变量

from multiprocessing import Process

num = 100
def test1():
    global num
    num +=10
    print(f'我是test1进程,操作之后的num是{num}')

def test2():
    global num
    num -=10
    print(f'我是test2进程,操作之后的num是{num}')

if __name__ == '__main__':
    print('我是主进程的第一行代码')

    p1 = Process(target=test1)
    p2 = Process(target=test2)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('我是主进程的最后一行代码',num)