"""
    正则表达式
        用于格式匹配与校验，常用于输入

    核心函数
        compile（pattern，flags=0）                        编译正则表达式，返回正则表达式对象
        match（pattern，string，flags=0）                   用正则表达式匹配字符串，成功返回匹配对象，否则返回None
        search（pattern，string，flags=0）                  搜索字符串中第一次出现正则表达式的模式，成功返回匹配对象，否则返回None
        split（pattern，string，maxsplit=0，flags=0）        用正则指定格式的模式分割符，拆分字符串，返回列表
        sub（pattern，repl，string，count=0，flags=0）       用指定的字符串替换原字符串中符合正则表达式匹配的部分，count可以计数替换的次数
        fullmatch（pattern，string，flags=0）                match函数的完全匹配（一字不差）版本
        findall（pattern，string，flags=0）                 查找字符串中所有与正则表达式相匹配的部分，成功返回字符串列表
        dinditer（pattern，string，flags=0）                查找字符串所有与正则表达式匹配的
"""
