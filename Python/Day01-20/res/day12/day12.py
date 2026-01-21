'''
set
    无序、不可重复

主要包含，成员运算、二元运算、比较运算

'''

# 二元运算：交、对称差、并、差
def binary_op():
    s1 = {1, 2, 3, 4, 5}
    s2 = {4, 5, 6, 7, 8}

    # 交集
    print(f's1&s2:{s1&s2}')
    print(f's1.intersection(s2):{s1.intersection(s2)}\n')#intersection:交集运算方法，返回一个交集对象

    # 对称差
    print(f's1^s2:{s1^s2}')
    print(f's1.symmetric_difference(s2):{s1.symmetric_difference(s2)}\n')#symmetric_difference:对称差运算方法，返回一个对称差对象

    # 并集
    print(f's1|s2:{s1|s2}')
    print(f's1.union(s2):{s1.union(s2)}\n')#union:并运算方法，返回一个并集对象
    # 更新运算
    s3 = {1, 2, 3}
    s4 = {1, 2, 3}
    s3 |= s2
    print(f's3 |= s2 : {s3}')
    s4.update(s2)
    print(f's4.update(s2):{s4}\n')


    # 差集
    print(f's1-s2:{s1-s2}')
    print(f's1.difference(s2):{s1.difference(s2)}\n')#difference:差集运算方法，返回一个差集对象

# 比较运算
def compare():
    s1 = {1, 2, 3, 4, 5}
    s2 = {4, 5, 6, 7, 8}
    s3 = {1, 2, 3}

    print(f's1 == s2:{s1 == s2}')
    print(f's1 != s2:{s1 != s2}')
    print(f's1 < s2:{s1 < s2}')
    print(f's1 > s2:{s1 > s2}')
    print(f's1 <= s2:{s1 <= s2}')
    print(f's1 >= s2:{s1 >= s2}')
    print(f's1 < s2 < s3:{s1 < s2 < s3}')
    print(f's1 > s2 > s3:{s1 > s2 > s3}')
    print(f's1 <= s2 <= s3:{s1 <= s2 <= s3}')
    print(f's1 >= s2 >= s3:{s1 >= s2 >= s3}')



    pass

# 方法： add()、clear()、copy()、discard()、pop()、remove()、update()
def methods():
    s1 = {1, 2, 3, 4, 5}

    # add()  集合添加元素
    s1.add(range(1,100))# range（1，100）会变成一个元素被添加进去
    print(f's1.add(range(1,100)):{s1}')
    # update() 集合批量添加元素
    s1.update(range(1, 10))
    print(f's1.update([range(1,10)]):{s1}')

    # copy 集合1复制到集合2
    s2 = s1.copy()
    print(f's2:{s2}')

    # discard() 集合1删除指定元素
    s1.discard(1)
    print(f's1.discard(1):{s1}')

    # pop() 集合1删除一个元素，会返回被删除的元素
    result = s1.pop()
    print(f's1.pop():{s1}，删除的元素是：{result}')

    # remove() 集合1删除指定元素
    s1.remove(5)
    print(f's1.remove(2):{s1}')

    # clear() 集合1清空
    s1.clear()
    print(f's1.clear():{s1}')

    pass

if __name__ == '__main__':
    # binary_op()
    # compare()
    # methods()

    pass