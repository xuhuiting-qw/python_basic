# # 迭代器是一次性的，状态只会向前推进，且不会自动重置(迭代器在遍历的过程中会被“消耗”)
from cn2an import cn2an, an2cn


names = ['张三','李四','王五']

# 需求：让for循环可以遍历Person的实例对象
# 实现方式一
class Person:
    def __init__(self,name,age,gender,address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address

    def __iter__(self):
        return PersonIterator(self)


# 迭代器对象
class PersonIterator:
    def __init__(self, p):
        # 将外部传进来的数据保存好
        self.p = p
        # 设置一个迭代器的初始状态(指针状态)
        self.index = 0
        # 配置好要遍历的内容
        self.attrs = [p.name,p.age,p.gender,p.address]

    # 迭代器的__iter__ 方法会返回自身
    def __iter__(self):
        return self

    # 迭代器的next方法  会根据当前的状态，返回下一个元素
    def __next__(self):
        if self.index >=len(self.attrs):
            raise StopIteration
        #获取要返回的内容
        value = self.attrs[self.index]
        # 更新迭代器的状态
        self.index += 1
        # 返回元素
        return value

p1 = Person('张三',20,'男','湖北武汉')
for item in p1:
    print(item)
print()

# 实现方式二
class Person:
    def __init__(self,name,age,gender,address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        # 设置一个迭代器的初始状态(指针状态)
        self.__index = 0
        # 配置好要遍历的内容
        self.__attrs = [name, age, gender, address]

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index >=len(self.__attrs):
            raise StopIteration
        #获取要返回的内容
        value = self.__attrs[self.__index]
        # 将返回中的字符串变成大写
        if isinstance(value,str):
            value = value.upper()
        if isinstance(value, int):
            # 将 数字变成汉字的数字
            value = an2cn(value)
        # 更新迭代器的状态
        self.__index += 1
        # 返回元素
        return value

p2 = Person('李四',27,'男','湖北武汉')
for item in p2:
    print(item)

