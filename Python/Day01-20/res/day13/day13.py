'''
dict
    {key:value}
'''

# 创建
def create():
    # {}字面量创建
    dict1 = {'name': 'zhangsan', 'age': 18}
    print(f'dict1:{dict1}\n')

    # dict构造函数创建
    dict2 = dict(name='lisi', age=19)
    print(f'dict2:{dict2}\n')

    # zip : 压缩两个序列创建字典
    dict3 = dict(zip('abcde','12345'))
    dict4 = dict(zip('abcde',range(1,10)))#  dict4:{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    print(f'dict3:{dict3}\n', f'dict4:{dict4}\n')

    # 生成语法创建
    dict5 = {i:i**2 for i in range(1,10)}
    print(f'dict5:{dict5}\n')

    pass


if __name__ == '__main__':
    create()

    pass
