"""
    推导式
        用来生成列表、集合、字典
"""
from pygments.lexers import func


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
    ''' 通过类方式定义装饰器 '''
    def __init__(self, output):
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
# 例 扑克游戏
from enum import Enum,unique
import random

@unique
class Suits(Enum):
    """ 牌色 """
    SPADES, HEART, CLUBS, DIAMONDS = range(4)

    def __lt__(self, other):
        """  """
        return self.value < other.value




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

    Objects_main_function()
    pass


if __name__ == '__main__':
    main()