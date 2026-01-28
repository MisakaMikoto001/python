"""
练习
    类和类之间的关系可以粗略的分为 is-a关系（继承）、has-a关系（关联）和 use-a关系（依赖）
"""
from random import random

"""
例子1：扑克游戏。
说明：简单起见，我们的扑克只有52张牌（没有大小王），游戏需要将 52 张牌发到 4 个玩家的手上，每个玩家手上有 13 张牌，
按照黑桃、红心、草花、方块的顺序和点数从小到大排列，暂时不实现其他的功能。
"""
from enum import Enum
class Suit(Enum):
    """
        枚举：不可变性，成员一旦创建不可改变
             唯一性，每个成员都有唯一的名称与值
    """
    SPADES, HEART, CLUB, DIAMONDS = range(4)# 给花色标记排序 0-3


class Card:
    """卡牌"""

    def __init__(self, point, suit):
        """
        :param point: 点数
        :param suit: 花色
        """
        self.point = point
        self.suit = suit

    def __str__(self):
        """
        :return: 牌面信息
        """
        suit_names = ['♠️', '❤️', '♣️', '♦️'] # 对应花色排序定义符号
        point_names = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f"{suit_names[self.suit.value]}{point_names[self.point]}"

    def __lt__(self, card):
        """卡牌排序"""
        if self.point == card.point:# 点数相同
            return self.suit.value < card.suit.value# 花色排序
        return self.point < card.point# 点数排序

# card2 = Card(2, Suit.CLUB)
# print(card2)
# cardA = Card(0, Suit.SPADES)
# print(cardA)
import  random
class Poker:
    """扑克"""

    def __init__(self):
        """初始化"""
        self.cards = [Card(point, suit)
                      for suit in Suit
                      for point in range(13)
                      ]
        self.current = 0# 当前牌

    def __str__(self):
        """显示格式化牌面信息，需调对象，直接访问属性不会触发本方法"""
        return f"[{', '.join(str(card) for card in self.cards)}]"

    def shuffle(self):
        """洗牌"""
        self.current = 0
        random.shuffle(self.cards)# 随机打乱

    def deal(self):
        """发牌"""
        if not self.has_more:
            print("没有牌了")
            return  None
        card = self.cards[self.current]# 获取牌
        self.current += 1
        return card

    @property # 属性方法 只读装饰器
    def has_more(self):
        """是否有牌"""
        return self.current < len(self.cards) # 剩余牌数

# poker = Poker()
# # print(f'poker:{poker.cards}')# 打印列表对象 ，未能调用str方法
# print(f'poker{ poker}')
# poker.shuffle()
# print(f'poker:{poker}')

class Player:
    """玩家"""

    def __init__(self,name):
        """初始化"""
        self.name = name
        self.cards = []

    def __str__(self):
        """显示玩家卡牌信息"""
        return f"{self.name}:{list(map(str,self.cards))}"
        # return f"{', '.join(str(card) for card in self.cards)}"

    def get_card(self, card):
        """摸牌"""
        self.cards.append(card)

    def arrange(self):
        """整理牌"""
        self.cards.sort(key=lambda card: (card.suit.value, card.point))

def main():
    """主程序"""
    poker = Poker()
    poker.shuffle()
    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]

    while poker.has_more:
        for player in players:
            player.get_card(poker.deal())

    for player in players:
        player.arrange()
        print(f'{player}')

    pass


if __name__ == '__main__':
    main()