import copy

# 直接赋值：两个变量指向同一个对象，修改其中一个，就会影响另一个
nums1 = [10,20,30]
nums2 = nums1
nums2[2] = 99
print(nums2,id(nums2))
print(nums1,id(nums1))
print()
# 浅拷贝：创建一个新的外层容器，但内部元素仍然引用原来的对象
nums3 = [20, 50, 99]
nums4 = copy.copy(nums3)
nums4[2] = 100
print(nums3, id(nums3))
print(nums4, id(nums4))
print()
# 浅拷贝存在的问题，嵌套数据仍然是共享的，修改嵌套数据会互相影响
nums5 = [20, 50, [55, 66]]
nums6 = copy.copy(nums5)
nums6[2][0] = 100
print(nums6, id(nums6))
print(nums5, id(nums5))
print()

# 深拷贝:创建一个新的外层容器，并对其内部所有的【可变子对象】进行递归复制
# 备注：
# 1、深拷贝可以彻底消除数据之间的相互影响
# 2、深拷贝遇到 不可变对象 不会复制，会直接引用
nums7 = [20, 50, [55, 66]]
nums8 = copy.deepcopy(nums7)
nums8[2][1] = 99
print(nums8,id(nums8))
print(nums7,id(nums7))

# 注意点：
# 1、深拷贝只复制可变对象，不可变对象会直接引用
# 2、元组中如果只包含不可变对象，则深拷贝没有效果

