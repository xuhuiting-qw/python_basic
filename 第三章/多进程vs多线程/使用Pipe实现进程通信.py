
from multiprocessing import Process,Pipe

def test1(con1):
    data = con1.recv()
    print(f'我是test1接收了{data}')

def test2(con2):
    con2.send(100)
    print(f'我是test2发送100')

if __name__ == '__main__':

    # duplex=False  管道是单向的，con1只能接收，con2只能发送
    con1,con2 = Pipe(duplex=False)

    p1 = Process(target=test1,args=(con1,))
    p2 = Process(target=test2,args=(con2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
