# 并发编程1
import random
import time
from concurrent.futures import ThreadPoolExecutor
from threading import Thread

def download(*args, **kwargs):
    start = time.time()
    print('开始下载')
    time.sleep(random.randint(1, 3))
    print('下载完成')
    print(f'{kwargs["filename"]}下载耗时: {time.time() - start :.2f}\n')

class DownloadThread(Thread):

    def __init__(self, filename):
        self.filename = filename
        super().__init__()

    def run(self):
        start = time.time()
        print(f'开始下载{self.filename}')
        time.sleep(random.randint(1, 3))
        print(f'{self.filename}下载完成')
        print(f'{self.filename}下载耗时: {time.time() - start :.2f}')


def serial_main1():
    start = time.time()
    download(filename="并发入门.pdf")
    download(filename="并发编程.pdf")
    download(filename="并发编程2.pdf")
    print(f'所有文件下载完成耗时: {time.time() - start :.4f}\n')

def concurrent_main1():
    threads = [
        Thread(target=download, kwargs={'filename': '并发入门.pdf'}),
        Thread(target=download, kwargs={'filename': '并发编程.pdf'}),
        Thread(target=download, kwargs={'filename': '并发编程2.pdf'}),
    ]
    start = time.time()
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print(f'所有文件下载完成耗时: {time.time() - start :.4f}\n')

def concurrent_main2():
    threads = [
        DownloadThread('并发入门.pdf'),
        DownloadThread('并发编程.pdf'),
        DownloadThread('并发编程2.pdf'),
    ]
    start = time.time()
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print(f'所有文件下载完成耗时: {time.time() - start :.4f}\n')

# 使用线程池
def ThreadPool_main1():
    start = time.time()
    with ThreadPoolExecutor(max_workers=3) as executor:
        filename = ['并发入门.pdf', '并发编程.pdf', '并发编程2.pdf']
        for filename in filename:
            executor.submit(download, filename=filename)
    print(f'所有文件下载完成耗时: {time.time() - start :.4f}\n')

# 守护线程 跟随主线程结束，并非与子线程关联
def display(connect):
    while True:
        print(connect, end=' ', flush=True)
        time.sleep(random.randint(1, 3))

def ThreadPool_main2():
    Thread(target=display, args=('并发入门',)).start()
    Thread(target=display, args=('并发编程',)).start()

def ThreadPool_main3():
    start = time.time()
    # Thread(target=display, args=('并发入门',), daemon=True).start()
    Thread(target=display, args=('并发入门',)).start()

    # Thread(target=display, args=('并发编程',), daemon=True).start()
    Thread(target=display, args=('并发编程',)).start()
    print(f'所有文件下载完成耗时: {time.time() - start :.4f}\n')
    time.sleep(5)

# 创建进程
from multiprocessing import Process,current_process

def sub_task(content,nums):
    # 通过current_process()获取当前进程对象
    print(f'PID: {current_process().pid}')
    # 通过进程对象进程的id和name属性获取进程的id和name
    print(f'name: {current_process().name}')

    # 每个进程都有自己的nums列表，进程之间的不共享内存
    # 在创建子进程时复制父进程的数据结构，三个进程从列表中pop（0）得到的值都是20
    counter,total = 0, nums.pop(0)
    print(f'loop count: {total}')
    time.sleep(1)
    while counter < total:
        counter += 1
        print(f'{content}：{counter}')
        time.sleep(0.5)

def sub_main():
    nums = [20,30,40]
    # 创建启动进程
    Process(target=sub_task, args=('并发入门',nums,)).start()
    Process(target=sub_task, args=('并发编程',nums,)).start()
    Process(target=sub_task, args=('并发编程2',nums,)).start()
    # 主程序进行时执行subtask函数
    sub_task('并发入坟',nums)


"""
    多线程与多进程的比较
        i/o 密集型任务 多线程 > 多进程
        计算密集型任务 多进程 > 多线程
"""
# 多线程版计算任务
import concurrent.futures
PRIMES = [
    1231413231,
    122133242,
    5345323245,
    324335536,
    3455467343,
    324335536,
    5876546657,
    43839473,
    898896786,
    63675455,
    7249583586946759,
    78346245304532
] * 5

def is_prime(n):
    """
        判断n是否为素数
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def MultithreadedComputing():
    """
        多线程版计算任务
    """
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
        for number,prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print(f'{number}是否为素数: {prime}')
            # print(f'{number}是否为素数: {prime}',flush=True)

    print(f'所有素数计算耗时: {time.time() - start :.4f}\n',) # 27.7547301 27.3058
    # print(f'所有素数计算耗时: {time.time() - start :.4f}\n',flush=True) # 28.1818928 28.2325

# 多进程版计算任务
def MultiprocessComputing():
    """
        多进程版计算任务
    """
    start = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=16) as executor:
        for number,prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print(f'{number}是否为素数: {prime}')

    print(f'所有素数计算耗时: {time.time() - start :.4f}\n',flush=True) # 8.2061 7.832366


"""
    进程间通信
        队列      使用multiprocessing.Queue()创建队列,可以被多个进程共享的队列，
                    底层是通过操作系统底层的管道和信号量（semaphore）实现的
"""
from multiprocessing import Queue, Process
import time

def counter_task(content,queue):
    """
        计数任务
    """
    counter = queue.get() # get 会阻塞等待队列有数据可取，可以指定Block和timeout参数，进行超时处理
    while counter < 50:
        print(f'{content}：{counter}',end=' ',flush=True)
        counter += 1
        queue.put(counter)
        time.sleep(0.01)
        counter = queue.get()

def MultiprocessCommunication():
    queue = Queue()
    queue.put(0)
    p1 = Process(target=counter_task, args=('并发入门',queue,))
    p1.start()

    p2 = Process(target=counter_task, args=('并发编程',queue,))
    p2.start()

    while p1.is_alive() and p2.is_alive():
        pass
    print(f'所有进程完成:{queue.put(50)}')

"""
总结
    以下情况时，应多考虑多线程：
        1.程序需要维护更多的共享状态（尤其状态可变时），python的列表、字典、集合都是线程安全的
            （多线程同时操作一个列表、字典或者集合，不会导致数据不一致），所以使用线程而非进程维护共享状态代价相较较小。
        2.程序会花费大量时间在 I/O 操作上，没有太多并行计算的需求并且不需要占用太多内存
    
    以下情况时，需要多考虑多进程：
        1.程序执行密集型计算任务，像，音视频解码、数据压缩、科学计算等等
        2.程序的输入可以并行分块，并且运算结果可以合并。
        3.程序在内存使用方面没有限制并且不强依赖I/O操作(入，文件读写，套接字等等）
"""


"""
    这种异步了解思想即可
    3.5版本引入并在3.7成为关键字的 async/await 语法
"""
# 生成器和协程
def fib1(int):
    """ 生成器 """
    a, b = 0, 1
    for _ in range(100):
        yield a
        a, b = b, a+b

def fib_main():
    gen_obj = fib1(1)
    print(gen_obj)

    for value in gen_obj:
        print(value)

# 协程
def clac_average():
    """ 协程 """
    total = 0
    count = 0
    average = None
    # 初始化协程
    while True:
        number = yield average
        total += number
        count += 1
        average = total / count

def coordinate_the_process_main():
    """ 协程的使用场景 """
    average_obj = clac_average()
    average_obj.send(None)
    for _ in range(50):
        print(f'{average_obj.send(float(input())):.4f}')


# async await 语法

# 同步
import time
def display1(num):
    time.sleep(1)
    print('hello world',num)
def sync_main():
    start = time.time()
    for i in range(1,10):
        display1(i)
    print(f'sync_main 耗时: {time.time() - start :.4f}秒')
# 异步
import asyncio
async def display2(num):
    await asyncio.sleep(1)
    print('hello world',num)

async def asynchronous_main():
    start = time.time()
    tasks = [asyncio.create_task(display2(i)) for i in range(1, 10)]
    await asyncio.wait(tasks)
    print(f'asynchronous_main 耗时: {time.time() - start :.4f}秒')
"""
    asyncio.run()：Python 3.7+ 的推荐方式，自动创建、运行、关闭事件循环，一个函数搞定所有
    asyncio.create_task()：将协程包装为 Task 对象，Python 3.13 中 asyncio.wait() 必须传入 Task 而非协程
    async def + await：asynchronous_main 本身需要 await 等待任务完成，所以必须声明为 async def
"""


#

if __name__ == '__main__':
    # serial_main1()
    # concurrent_main1()
    # concurrent_main2()

    # ThreadPool_main1()
    # ThreadPool_main2()
    # ThreadPool_main3()

    # sub_main()
    # MultithreadedComputing()
    # MultiprocessComputing()

    # MultiprocessCommunication()

    # fib_main()
    # coordinate_the_process_main()
    # sync_main()
    # asyncio.run(asynchronous_main())


    pass