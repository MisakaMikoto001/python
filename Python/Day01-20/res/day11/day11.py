'''
转义字符 含义：\n \t \r
原始字符 r/R‘’
'''

# 转义与原始字符
def escape():
    s1 = '\t \is \time \to \read \now'
    s2 = r'\it \is \time \to \read \now'
    print(s1)
    print(s2)

# 拼接与重复
def join_multi():
    s = 'hello'
    print(s * 3)
    print('-' * 50)
    print('hello' + 'world')
    print('-' * 50)
    print('hello' + ' ' + 'world')
    print('-' * 50)
    print('hello' + ' ' + 'world' + ' ' + 'python')
    print('-' * 50)
    print('hello' + ' ' + 'world' + ' ' + 'python' + ' ' + 'programming')

# 比较
def compare():
    s1 = 'hello world'
    s2 = 'life is a fuck movie'
    print(s1 == s2)
    print(s1 != s2)
    print(s1 > s2)
    print(s1 < s2)

# 索引与切片
def index_slice():
    s = 'hello world'

    print(f's[0]:{s[0]}, s[-1]:{s[-1]}\n')
    print(f's[0:5:1]:{s[0:5:1]}, s[5:0:-2]:{s[5:0:-2]}')
    try:
        print(s[20])
    except Exception as e:
        print(f's[10]:{e}')

    try:
        print(f's[1:-5:-1]:{s[1:-5:-1]}')
    except Exception as e:
        print(f's[1:10:10]:{e}')

    pass

# 拆分与合并
def split_join():
    # 拆分 指定元素不要，取两边
    s = 'hello world'
    print(f's.split():{s.split()}\n')#默认空格拆分
    print(f's.split("o"):{s.split("o")}\n')#指定字符拆分
    print(f's.split("o", 1):{s.split("o", 1)}\n')#指定次数拆分

    # 合并
    s = 'hello world'#原始字符串
    str = s.split()#拆分

    # 合并 语法： "-".join(str)
    print(f'("-").join(str):{("-").join(str)}\n')#合并
    pass

if __name__ == '__main__':
    # escape()
    # join_multi()
    # compare()
    # index_slice()
    # split_join()


    pass