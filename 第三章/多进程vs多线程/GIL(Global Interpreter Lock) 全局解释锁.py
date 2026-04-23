# 一、关于GIL(Global Interpreter Lock)
# 1、GIL锁是 CPython 解释器中的一把互斥锁
# 2、GIL锁的作用是：无论cpu有多少个核心，在某一时刻，只允许同一个进程中的线程去执行Python代码

# 二、结论：CPython 解释器中的多线程模型，本质上是并发，不是并行

# 三、为何要这样设计------为了确保解释器级别的数据安全

# GIL锁和编码时使用的Lock 和 RLock不是同一种东西
# Lock 和  RLock 是业务层面的锁，目标：让业务逻辑不要出错

import os
import time
from threading import RLock,Thread,current_thread
from concurrent.futures import  ThreadPoolExecutor,as_completed


# RLock 示例1
# def speak(lock):
#     for index in range(10):
#         # 上锁:如果锁是空闲的，立刻上锁，继续往下执行，如果锁被别人拿着，当前进程会阻塞等待（原地）
#         lock.acquire()
#         print('好好',end='')
#         print('学习',end='')
#         print('天天',end='')
#         print('向上')
#         # 释放锁：acquire 和 release 必须成对出现，否则会永远卡住（死等）
#         lock.release()
#         time.sleep(1)
#
# def study(lock):
#     for index in range(15):
#         # with lock :会自动完成两件事
#         #       1、进入前：自动执行 lock.acquire() 上锁
#         #       2、离开后：自动执行 lock.release()  释放锁
#         # 好处：即便代码块发生异常，也能保证释放锁，避免“卡死”
#         # RLock 可以多次上锁
#         with lock:
#             print('A', end='')
#             print('B', end='')
#             print('C', end='')
#             print('D')
#         time.sleep(1)
#
# # 要一边说话一边学习
# if __name__ == '__main__':
#     lock = RLock()
#     p1 = Thread(target=speak,args=(lock,))
#     p2 = Thread(target=study,args=(lock,))
#
#     p1.start()
#     p2.start()


# RLock 示例2：不要让两个窗口卖出同一张票
cur = 1

def sale(lock):
    global cur
    while True:
        with lock:
            if cur <= 20:
                print(f'{current_thread().name}出售了第{cur}张票')
                cur += 1
            else:
                print('票已售空')
                break


if __name__ == '__main__':

    lock  = RLock()
    t1 = Thread(target=sale,name='窗口1',args=(lock,))
    t2 = Thread(target=sale,name='窗口2',args=(lock,))
    t3 = Thread(target=sale,name='窗口3',args=(lock,))

    t1.start()
    t2.start()
    t3.start()









