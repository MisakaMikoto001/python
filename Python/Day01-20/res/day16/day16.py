'''
高阶函数操作
    不定参数、列表
    匿名函数
'''


def add(a, b):
    return a + b
def mul(a, b):
    return a * b

# 多参
def calc(*args, **kwargs):
    items = list(args) + list(kwargs.values())
    result = 0

    for item in items:
        if type(item) in (int, float):
            result += item
        else:
            print('calc参数错误')

    return result

# Y优化
def calc2(init_value, func, *args, **kwargs):
    items = list(args) + list(kwargs.values())
    result = init_value

    for item in items:
        if type(item) in (int, float):
            result = func(result, item)
        else:
            print('calc2参数错误')
            continue

    return result

def FUNC():
    dict = {'num1':'a', 'num2':'b', 'num3':'c', 'num4':'d'}
    print(f'calc(1,2,3,4,dict): {calc(1,2,3,4,**dict)}')
    print(f'calc2(1,add,2,3,4,dict): {calc2(1,add,2,3,4,**dict)}')

# 过滤 filter 映射 map
class FILTER_MAP:

    # 筛选条件
    def filter_func(self,num):
        return  num % 2 != 0

    # 映射条件
    def map_func(self,num):
        return num ** 2

def filter_map():
    numbers = [1,2,3,4,5]
    function = FILTER_MAP ()
    lists = list(map(function.map_func, filter(function.filter_func, numbers)))

    print(f'lists: {lists}')

# 匿名函数
def anonymous_func(num1: int,num2: int):
    '''
    定义 lambda 函数的关键字是lambda，后面跟函数的参数，如果有多个参数用逗号进行分隔；
    冒号后面的部分就是函数的执行体，通常是一个表达式，表达式的运算结果就是 lambda 函数的返回值，不需要写return 关键字
    '''

    # 在 f-string 的表达式部分无法直接调用带参数的函数
    # print(f'add = lambda num1: num1 + num2: {lambda X,Y:X + Y（num1,num2)}')# lambda函数只创建未被调用，是fstring的特性之一

    # lambda函数创建后，可以调用
    lambda_add = lambda num1,num2: num1 + num2
    print(f'lambda_add(num1,num2): {lambda_add(num1,num2)}')#lambda_add(num1,num2): 11

    # 可以使用普通函数调用
    print(f'result:{(lambda x,y:x+y)(num1,num2)}')#result:11

# sorted函数
def sorted_func():
    # 列表排序
    numbers = [10,1,2,3,4,5]
    print(f'sorted(numbers): {sorted(numbers)}')
    print(f'sorted(numbers, reverse=True): {sorted(numbers, reverse=True)}')
    print(f'sorted(numbers, key=lambda x:x%2): {sorted(numbers, key=lambda x:x%2)}')

    # 字典排序
    dict = {'num1':'a', 'num2':'b', 'num3':'c', 'num4':'d'}
    print(f'sorted(dict.items(), key=lambda x:x[1]): {sorted(dict.items(), key=lambda x:x[1])}')

# 偏函数 functools.partial：创建一个新函数，使用一个已定义的函数的功能，并添加新的功能
import functools
def partial_func():
    '''
    partial:
        参数1，返回值都是函数
    '''

    int2 = functools.partial(int,base=2)
    print(f'int2("1001"): {int2("1001")}')
    int8 = functools.partial(int,base=8)
    print(f'int8("1001"): {int8("1001")}')
    int16 = functools.partial(int,base = 16)
    print(f'int16("1001"): {int16("1001")}')


if __name__ == '__main__':
    # FUNC()
    # filter_map()
    # sorted_func()
    # anonymous_func(5,6)
    partial_func()

    pass
