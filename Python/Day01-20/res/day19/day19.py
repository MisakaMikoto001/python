"""
    面向对象
        类（class）: 某种通用事务的抽象定义，如动物
        对象（object）: 某种类的具体应用，如人
        封装（encapsulation）: 抽象通用操作
        继承（inheritance）: 类的细分，动物->人
        多态（polymorphism）:  子类重新定义父类的方法，比如喊叫（人），汪汪汪（狗）
"""

'''
    可见属性
    属性装饰器
'''

# 父类
class Animal:
    def __init__(self, name, age, private, protected):
        """初始化方法"""
        self.name = name
        self.age = age
        self.__private = private
        self._protected = protected

    def eat(self):
        print(f'{self.name} is eating')

    def call(self):
        print(f'{self.name} is calling')

    def show(self):
        print(f'{self.name} is {self.age} years old')


# 继承
class Person(Animal):
    def __init__(self, name, age, job):
        """初始化方法"""
        super().__init__(name, age,'private', 'protected')
        self.job = job

    def call(self):
        print(f'{self.name} is calling, and yahouyahou~')

    def show(self):
        print(f'{self.name} is {self.age} years old')

    def work(self,job):
        print(f'{self.name} is working, and working on {job}')

class Cat(Animal):
    # 禁止动态属性
    __slots__ = ('name', 'age')# 只能是这两个属性，不能添加其他属性

    def __init__(self, name, age, color):
        """初始化方法"""
        super().__init__(name, age, 'private', 'protected')
        self.ani_color = color

    def call(self):
        print(f'{self.name} is calling, and miamiamia~')

    def show(self):
        print(f'{self.name} is {self.age} years old')

    def color(self,color):
        print(f'{self.name} is working, and {color}')


# 静态方法与类方法
class STATIC_METHOD(Animal):
    # 类属性
    address = 'beijing'

    def __init__(self,name,age,address):
        """初始化方法，实例属性"""
        super().__init__(name, age, 'private', 'protected')
        self.address = address

    def call(self):
        print(f'{self.name} is calling')

    @staticmethod
    def static_method(param1,param2):
        """
        定义方式：使用@staticmethod
        参数特点：不接收隐式self或者cls参数
        调用方式：可通过类名或实例调用
        使用场景：与类相关但不访问类或者示例数据
        """
        # print(f'{self.name} is calling')# AttributeError: 'STATIC_METHOD' object has no attribute 'name'
        return param1 + param2

    @classmethod
    def class_method(cls):
        """
        定义方式：使用@classmethod装饰器
        参数特点：第一个参数是cls（指向类）
        调用方法：通过类名或者实例调用
        使用场景：需要访问类属性或者创建类实例
        """
        print(f'{cls.__name__} is {cls.address}')
    pass

print(f'STATIC_METHOD.static_method(1,2)：{STATIC_METHOD.static_method(1,2)}')
STATIC_METHOD.class_method()

def FUNC():
    """访问隐私、保护、公开属性"""
    Tom = Person('Tom', 18, 'engineer')

    # 公有属性
    print(f'Tom.name: {Tom.name}')
    # 保护属性
    print(f'Tom._protected: {Tom._protected}')
    # 私有属性
    # print(f'Tom.__private: {Tom.__private}')#AttributeError: 'Person' object has no attribute '__private'


def Create_class():
    """创建对象"""
    Tom = Person('Tom', 18, 'engineer')
    Mimi = Cat('Mimi', 2, 'white')

    # 封装
    Tom.eat()
    Mimi.eat()

    # 多态
    Tom.call()
    Mimi.call()

    #动态属性
    Tom.sex = 'male'#增加sex属性
    print(f'Tom.sex: {Tom.sex}')
    # 禁止动态属性 ：__slots__ = ('name', 'age', 'color')
    Mimi.sex = 'female'
    # print(f'Mimi.sex: {Mimi.sex}')#ValueError: 'color' in __slots__ conflicts with class variable

    pass

if __name__ == '__main__':
    # Create_class()
    # FUNC()

    pass