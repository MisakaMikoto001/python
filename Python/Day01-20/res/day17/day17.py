'''
函数的高级应用
    装饰器：用一个函数装饰另外一个函数并为其提供额外的能力
    递归: 函数自己调用自己称为递归调用
'''

# 装饰器
def add(a, b):
    '''
    初始函数
    '''
    return a + b

def re_add(func):
    '''
    装饰器
    '''
    def wrapper(*args, **kwargs):
        print('原始函数执行前')
        result = func(*args, **kwargs)# 原始函数不变，在其前后添加功能
        print('原始函数执行后')
        return result
    return  wrapper

def FUNC1():
    print(f'add(1,2): {add(1,2)}')
    print(f're_add(add)(1,2): {re_add(add)(1,2)}')

@re_add
def add(a, b):
    '''
    被装饰的函数
    '''
    return a + b

def FUNC2():
    print(f'add(1,2): {add(1,2)}')


# 递归
def factorial_add(n):
    '''
    简单且重复的内容最适合递归
    需要注意出口，避免无限递归
    '''
    if n == 1:# 递归出口
        return 1
    else:
        return n + factorial_add(n - 1)
    pass


if __name__ == '__main__':
    # FUNC2()
    print(f'factorial_add(100): {factorial_add(100)}')

    pass