'''
函数练习
'''

'''
例子1：随机验证码
设计一个生成随机验证码的函数，验证码由数字和英文大小写字母构成，长度可以通过参数设置。
'''
def random_code(code_len):
    import random
    import string

    if code_len <3 :
        print('长度不能小于3')
    else:
        '''
        choice return a single element
        sample return a list
        string.digits contains all numbers
        string.ascii_uppercase contains all uppercase letters
        string.ascii_lowercase contains all lowercase letters
        '''

        # choice  method
        result1 = [
            random.choice(string.digits)+
            random.choice(string.ascii_uppercase)+
            random.choice(string.ascii_lowercase)
        ]
        for i in range(code_len-3):
            result1.append(random.choice(string.digits+string.ascii_uppercase+string.ascii_lowercase))# append: add a single element
        print(f'use choice method :random.shuffle(result1):{random.shuffle(result1)}')# shuffle: 打乱列表

        # sample method
        result2 = []
        result2.extend(random.sample(string.digits,1))# extend: add a list
        result2.extend(random.sample(string.ascii_uppercase,1))
        result2.extend(random.sample(string.ascii_lowercase,1))
        remaining = random.sample(
            string.digits + string.ascii_uppercase + string.ascii_lowercase, code_len-3
        )
        result2.extend(remaining)
        print(f'use sample method :random.shuffle(result2):{random.shuffle(result2)}')

'''
例子3：最大公约数和最小公倍数
设计计算两个正整数最大公约数和最小公倍数的函数。
 x 和 y 的最大公约数是能够同时整除 x 和 y 的最大整数，
 如果 x 和 y 互质，那么它们的最大公约数为 1； x 和 y 的最小公倍数是能够同时被 x 和 y 整除的最小正整数，
 如果 x 和 y 互质，那么它们的最小公倍数为 x×y 。
 需要提醒大家注意的是，计算最大公约数和最小公倍数是两个不同的功能，应该设计成两个函数，而不是把两个功能放到同一个函数中。
'''
class MULTIPLE_NUMBER:
    # 最大公约数
    def greatest_common_divisor(self, x: int, y: int)->int:
        self.x = x
        self.y = y

        # 辗转相除法
        while y != 0:
            x, y = y, x % y
        return x

        pass

    # 最小公倍数
    def greatest_common_multiple(self, x: int, y: int)->int:
        self.x = x
        self.y = y

        #
        return x * y // self.greatest_common_divisor(x, y)

        pass


'''
例子5：双色球随机选号
我们用函数重构之前讲过的双色球随机选号的例子（《第09课：常用数据结构之列表-2》），
将生成随机号码和输出一组号码的功能分别封装到两个函数中，然后通过调用函数实现机选N注号码的功能。
'''
import random
class two_color_balls:
    """双色球随机选号"""
    red_balls = [i for i in range(1,33)]
    blue_balls = [i for i in range(1,17)]

    def choose_numbers(self,balls:list, num:int)->list:
        result = random.sample(balls, num)
        result.sort()
        return result

    def display(self):
        """输出一组双色球号码"""
        select_red_balls = self.choose_numbers(self.red_balls, 6)
        select_blue_balls = self.choose_numbers(self.blue_balls, 1)

        print(f'{select_red_balls} | {select_blue_balls}')
        return select_red_balls, select_blue_balls
    pass

if __name__ == '__main__':
    # random_code(5)
    # print(f'MULTIPLE_NUMBER().greatest_common_divisor(12, 8):{MULTIPLE_NUMBER().greatest_common_divisor(12, 8)}\n'
    #       f'MULTIPLE_NUMBER().greatest_common_multiple(12, 8):{MULTIPLE_NUMBER().greatest_common_multiple(12, 8)}')
    print(f'two_color_balls().display(): {two_color_balls().display()}\n')

    pass
