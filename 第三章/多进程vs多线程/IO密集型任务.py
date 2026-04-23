# CPU密集型任务，更适合用多线程
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


# 拷贝文件
def copy_file(index):
    with open('log.txt','rt') as src,open(f'a_副本{index}.txt','wt') as dst:
        while True:
            data = src.readline()
            if not data:
                break
            dst.write(data)

if __name__ == '__main__':
    print('-------多进程完成任务-------')
    start = time.time()
    with ProcessPoolExecutor(4) as executor:
        list(executor.map(copy_file, [1]))
    end = time.time() - start
    print(f'多进程总耗时：{end}秒 \n')

    print('-------多线程完成任务-------')
    start = time.time()
    with ThreadPoolExecutor(4) as executor:
        list(executor.map(copy_file, [2]))
    end = time.time() - start
    print(f'多线程总耗时：{end}秒 \n')