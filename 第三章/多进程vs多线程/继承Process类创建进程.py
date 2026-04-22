from multiprocessing import Process
import os,time

class SpeakProcess(Process):
    def __init__(self,a):
        super().__init__()
        self.a = a


    def run(self):
        for index in range(10):
            print(f'{self.a}我在说话{index},进程是{os.getpid()},我的父进程是{os.getppid()}')
            time.sleep(1)

class StudyProcess(Process):
    def run(self):
        for index in range(15):
            print(f'我在学习{index},进程是{os.getpid()},我的父进程是{os.getppid()}')
            time.sleep(1)

if __name__ == '__main__':
    print('我是主进程的第一行')
    p1 = SpeakProcess(100)
    p2 = StudyProcess()

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('我是主进程的最后一行')
