
# 定义个Person类 （类名通常使用：大驼峰写法）
class Person:
    # 初始化方法
    def __init__(self, name, age, gender):
        # 给示实例添加属性（语法为:self.属性名 = 值）
        self.name = name
        self.age = age
        self.gender = gender

# 创建Person类的实例对象
p1 = Person('张三',18,'男')
p2 = Person('李四',20,'女')
# 直接打印一个示例，返回的是地址
print(p1)

# 通过点语法可以访问或修改实例身上的属性
print(p1.name)
p2.age = 30
print(p2.age)

# 通过实例.__dict__可以查看实例身上的所有属性
print(p1.__dict__)

# 实例创建完毕后，依然可以通过 实例.属性名 = 值 去给实例追加属性
p1.address = '湖北省武汉市213'
print(p1.__dict__)

# 同过type函数，可以查看某个实例对象，是由哪个类创建出来的
print(type(p1))
