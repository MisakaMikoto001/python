"""
例子2：工资结算系统。
    要求：某公司有三种类型的员工，分别是部门经理、程序员和销售员。
    需要设计一个工资结算系统，根据提供的员工信息来计算员工的月薪。
        其中，部门经理的月薪是固定 15000 元；
        程序员按工作时间（以小时为单位）支付月薪，每小时 200 元；
        销售员的月薪由 1800 元底薪加上销售额 5% 的提成两部分构成。
"""
from abc import abstractmethod, ABCMeta


class Employee(metaclass=ABCMeta):
    """员工"""

    def __init__(self):
        self.name = ''
        self.pay = 0

    @abstractmethod # 抽象方法
    def get_pay(self):
        """计算月薪"""
        pass

class Manger(Employee):
    """部门经理"""

    def __init__(self):
        super().__init__()
        self.pay = 15000

    def get_pay(self):
        """计算月薪"""
        return self.pay

class Programmer(Employee):
    """程序员"""

    def __init__(self,work_hours):
        super().__init__()
        self.work_hours = work_hours

    def get_pay(self):
        """计算月薪"""
        return self.work_hours * 200


class Salesman(Employee):
    """销售员"""

    def __init__(self, sales):
        super().__init__()
        self.sales = sales

    def get_pay(self):
        """计算月薪"""
        return 1800 + self.sales * 0.05

def main():
    """主函数"""
    manger = Manger()
    programmer = Programmer(400)
    salesman = Salesman(50000)
    print(f'部门经理的月薪是：{manger.get_pay()}')
    print(f'程序员的月薪是：{programmer.get_pay()}')
    print(f'销售员的月薪是：{salesman.get_pay()}')

if __name__ == '__main__':
    main()