# join 方法的作用：阻塞当前进程，等join前面的进程执行完，再继续往下执行
# join(timeout)，其中timeout是可选参数，表示等多久，单位是秒

# 注意点：
# 1、p.join() 不是让进程p 等，而是让 执行这行join代码的那个进程 去等，等的是p这个进程
# 2、当达到了timeout所指定的时间后，进程并不会终止，只是不再等了
# 3、join 必须在start之后

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
if __name__ == '__main__':
    print('我是主进程的第一行')
    p1 = Process(target=speak)
    p2 = Process(target=study)

    p1.start()
    # 让主进程等 5s 再继续执行
    p1.join(5)
    p2.start()

    # p1.join()  # 让主进程等 p1进程 执行完毕后，主进程再继续执行
    # p2.join()  # 让主进程等 p2进程 执行完毕后，主进程再继续执行
    print('我是主进程的最后一行')





