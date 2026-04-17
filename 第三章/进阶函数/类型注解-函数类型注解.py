
# 函数类型注解：给函数的参数和返回值添加说明
# 语法格式：函数名(参数1:类型,参数2:类型) -> 返回值类型：

# 示例1、设置参数类型注解，设置返回值类型注解
def add(x: int, y: int) -> int:
    return x + y

# 示例2、参数有默认值(python可以推导出参数的类型)、设置返回值类型
def add1(x=1, y=1) -> int:
    return x + y

# 示例3:设置多个返回值的类型注解
def show_nums_indo(nums: list[int]) -> tuple[int, int, float]:
    max1 = max(nums)
    min1 = min(nums)
    result = max1 / min1
    return max1, min1, result

# 示例4: 设置 *args 的类型注解，每个元素是int类型
def add2(*args: int) -> int:
    return sum(args)

# 示例5: 设置 **kwargs 的类型注解，每组参数的值必须是str或者int类型
def show_info(**kwargs: str | int):
    print(kwargs)

# 获取函数的注解信息
print(add.__annotations__)
