import os
import time
from concurrent.futures import  ThreadPoolExecutor,as_completed
from threading import get_native_id,RLock

# 1、创建 线程池执行器 ，使用submit方法提交任务，使用shutdown方法等待任务完成
# def work(n,lock):
#     with lock:
#         print(f'work正在执行任务{n}--------{get_native_id()}')
#     time.sleep(1)
#
# if __name__ == '__main__':
#     print('-----------start-----------')
#     # 创建一个线程池执行器
#     executor = ThreadPoolExecutor(3)
#     lock = RLock()
#     # 使用 submit 方法 提交任务（submit只负责提交任务，不会阻塞主线程）
#     executor.submit(work,1,lock)
#     executor.submit(work,2,lock)
#     executor.submit(work,3,lock)
#     executor.submit(work,4,lock)
#     executor.submit(work,5,lock)
#     executor.submit(work,6,lock)
#     executor.submit(work,7,lock)
#
#     # shutdown 的作用：不再接收新的任务
#     # wait = True 的作用是：阻塞主线程，等待线程池中所有任务执行完毕
#     executor.shutdown(wait=True)
#
#     print('-----------end-----------')

# 2、获取子线程执行后的返回结果(Future类的实例对象 + result方法)
# def work(n,lock):
#     with lock:
#         print(f'work正在执行任务{n}--------{get_native_id()}')
#     time.sleep(1)
#     return f'我是任务{n}的结果'
#
# if __name__ == '__main__':
#     print('-----------start-----------')
#     # 创建一个线程池执行器
#     executor = ThreadPoolExecutor(3)
#     lock = RLock()
#     futures = [executor.submit(work,n,lock) for n in range(1,8)]
#     # 阻塞主线程，等待线程池中所有任务执行完毕
#     executor.shutdown(wait=True)
#
#     for n in futures:
#         print(n.result())
#
#     print('-----------end-----------')

# 3、使用as_completed: 按 完成顺序 获取结果
# def work(n,lock):
#     with lock:
#         print(f'work正在执行任务{n}--------{get_native_id()}')
#     if n==1:
#         time.sleep(10)
#     time.sleep(1)
#     return f'我是任务{n}的结果'
#
# if __name__ == '__main__':
#     print('-----------start-----------')
#     # 创建一个线程池执行器
#     executor = ThreadPoolExecutor(3)
#     lock = RLock()
#     futures = [executor.submit(work,n,lock) for n in range(1,8)]
#
#     # 准备一个 result_list 去收集任务的具体结果
#     result_list = []
#
#     for n in as_completed(futures):
#         result_list.append(n.result())
#
#     # 阻塞主线程，等待线程池中所有任务执行完毕
#     executor.shutdown(wait=True)
#     # 打印最终的结果
#     print(result_list)
#     print('-----------end-----------')

# 4、使用 add_done_callback 方法，为任务添加完成时的回调函数
# def work(n,lock):
#     with lock:
#         print(f'work正在执行任务{n}--------{get_native_id()}')
#     if n==1:
#         time.sleep(10)
#     time.sleep(1)
#     return f'我是任务{n}的结果'
#
# if __name__ == '__main__':
#     print('-----------start-----------')
#     # 创建一个线程池执行器
#     executor = ThreadPoolExecutor(3)
#
#     result_list = []
#     # 任务完成后的回调函数
#     def done_func(future):
#         result_list.append(future.result())
#
#     lock = RLock()
#     # 开启8个任务，并指定回调函数
#     for n in range(8):
#         f = executor.submit(work,n,lock)
#         f.add_done_callback(done_func)
#
#     # 阻塞主线程，等待线程池中所有任务执行完毕
#     executor.shutdown(wait=True)
#     # 打印最终结果，按照“完成的顺序”获取
#     print(result_list)
#     print('-----------end-----------')



# 5、使用map方法批量提交任务（注意：map方法是阻塞的，并且得到结果的顺序，与任务分配的顺序是一致的）
# def work(n,lock):
#     with lock:
#         print(f'work正在执行任务{n}--------{get_native_id()}')
#     time.sleep(1)
#     return f'我是任务{n}的结果'
#
# if __name__ == '__main__':
#     print('-----------start-----------')
#     # 创建一个线程池执行器
#     executor = ThreadPoolExecutor(3)
#     lock = RLock()
#     # 通过map方法批量提交任务(结果按照提交的顺序来)
#     results = executor.map(work,[1,2,3,4,5,6,7],[lock]*7)
#     # 获取 results 生成器中的内容 是阻塞的
#     print(list(results))
#
#     executor.shutdown(wait=False)
#     print('-----------end-----------')

# 6、使用with ： 线程池的“自动回收”的写法，离开with 代码块时自动执行 shutdown(wait=True)
def work(n,lock):
    with lock:
        print(f'work正在执行任务{n}--------{get_native_id()}')
    time.sleep(1)
    return f'我是任务{n}的结果'

if __name__ == '__main__':
    print('-----------start-----------')
    # 创建一个线程池执行器
    # executor = ProcessPoolExecutor(3)
    lock = RLock()
    with ThreadPoolExecutor(3) as executor:
        # 通过map方法批量提交任务(结果按照提交的顺序来)
        results = executor.map(work, [1, 2, 3, 4, 5, 6, 7],[lock]*7)
        # 获取 results 生成器中的内容 是阻塞的
        print(list(results))

    print('-----------end-----------')














