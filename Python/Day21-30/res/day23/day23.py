"""
csv
    纯文本，使用某种字符集，如ASCII、Unicode、gb2312等
    由一条条记录组成，典型每行一条
    每条记录被分隔符，有‘，’、‘|’、’；‘等，分隔成段或列
    每条数据有相同的字段序列
"""

import csv
import random
def csv_read():
    """scv 读取"""

    with open('test.csv', 'r', encoding='utf-8') as f:
        """reader模块 会返回一个csvreader，是迭代器， 可用next、for-in循环读取"""
        csv_reader = csv.reader(f, delimiter='|')
        for row in csv_reader:
            """返回列表的一个对象，是一组数据"""
            print(csv_reader.line_num, end=' \t')
            for col in row:
                print(col, end='\t')
            print()
    pass

def csv_write():
    """csv 写入"""

    with open('test.csv', 'w', encoding='utf-8', newline='') as f:
        """writer模块 会返回一个csvwrite对象，可以用csvwrite对象的writerow、writerows方法将数据写入csv文件"""
        writer = csv.writer(f)
        writer.writerow(['id', 'name', 'age', 'sex'])
        names = ['lisi', 'wangwu', 'zhaoliu']
        for name in names:
            score = [random.randrange(50,100) for _ in range(4)]# 生成4个随机数
            score.insert(0, name) # 插入name
            writer.writerow(score)

    pass

def main():
    csv_read()
    csv_write()

if __name__ == '__main__':
    main()