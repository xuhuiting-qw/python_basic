# 1、迭代器是惰性计算，不会一次性生成所有结果，所以能显著降低内存占用
# 2、当数据量很大，不确定要用多少结果时，推荐使用迭代器

# 使用迭代器实现
class Fibo:
    def __init__(self,total):
        # 要生成多少个数
        self.total = total
        self.index = 0
        # 初始的两个值
        self.pre = 1
        self.cur = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >=self.total:
            raise StopIteration
        # 前两项都是1
        if self.index < 2:
            value = 1
        else:
            # 新的结果等于前两项的和
            value = self.pre + self.cur
            # 更新前两项
            self.pre = self.cur
            self.cur = value
        self.index +=1
        return value

f1 = Fibo(10)
result = [n for n in f1]
print(result)

# 不用迭代器实现
def fibo(total):
    if total <= 0:
        return []
    elif total == 1:
        return 1
    nums = [1,1]
    for i in range(2, total):
        value = nums[-1] + nums[-2]
        nums.append(value)
    return nums

print(fibo(10))



