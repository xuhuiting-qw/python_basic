# 守护进程：一种依附于主进程存在的子进程，一旦主进程结束，它就会被自动终止（主进程一死，守护进程必须跟着死）

# 守护进程的使用场景：
# 1、后台监控类任务
# 2、日志、统计、采样任务
# 3、辅助型“陪跑任务”

# 注意点：
# 1、守护进程必须是子进程
# 2、主进程结束，守护进程也会随之结束
# 3、守护进程中，不允许再创建新的子进程
# 4、必须在 start 之前，start() 之后，不能再设置daemon

import os
import time
from multiprocessing import Process

def monitor():
    while True:
        try:
            with open('log.txt', 'r', encoding='utf-8') as file1:
                lines = sum(1 for _ in file1)
                # lines = file1.readlines()
        except FileNotFoundError:
            lines = 0
        print(f'我是守护进程{os.getpid()}，log.txt共有{lines}行')
        time.sleep(1)

if __name__ == '__main__':
    print(f'我是主进程{os.getpid()}中的第一行代码')

    p1 = Process(target=monitor,daemon=True)
    p1.start()

    # 向文件中写入数据
    with open('log.txt','a',encoding='utf-8') as file:
        for index in range(10):
            file.write(f'你好{index}\n')
            # 让缓冲区的东西，立马写入文件中
            file.flush()
            time.sleep(1)
    print(f'我是主进程{os.getpid()}中的最后一行代码')