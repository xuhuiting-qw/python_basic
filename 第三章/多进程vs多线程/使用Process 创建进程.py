import os
import time
from multiprocessing import Process

# 定义一个 speak 函数，功能是：每隔1s说话一次（一共说话10次）
def speak():
    for index in range(10):
        print(f'我在说话{index},进程的pid是：{os.getpid()}')
        time.sleep(1)


# 定义一个 study 函数，功能是：每隔1s学习一次（一共学习15次）
def study():
    for index in range(15):
        print(f'我在学习{index},进程的pid是：{os.getpid()}')
        time.sleep(1)

# 要一边说话一边学习
# 注意：一定要写 if __name__ == '__main__' 这个判断：原因如下：
# 1、当创建子进程时，python并不会把父进程内存里面的speak函数直接交给子进程
# 2、python会启动一个全新的python解释器进程，重新执行当前的.py文件（作为模块）
# 3、在执行过程中，重新定义出一个speak函数，交给子进程
if __name__ == '__main__':
    # 创建两个 Process 类的实例对象（进程对象）
    # 注意点；1、p1、p2 就对应着以后的两个子进程，在创建它们的时候，就要指定好他们要执行的任务
    #       2、此时的p1、p2只是代码层面的两个进程对象，操作系统还没有真的创建p1、p2 两个进程

    p1 = Process(target=speak)
    p2 = Process(target=study)
    # 调用进程对象的start方法，会立刻向操作系统申请一个进程，并且会将该进程交由操作系统进行调度

    p1.start()
    p2.start()





