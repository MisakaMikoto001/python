# list operation
# l = [1, 2, 3, 4, 5]
# l.append(6)
# print(l)
# l.insert(0, 0)
# print(l)
# try:
#     l.pop(7)
# except IndexError:
#     print('IndexError     l.pop(7)')
# try:
#     l.remove(9)
# except ValueError:
#     print('ValueError     l.remove(7)')
# try:
#     l.index(7)
# except ValueError:
#     print('ValueError     l.index(7)')
#
# l.count(1)
# l.extend([7, 8, 9])
# print(l)
#
# l.reverse()
# print(l)
# l.sort()
# print(l)
# del l[0]
# print(l)
# l.clear()
# print(l)

'''
双色球是由中国福利彩票发行管理中心发售的乐透型彩票，每注投注号码由6个红色球和1个蓝色球组成。
红色球号码从1到33中选择，蓝色球号码从1到16中选择。每注需要选择6个红色球号码和1个蓝色球号码
'''

import random

red_balls = [x for x in range(1, 34)]
blue_balls = [x for x in range(1, 17)]
red_selected = random.sample(red_balls, 6) # sample 函数是 从列表中随机抽取指定数量的元素
blue_selected = random.choice(blue_balls) # choice 函数是 从列表中随机抽取一个元素

red_selected.sort()
print(red_selected, blue_selected)