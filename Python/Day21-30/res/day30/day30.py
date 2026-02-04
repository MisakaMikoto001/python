"""
    正则表达式
        用于格式匹配与校验，常用于输入

        常用符号
        .		通配符	                            b.t	        可以匹配 bat/but/b1t/b#t等等
        \\w		匹配字母、数字、下划线	                b\\wt	    可以匹配bat/b1t/b_t
        \\s		匹配空白字符，如空格，\\t，\\n，\\r等	love\\syou	love you
        \\d		匹配数字	                            \\d\\d	    可以匹配 00 / 01 / 02 等
        \\b		匹配单词的边界	                        \\blove\\b	可以匹配完整的love 如
                                                                    i, love you, my lover
                                                                    中的love，而不会匹配lover的love
        ^		匹配字符串的开始位置	                ^i	        可以匹配任意i开头的字符串
        $		匹配字符串的结束位置	                $you	    可以匹配任意you结尾的字符串
        \\W		匹配非字母、数字、下划线	            b\\Wt	    不可以匹配bat/b1t/b_t
                                                                    可以匹配b@t/b#t/b t/等等
        \\S		匹配非空白字符	                        love\\Syou	可以匹配love#you，但不能匹配love you
        \\D		匹配非数字	                        \\d\\D	    匹配0@/2#/3%等等
        \\B		匹配非单词边界	                        \\Blove\\B	不可以匹配完整的love 如
                                                                    i, love you, my lover
                                                                    中的love，而是会匹配lover的love

    核心函数
        compile（pattern，flags=0）                         编译正则表达式，返回正则表达式对象
        match（pattern，string，flags=0）                   用正则表达式匹配字符串，成功返回匹配对象，否则返回None
        search（pattern，string，flags=0）                  搜索字符串中第一次出现正则表达式的模式，成功返回匹配对象，否则返回None
        split（pattern，string，maxsplit=0，flags=0）        用正则指定格式的模式分割符，拆分字符串，返回列表
        sub（pattern，repl，string，count=0，flags=0）       用指定的字符串替换原字符串中符合正则表达式匹配的部分，count可以计数替换的次数
        fullmatch（pattern，string，flags=0）                match函数的完全匹配（一字不差）版本
        findall（pattern，string，flags=0）                 查找字符串中所有与正则表达式相匹配的部分，成功返回字符串列表
        finditer（pattern，string，flags=0）                查找字符串所有与正则表达式匹配的部分，返回一个迭代器
        purge（）                                           清除隐式编译的正则表达式缓存
        re.I / re.IGNORECASE                               忽略大小写匹配标记
        re.M / re.MULTILINE                                多行匹配标记
"""


"""
例子1：验证输入用户名和QQ号是否有效并给出对应的提示信息
    要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
"""
import re

def check_name_qqnum(name,qq):
    """
        match 第一个参数是正则表达式对象，第二个参数待匹配的字符串
    """
    name_pattern = re.match(r'^[0-9a-zA-Z_]{6,20}$', name)# 匹配用户名 ^: 开头 $: 结尾
    qq_pattern = re.match(r'^[1-9]\\d{4,11}$', qq)
    if name_pattern and qq_pattern:
        print('用户名：%s,QQ号：%s有效' % (name, qq))
    elif not name_pattern:
        print('用户名：%s无效' % (name))
    else:
        print('QQ号：%s无效' % (qq))

"""
例子2：从一段文字中提取出国内手机号码。
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也不是110或119，王大锤的手机号才是15600998765。
"""
def extraction_phone_number():
    """
        re.S: 使.匹配包括换行在内的所有字符
    """
    text = "重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，\n不是15600998765，也不是110或119，王大锤的手机号才是15600998765。"
    pattern = re.compile(r'(?<=\D)1[3-9]\d{9}(?=\D)')# ？<= 匹配前面，？= 匹配后面

    # 查找文本匹配并存到列表中
    matches = re.findall(pattern, text)
    for match in matches:
        print(match)
    print('---------------------------------------------------------------------------------------------------------')

    # 迭代器
    for match in re.finditer(pattern, text):
        print(match.group())
    print('---------------------------------------------------------------------------------------------------------')

    # search
    match3 = pattern.search(text)
    while match3:
        print(match3.group())
        match3 = pattern.search(text, match3.end())

"""
例子3：替换字符串中的不良内容
"""
def replace_bad_content():
    """
        replace
    """
    content = 'Oh, shit! 你是傻逼吗? Fuck you.'
    pattern = re.compile(r'shit|fuck|[傻逼]', re.I)
    # pattern = re.compile(r'[shit][fuck][傻逼]', flags=re.I)# 【】匹配任意字符
    print(f're.sub(pattern, "***", content): {re.sub(pattern, "***", content)}')


"""
例子4：拆分长字符串
"""
def split_long_string():
    poem = """
    There was a young lady named Bright,
    Whose speed was far faster than light;
    She started one day
    In a relative way,
    Into the night.
    """

    sentence = re.split(r'[,;.]', poem)
    list = [list for list in sentence if list]

    for sentence in list:
        print(sentence)

def main():
    # check_name_qqnum('namda12@', '12345678')
    # check_name_qqnum('namda12', '0345678')
    # extraction_phone_number()
    # replace_bad_content()
    split_long_string()

    pass

if __name__ == '__main__':
    main()