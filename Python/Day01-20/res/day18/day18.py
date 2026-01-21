'''
    面向对象
        类（class）: 某种通用事务的抽象定义，如动物
        对象（object）: 某种类的具体应用，如人
        封装（encapsulation）: 抽象通用操作
        继承（inheritance）: 类的细分，动物->人
        多态（polymorphism）:  子类重新定义父类的方法，比如喊叫（人），汪汪汪（狗）
'''

# 父类
class Animal:
    def __init__(self, name, age):
        '''初始化方法'''
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name} is eating')

    def call(self):
        print(f'{self.name} is calling')

    def show(self):
        print(f'{self.name} is {self.age} years old')


# 继承
class Person(Animal):
    def __init__(self, name, age, job):
        '''初始化方法'''
        super().__init__(name, age)
        self.job = job

    def call(self):
        print(f'{self.name} is calling, and yahouyahou~')

    def show(self):
        print(f'{self.name} is {self.age} years old')

    def work(self,job):
        print(f'{self.name} is working, and working on {job}')

class Cat(Animal):
    def __init__(self, name, age, color):
        '''初始化方法'''
        super().__init__(name, age)
        self.color = color

    def call(self):
        print(f'{self.name} is calling, and miamiamia~')

    def show(self):
        print(f'{self.name} is {self.age} years old')

    def color(self,color):
        print(f'{self.name} is working, and {color}')

if __name__ == '__main__':
    '''创建对象'''
    Tom = Person('Tom', 18, 'engineer')
    Mimi = Cat('Mimi', 2, 'white')

    # 封装
    Tom.eat()
    Mimi.eat()

    # 多态
    Tom.call()
    Mimi.call()