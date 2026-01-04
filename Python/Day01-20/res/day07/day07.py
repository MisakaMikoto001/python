# 花旗骰子
'''
说明：CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
简化后的规则是：玩家第一次摇骰子如果摇出了 7 点或 11 点，玩家胜；玩家第一次如果摇出 2 点、3 点或 12 点，庄家胜；
玩家如果摇出其他点数则游戏继续，玩家重新摇骰子，如果玩家摇出了 7 点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；
其他点数玩家继续摇骰子，直到分出胜负。
为了增加代码的趣味性，我们设定游戏开始时玩家有 1000 元的赌注，
每局游戏开始之前，玩家先下注，如果玩家获胜就可以获得对应下注金额的奖励，如果庄家获胜，玩家就会输掉自己下注的金额。
游戏结束的条件是玩家破产（输光所有的赌注）。
'''

'''
import random
'''
import random

money = 1000
while money > 0:
    print(f'资产:{money}')

    while True:
        debt = int(input('请下注:'))
        if 0 < debt <= money:
            break

    point = random.randint(1, 6) + random.randint(1, 6)

    if point == 7 or point == 11:
        money += debt
        print(f'玩家摇出了{point}，玩家胜，获得{debt}元,目前资产为{money}')
    elif point == 2 or point == 3 or point ==12:
        money -=  debt
        print(f'玩家摇出了{point}，庄家胜，损失{debt}元,目前资产为{money}')
    else:
        while True:
            point = random.randint(1, 6) + random.randint(1, 6)
            if point == 7 or point == 11:
                money += debt
                print(f'玩家摇出了{point}，玩家胜，获得{debt}元,目前资产为{money}')
                break
            elif point == 2 or point == 3 or point ==12:
                money -= debt
                print(f'玩家摇出了{point}，庄家胜，损失{debt}元,目前资产为{money}')
                break

print(f'你破产了，资产{money}')