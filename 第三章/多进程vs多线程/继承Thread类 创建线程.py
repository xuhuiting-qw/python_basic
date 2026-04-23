from threading import Thread,RLock,get_native_id
import os,time

class SpeakThread(Thread):
    def __init__(self,a,lock,**kwargs):
        super().__init__(**kwargs)
        self.a = a
        self.lock = lock


    def run(self):
        for index in range(5):
            with self.lock:
                print(f'{self.a}我在说话{index},进程是{os.getpid()},线程是{get_native_id()}')
            time.sleep(1)

class StudyThread(Thread):
    def __init__(self,lock):
        super().__init__()
        self.lock = lock

    def run(self):
        for index in range(5):
            with lock:
                print(f'我在学习{index},进程是{os.getpid()},线程是{get_native_id()}')
            time.sleep(1)

if __name__ == '__main__':
    print('我是主进程的第一行')

    lock = RLock()
    t1 = SpeakThread(100,lock)
    t2 = StudyThread(lock)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('我是主进程的最后一行')
