"""
    推导式
        用来生成列表、集合、字典
"""
from pygments.lexers import func
from trio import sleep


def formula_of_derivation():
    prices = {
        "APL":120.2,
        "AML":110.1,
        "PLO":89.4,
        "EOL":111.9,
        "TPL":9,
        "ROL":134
    }

    """
        {key_expression: value_expression for item in iterable if condition}
            parameters  key_expression and value_pression is the key-value for the new dict
                        for item in iterable is traversal_part, extract the object from the iterator
                        if condition is filter criteria ,only elements that satisfy the condition will be hold on
    """
    filtered_prices = {key:value for key,value in prices.items() if value < 100}

    print(filtered_prices)

"""
嵌套列表
"""
def nested_list():
    names = ['关羽', '张飞', '赵云', '马超', '黄忠']
    courses = ['语文', '数学', '英语']
    scores = [[None] * len(courses) for i in range(len(names))]

    for row,name in enumerate(names):
        for col,course in enumerate(courses):
            scores[row][col] = input(f"请输入{name}的{course}成绩：")
            print( scores)

"""
    排序
        堆排序
            堆结构排序：大堆、小堆
"""
import heapq
def heap_sort():

    list1 = [5, 3, 1, 2, 4]
    list2 = [
        {'name': '张三', 'age': 18, 'score': 20, 'heigh': 180},
        {'name': '李四', 'age': 19, 'score': 80, 'heigh': 170},
        {'name': '王五', 'age': 20, 'score': 70, 'heigh': 260},
        {'name': '赵六', 'age': 21, 'score': 60, 'heigh': 150},
        {'name': '孙七', 'age': 22, 'score': 50, 'heigh': 140},
        {'name': '周八', 'age': 23, 'score': 40, 'heigh': 30},
        {'name': '吴九', 'age': 24, 'score': 90, 'heigh': 120}
    ]

    #
    print(f'heapq.nlargest(5, list1): {heapq.nlargest(5, list1)}')# 获取list1中的5个最大的元素
    print(f'heapq.nsmallest(5, list1): {heapq.nsmallest(5, list1)}')# 获取list1中的5个最小的元素

    print(f'heapq.nlargest(5, list2, key=lambda x:x["score"]): {heapq.nlargest(2, list2, key=lambda x:x["score"])}')# 获取list2中的5个最大的元素
    print(f'heapq.nsmallest(5, list2, key=lambda x:x["score"]): {heapq.nsmallest(1, list2, key=lambda x:x["score"])}')# 获取list2中的5个最小的元素


"""
迭代工具模块 itertools
"""
def itertools():
    import itertools
    print('start')

    # 产生abcd全排
    print(list(itertools.permutations('ABCD')))
    # 五选三组合
    print(list(itertools.combinations('ABCDE',3)))
    # 笛卡尔积
    print(list(itertools.product('ABC','123')))
    # 无限循环
    print(list(itertools.cycle(('a','b','c'))))#双层

"""
collections模块常用工具类：
    namedtuple:命令元组，一个类工厂，接受类型的名称和属性列表来创建一个类
    deque：双端队列，是列表的替代实现，python的列表底层是基于数组实现的，而deque底层是双向链表，
        因此当需要在头尾增删元素时，deque会表现出良好性能，时间渐进复杂度约为O（1）。
    counter:dict的子类，键是元素，值是元素的计数。
        它的most_common()方法可以帮助获取出现频率最高的元素。
        counter和dict的继承关系，按照CARP原则，counter和dict应该是关联更合适，这样可以
        降低耦合度，提高灵活度，通过委托的形式只暴露需要的接口。
    orderedDict:dict的子类，记录键值对的插入的顺序，看起来既有字典的行为，也有链表的行为。
    defaultdict:类似于字典类型，但是可以通过默认的工厂函数来获取对应键的默认值，相比字典的
        setdefault()方法，这种更高效
"""
def find():
    from collections import Counter

    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
        'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
        'look', 'into', 'my', 'eyes', "you're", 'under'
    ]

    counter = Counter(words)
    print(f'counter.most_common(3):{counter.most_common(3)}')


"""
函数的使用方法：
    将函数视为一等公民
        函数可以赋值给变量
        函数可以做函数的参数
        函数可以作为函数的返回值
"""
import time
from functools import wraps
#   装饰器函数（使用与取消）
def record_useing(func):
    """
    eg: 输出函数执行时间
    自定义装饰器函数，用于记录函数的执行时间
    参数：无
    返回值：无
    """
    @wraps(func) # 保留原始函数的元数据 不加的话原函数会被这个装饰器覆盖
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        print(f'{func.__name__}执行时间：{end_time - start_time}秒')
        return result
    return wrapper

@record_useing
def my_decorators():
    """
    使用装饰器函数
    """
    time.sleep(2)

def base_decorator(output):
    """ 参数化装饰器函数工厂 """
    def actual_decorator(func):
        """ 实际装饰器函数，用于装饰目标函数 """
        @wraps(func) # 保留原始函数的元数据 不加的话原函数会被这个装饰器覆盖
        def wrapper(*args,**kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            output(f'{func.__name__}执行时间：{end_time - start_time}秒')
            return result
        return wrapper
    return actual_decorator

# 定义输出方式 打印日志
def print_logger(msg):
    print(f'{func.__name__}: {msg}')
# 定义输出方式 保存到列表
list1 = []
def print_list(msg):
    print(f'{func.__name__}: {msg}')

# 使用参数化装饰器函数
def using_base_decorator():
    """
    使用基础装饰器函数
    """
    @base_decorator(print_logger)
    def slow_function(n):
        '''模拟耗时函数'''
        total = 0
        for i in range(n):
            total += i ** 2
        return total

    @base_decorator(print_list)
    def add_function(a,b):
        return a+b

    result = slow_function(1000)
    print(result)
    result = add_function(1,2)
    print(result)

# ====== 类方式定义装饰器
class DECORATORS:
    def __init__(self, output):
        ''' 通过类方式定义装饰器 '''
        self.output = output

    def __call__(self, func):
        """ 实际装饰器函数，用于装饰目标函数 """
        @wraps(func) # 保留原始函数的元数据 不加的话原函数会被这个装饰器覆盖
        def wrapper(*args,**kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            self.output(f'{func.__name__}执行时间：{end_time - start_time}秒')
            return result
        return wrapper
# 定义方法
def print_time(msg):
    print(f'{msg}')
# 使用类方式定义装饰器
# 定义装饰器实例
decorator = DECORATORS(print_time)


#============== 类定义装饰器 创建单例装饰器
# 定义单例装饰器
class SINGLETON:
    ''' 单例装饰器 '''
    def __init__(self, cls):
        self.output = cls
        self.instance = None # 单例实例字典

    def __call__(self, *args, **kwargs):
        """ 创建或返回单例实例 """
        if self.instance is None:
            self.instance = self.output(*args, **kwargs)
        return self.instance
# 创建单例装饰器实例
@SINGLETON
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 测试单例装饰器
def single_decorator():
    p1 = Person('张三', 18)
    p2 = Person('李四', 20)
    print(p1.name, p1.age)
    print(p2.name, p2.age)

#============== 线程安全的单例装饰器
import threading
import time

class SINGLETONFORSECURITY:
    ''' 单例装饰器 '''
    def __init__(self, cls):
        self.output = cls
        self.instance = None # 单例实例字典
        self.lock = threading.Lock() # 线程锁

    def __call__(self, *args, **kwargs):
        """ 创建或返回单例实例 """
        with self.lock:
            if self.instance is None:
                self.instance = self.output(*args, **kwargs)
        return self.instance

@SINGLETONFORSECURITY
class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name
# 测试线程安全的单例装饰器
def singleton_decorator():
    p1 = Person('张三', 18)
    p2 = Person('李四', 20)
    print(p1.name, p1.age)
    print(p2.name, p2.age)

# ======================== 面向对象编程
# ===== 封装 继承 多态
from abc import abstractmethod, ABCMeta

class Employer(metaclass=ABCMeta):
    ''' employee class '''
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        ''' 计算工资 '''
        pass

class Manager(Employer):
    ''' manager class '''
    def __init__(self, name):
        super().__init__(name)

    def calculate_salary(self):  # 修正：与父类方法名一致
        return 15000

class Programmer(Employer):
    ''' Programmer class '''
    def __init__(self, name, workhours=0):
        self.workhours = workhours
        super().__init__(name)

    def calculate_salary(self):  # 修正：与父类方法名一致
        return 500 * self.workhours

class Salesman(Employer):
    ''' salesman class '''
    def __init__(self, name, sales=0):
        self.sales = sales
        super().__init__(name)

    def calculate_salary(self):  # 修正：与父类方法名一致
        return 5000 + self.sales * 0.1

class Factory:
    ''' factory class CREATE EMPLOYEE'''
    @staticmethod
    def create_employee(emp_type, *args, **kwargs):
        ''' create employee '''
        all_emp_type = {
            'manager': Manager,
            'programmer': Programmer,  # 统一小写
            'salesman': Salesman
        }
        cls = all_emp_type.get(emp_type.lower())  # 统一转小写，且用 get 避免 KeyError
        if cls is None:
            raise ValueError(f"未知的员工类型: {emp_type}")
        return cls(*args, **kwargs)

def Objects_main_function():
    ems = [
        Factory.create_employee('manager', '张三'),
        Factory.create_employee('programmer', '李四', workhours=10),  # 统一小写
        Factory.create_employee('salesman', '王五', sales=10000),
    ]
    for emp in ems:
        print(emp.name, emp.calculate_salary())
"""
    类于类的关系
        1. is-a :继承
        2. has-a :关联 / 聚合 / 组合
        3. use-a :依赖
"""
# ======================== 关联 组合
# 例 扑克游戏
from enum import Enum,unique
import random

@unique
class Suits(Enum):
    """ 牌色 """
    SPADES, HEART, CLUBS, DIAMONDS = range(4)

    def __lt__(self, other):
        """ 花色比较大小 """
        return self.value < other.value

class Card:
    """ 牌 """
    suits = ['♠', '♥', '♣', '♦']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, suit, rank):
        """ 初始化牌 """
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        """ 表示牌 """
        return f"{self.suits[self.suit.value]}{self.ranks[self.rank - 1]}"

class Poker:
    """ 扑克游戏 """

    def __init__(self):
        self.index = 0
        self.cards = [Card(suit, rank)
                      for suit in Suits
                      for rank in range(1,14)] # 初始化扑克牌

    def shuffle(self):
        """ 洗牌 """
        random.shuffle(self.cards) # 随机打乱牌组
        self.index = 0

    def deal(self):
        """ 发牌 """
        card = self.cards[self.index]
        self.index += 1
        return card

    @property
    def has_more(self):
        """ 是否还有牌 """
        return self.index < len(self.cards)

class Player:
    """ 玩家 """
    def __init__(self, name):
        self.name = name
        self.hand = [] # 玩家手牌

    def get_one(self, card):
        """ 获取牌 """
        self.hand.append(card)

    def sort(self, compare=lambda card: (card.suit, card.rank)):
        """ 排序 """
        self.hand.sort(key=compare)# 排序标准就Suit基类的lt方法

def play_poker_main():
    poker = Poker()
    poker.shuffle()

    players = [Player('张三'), Player('李四'), Player('王五')]
    while poker.has_more:
        """ 游戏循环 """
        for player in players:
            """ 玩家循环 """
            if poker.has_more:
                """ 发牌 """
                player.get_one(poker.deal())
    for player in players:
        """ 玩家循环排序 """
        player.sort()
        print(f'{player.name} 手牌: {player.hand}')
        player.hand.clear()
    print('游戏结束')

# ========== 垃圾回收 、循环引用、弱引用 ==========
# Python 使用自动化内存管理，无需手动释放内存。这种机制称为垃圾回收（Garbage Collection）。
# 这种管理机制以 引用计数 为基础，同时也引入了 标记-清楚 当一个对象的引用计数为0时，该对象的内存就会被释放。
"""
C源码 PyObject 结构体
typedef struct _object {
    int refcnt;
    void *data;
} PyObject;
"""
import sys

class PyObject:
    _all_instances = []  # 类级别的跟踪列表

    def __init__(self, data):
        self.data = data
        self.ob_type = type(data)
        PyObject._all_instances.append(self)

    def refcnt(self):
        """计算这个对象被引用的真实次数"""
        count = 0
        import gc
        for obj in gc.get_objects():
            if obj is self:
                count += 1
        return count

def PyObject_Simple():
    print("=== 真实的引用计数变化 ===")

    # 创建对象 +1
    a = [1, 2, 3]
    print(f"刚创建: sys.getrefcount(a) = {sys.getrefcount(a)}")  # 注意：getrefcount 自己也会 +1

    # 赋值给新变量 +1
    b = a
    print(f"b = a: sys.getrefcount(a) = {sys.getrefcount(a)}")

    # 再赋值 +1
    c = a
    print(f"c = a: sys.getrefcount(a) = {sys.getrefcount(a)}")

    # 放入列表
    lst = [a]
    print(f"放入列表: sys.getrefcount(a) = {sys.getrefcount(a)}")

    # 删除引用 -1
    del b
    print(f"del b: sys.getrefcount(a) = {sys.getrefcount(a)}")

    # 变量重新赋值 +1
    c = "new"
    print(f"c = 'new': sys.getrefcount(a) = {sys.getrefcount(a)}")

    # 从列表移除 -1
    lst.remove(a)
    print(f"从列表移除: sys.getrefcount(a) = {sys.getrefcount(a)}")

"""
引用计数会因为循环引用导致内存泄露，为了解决这个问题，引入了 “标记-清除”和“分代收集”。
    举例说明就是，在创建一个对象的时候，会被放在第一代中，如果在垃圾检查中活了下来，
    就会放在第二代，如果在第二代垃圾检查中活了下来，就会放在第三代，类推。
    
    以下情况会导致垃圾回收：
        调用  gc.collect()
        gc 模块的计数器到达阈值
        程序退出
"""

# ============ 混入 （Mixin） ============
"""
    混入 （Mixin） 是一种设计模式，用于将多个类的特征组合到一个类中。
    这种模式在 Python 中通过使用继承来实现。
    遵循 “单一职责原则”，每个类只负责一个特定功能。
    举例说明就是，在创建一个类的时候，我们可以继承多个类的特征，从而实现代码的复用。
    这种模式在 Python 中被称为 混入 （Mixin） 。
"""
class SetOnceMappingMixin:
    """ 自定义混入类  只设置一次的映射类 """
    __slots__ = () # 不使用 __dict__ 属性

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key)+' already set')
        return super().__setitem__(key, value) #协作式多重继承

class SetOnceDict(SetOnceMappingMixin, dict):# mixin 必须先于dict
    """ 自定义字典类  只设置一次的映射类 """
    pass

def SetNonceDict_main():
    my_dict = SetOnceDict()
    my_dict['a'] = 1
    my_dict['b'] = 2
    # my_dict['a'] = 3  # 报错
    print(f'mro: {SetOnceDict.__mro__}')

# ===== mro 方法解析顺序
class A():
    def say_hello(self):
        print('hello,A')

class B(A):
    pass

class C(A):
    def say_hello(self):
        print('hello C')

class D(B, C):
    pass

def mro_main():
    print(D.__mro__)
    D().say_hello()

# ============== 元编程与元类 ==============
"""
    对象是类创建的，类是元类创建的。元类创建类的元信息。所有的类都直接或简介的继承自 Object 。
    所有的元类都直接或间接的继承自 type 类。
"""
# 例子 使用元类实现单例模式
import threading

class SingletonMeta(type):
    """ 自定义元类  单例模式 """
    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        cls.__lock = threading.RLock()
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance

class President(metaclass=SingletonMeta):
    """ 自定义总统类  单例模式 """
    pass

def meta_main():
    p1 = President()
    p2 = President()
    print(p1 is p2)  # True


# =============== 并发编程 ==============
"""
    并发编程是指在程序中，多个任务或线程同时执行，以提高程序的效率和响应性。
    并发编程的目的是利用多核处理器的并行计算能力，提高程序的执行速度。
    并发编程的实现方式有多种，包括多线程、多进程、异步编程等。
    
    多进程：每个进程执行一个任务，进程之间通过通信进行合作。
    异步编程：程序在执行过程中，会将任务分解为多个异步操作，每个操作在后台执行，不阻塞主程序的执行。
"""
# 例子 多线程
import glob
import threading
import os
from PIL import Image

PREFIX = 'thread'

def generate__thumbnail(infile, size, format='PNG'):
    """ 生成指定图片的缩略图 """
    file, ext = os.path.splitext(infile) # 获取文件名和扩展名
    file = os.path.basename(file) # 移除路径前缀
    print(file)
    outfile = f'{PREFIX}/{file}_{size[0]}_{size[1]}.{ext}' # 生成缩略图文件名

    img = Image.open(infile) # 打开图片
    img.thumbnail(size, Image.LANCZOS) # 缩略图
    img.save(outfile, format) # 保存缩略图

def thumbnail_main():
    """ 多线程生成缩略图 """
    if not os.path.exists(PREFIX):
        # """ 如果缩略图文件夹不存在，创建它 """
        os.makedirs(PREFIX)
    for infile in glob.glob(r'C:\Users\Administrator\Pictures\Saved Pictures\*.png'):
        for size in [(32, 32), (64, 64), (128, 128)]:
            """ 创建线程 """
            threading.Thread(
                target=generate__thumbnail,
                args=(infile, size),
            ).start()

# 多线程 竞争资源
from concurrent.futures import  ThreadPoolExecutor

class Account:
    """ 极限资源类 """
    def __init__(self):
        self.balance = 0.0
        self.lock = threading.Lock()

    def deposit(self, amount):
        """ 存款 """
        # 加锁 10000
        with self.lock:
            new_balance = amount + self.balance
            time.sleep(0.001)
            self.balance = new_balance

        # # 无锁 1100
        # new_balance = self.balance + amount
        # time.sleep(0.001)
        # self.balance = new_balance

def multithreading_main():
    account = Account()

    # 创建线程池
    pool = ThreadPoolExecutor(max_workers=10)
    Futures = []
    # 提交任务
    for i in range(100):
        future = pool.submit(account.deposit, 100)
        Futures.append(future)

    # 关闭线程池
    pool.shutdown(wait=True)
    for future in Futures:
        future.result()
    print(account.balance)


   # =========================

def main():
    # formula_of_derivation()
    # nested_list()
    # heap_sort()
    # itertools()
    # find()

    # my_decorators()
    # 在外部检查
    # print(my_decorators.__name__)

    # using_base_decorator()
    # decorator
    # single_decorator()

    # Objects_main_function()
    # play_poker_main()

    # PyObject_Simple()

    # SetNonceDict_main()
    # mro_main()

    # meta_main()
    # thumbnail_main()
    multithreading_main()
    pass

if __name__ == '__main__':
    main()