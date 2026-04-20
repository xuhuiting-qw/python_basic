import os
import time
from multiprocessing import Process,current_process

def speak(a,b,name):
    for index in range(3):
        print(f'{name}-----{a}---{b}---我是一个{current_process().name}进程，我在说话{index},进程的pid是：{os.getpid()}')
        time.sleep(1)

def study():
    for index in range(3):
        print(f'我在学习{index},进程的pid是：{os.getpid()}')
        time.sleep(1)

# 要一边说话一边学习
if __name__ == '__main__':
    # Process的参数：
    #      group ： 默认值为None（应当始终为None）
    #      target:  子进程要执行的可调用对象，默认值为None
    #      name:   进程名称，默认为None，如果设置为None，Python会自动分配名称
    #      args：   给target传的位置参数（元组）
    #      kwargs： 给target传的关键字参数（字典）
    #      daemon： 标记进程是否为守护进程，取值为布尔值（默认为None，表示从创建方进程继承）
    p1 = Process(target=speak,args=(66,88),kwargs={'name':'张三'})
    p2 = Process(target=study,name = '我是一个学习进程')
    print(p2.name)
    p1.start()
    p2.start()





