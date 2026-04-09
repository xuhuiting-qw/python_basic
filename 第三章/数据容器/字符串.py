

# 常用方法
str1 = 'welcome@to@python!'
# 1、index 方法，获取指定字符，在字符串中第一次出现的下标
print(str1.index('t'))
# 2、count方法，获取指定元素出现的次数
print(str1.count('t'))
# 3、split方法，根据指定字符分割，并将分割后的内容存入一个新列表
result1 = str1.split('@')
print(result1,type(result1))
# 4、replace方法，将字符串中的某个字符片段替换成目标字符串，返回新字符串
result2 = str1.replace('@to@','你好')
print(str1)
print(result2)
# 5、strip 方法 ，从某个字符串中删除:指定字符串中的任意字符
# 规则：从字符串两端开始删除，直到遇到第一个不在字符串中的字符就停下
msg = '5362你1好2啊3966'
result3 = msg.strip('5936')
print(result3)

print()


# 常用内置函数
# len函数，返回字符串长度
msg1 = 'hello'
print(len(msg1))

