"""
文件读写、异常处理
    文件读写
        打开
            open: 参数，文件地址，操作方法，编码方法
            操作： r 只读
                  w 若存在，清空后写入；若不存在，创建后写入
                  x 若存在，写入异常；若不存在，创建后写入
                  a 文件末尾追加写入
                  b 二进制模式打开
                  t 文本模式
                  + 更新模式
        关闭
            close：

    异常处理

"""

def open_file_with_read(filepath):
    """文件、异常"""

    # r 只读
    file = open(filepath, 'r', encoding='utf-8')
    print(file.read())
    file.close()

def open_file_with_write(filepath, content):
    """文件、异常"""

    # w 若存在，清空后写入；若不存在，创建后写入
    file = open(filepath, 'w', encoding='utf-8')
    file.write(content)
    file.close()

def open_file_with_append(filepath, content):
    """文件、异常"""

    # a 文件末尾追加写入
    file = open(filepath, 'a', encoding='utf-8')
    file.write(content)
    file.close()

def open_file_with_x(filepath,content):
    """文件、异常"""

    # x 若存在，写入异常；若不存在，创建后写入
    try:
        file = open(filepath, 'x', encoding='utf-8')
        file.write(content)
        file.close()
    except FileExistsError:
        print('文件已存在')

def open_file_with_plus(filepath, content):
    """文件、异常"""

    # + 读写模式
    file = open(filepath, 'w+', encoding='utf-8')
    file.write(content)
    print(file.read())
    file.close()

def open_file_with_binary(filepath):
    """文件、异常"""

    # b 二进制模式打开
    file = open(filepath, 'rb')
    print(file.read())
    file.close()

def open_file_with_text(filepath, content):
    """文件、异常"""

    # t 读写模式
    file = open(filepath, 'w+t', encoding='utf-8')
    file.write(content)
    print(file.read())
    file.close()

def open_file_with_exception(filepath):
    """文件、异常"""

    try:
        file = open(filepath, 'r', encoding='utf-8')
        print(file.read())
        file.close()
    except FileNotFoundError:
        print('文件不存在')
    except UnicodeDecodeError:
        print('文件编码错误')

def open_close_file():
    """主函数"""
    str = '自嘲\n现代⋅ 鲁迅\n运交华盖欲何求，未敢翻身已碰头。\n破帽遮颜过闹市，漏船载酒泛中流。\n横眉冷对千夫指，俯首甘为孺子牛。\n躲进小楼成一统，管他冬夏与春秋。'

    # read
    open_file_with_read('test.txt')

    # write
    open_file_with_write('test.txt', str)
    open_file_with_read('test.txt')

    # append
    open_file_with_append('test.txt', str)
    open_file_with_read('test.txt')

    # x
    open_file_with_x('test.txt', str)
    open_file_with_read('test.txt')

    # +
    open_file_with_plus('test.txt', str)
    open_file_with_read('test.txt')

    # binary
    open_file_with_binary('test.txt')
    open_file_with_text('test.txt', str)

    # exception
    open_file_with_exception('test.txt')

def defind_exception(valueError):
    """定义异常"""
    pass

def factorial(n):
    """阶乘"""
    if n < 0:
        raise defind_exception('n must be >= 0')
    if n == 0:
        return 1
    return n * factorial(n - 1)

def faction_defind_exception():
    """阶乘异常"""
    try:
        print(factorial(-1))
    except defind_exception as e:
        print(e)

def main():
    # open_close_file()
    faction_defind_exception()

if __name__ == '__main__':
    main()