
# 变量类型注解：给变量加上类型说明，可增加代码的可读性。让IDE 的提示更友好
num: int = 100
price: float = 12.3
msg: str = '你好'
is_vip: bool = False
# 注意：可以先写变量的类型注解，以后再赋值
school: str
# 此时school变量才被创建
school = '学校'

# hobby 是列表，并且列表中的所有元素必须是 str类型
hobby: list[str] = ['1', '2', '3']

# hobby1 是列表，并且列表中的所有元素可以是 str 或者 int 类型
hobby1: list[str | int] = ['1', '2', '3', 100]
# 上面代码的旧写法如下：
from typing import Union

hobby2: list[Union[str, int]] = ['1', '2', '3', 100]

# city 是集合，并且集合中所有元素必须是 str类型
city: set[str] = {'hello', '你好'}

# city1 是集合，并且集合中所有元素可以是 str类型 、 float或者bool类型
city1: set[str | float | bool] = {'hello', '你好', 12.3, True}

# person 是字典，键是str类型 ，值是int 类型
person: dict[str, int] = {'张三': 10, '李四': 20}
# person1 是字典，键是str类型或int类型 ，值是int 类型
person1: dict[str | int, int] = {'张三': 10, '李四': 20, 1: 100}

# 元组的类型声明有点特殊，各位要留意一下：
# scores 是元组，不可变对象 并且元组中仅包含1个int类型的元素
scores: tuple[int] = (60,)
# scores1 中必须有一个是int类型，一个是str类型且顺序对应
scores1: tuple[int, str] = (60, '你好')
# sources2是元组，并且元组中包含任意int类型个数的元素
sources2: tuple[int, ...] = (70, 80, 90, 100)
# sources3是元组，并且元组中包含任意个数的元素，元素类型可以是int或者str
sources3: tuple[int | str, ...] = (70, 80, 90, 100, 'hello')

# 注意：Python会根据初始赋值推导变量类型
# 1、对于普通变量：后续如果改变类型，不会警告
# 2、对于数据容器：要求内部元素类型必须与推导出来的一致，否则就会警告
