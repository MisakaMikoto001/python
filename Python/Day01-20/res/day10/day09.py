'''
元组的操作
    in 、not int、+
'''
from hmac import compare_digest

# 切片 ： [start:end:step]
def split():
    l = [x for x in range(10)]
    print(f'l[::2]:{l[::2]}\n')
    print(f'l[::-1]:{l[::-1]}\n')
    print(f'l[2:9:-2]:{l[2:9:-2]}\n')
    print(f'l[9:2:-2]:{l[9:2:-2]}\n')

# 比较 ： == 、 != 、 < 、 > 、 <= 、 >=
def compare():
    compare_int = (1, 2, 3, 4, 5)
    compare_str = ('1', '2', '3', '4', '5')
    compare_str2 = ('a', 'b', 'c', 'd', 'e' )
    print(f'compare_int == compare_str:{compare_int == compare_str}\n')
    print(f'compare_int != compare_str:{compare_int != compare_str}\n')
    # print(f'compare_int < compare_str:{compare_int < compare_str}\n')#TypeError: '<' not supported between instances of 'int' and 'str'
    print(f'compare_int < compare_str2:{compare_str < compare_str2}\n')
    # print(f'compare_int > compare_str:{compare_int > compare_str}\n')#TypeError: '>' not supported between instances of 'int' and 'str'
    print(f'compare_int > compare_str2:{compare_str > compare_str2}\n')
    # print(f'compare_int <= compare_str:{compare_int <= compare_str}\n')#TypeError: '<=' not supported between instances of 'int' and 'str'
    print(f'compare_int <= compare_str2:{compare_str <= compare_str2}\n')
    # print(f'compare_int >= compare_str:{compare_int >= compare_str}\n')#TypeError: '>=' not supported between instances of 'int' and 'str'
    print(f'compare_int >= compare_str2:{compare_str >= compare_str2}\n')


# 打包 、 解包 ： * 、 **
# 打包 ： 含义 是把多个元素打包成元组
# 解包 ： 含义 是把元组拆成多个元素
def pack(*args):
    int = 1, 2, 3# 因为，符号 , 所以自动创建元组
    print(f'type(int):{type(int)}\n')  # 打包
def unpack():
    tuple = 1, 2, 3
    a, b, c = tuple
    print(f'a:{a}\nb:{b}\nc:{c}\n')

    try:
        a, b = tuple
    except ValueError:
        print(f'{ValueError}: too many values to unpack (expected 2)')
    try:
        a, b, c, d = tuple
    except ValueError:
        print(f'{ValueError}: not enough values to unpack (expected 4, got 3)')
def pack_unpack():
    tuple = 1, 2, 3, 4, 5
    a, *b, c = tuple
    print(f'a:{a}\nb:{b}\nc:{c}\n')
    a, *b = tuple
    print(f'a:{a}\nb:{b}\n')
    *a, *b = tuple # SyntaxError: multiple starred expressions in assignment


if __name__ == '__main__':
    pack_unpack()
    pass
