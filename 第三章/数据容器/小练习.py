

# 练习一、水果清单
fruits = {
    '苹果':4.5,
    '香蕉':3.2,
    '橙子':5.8,
    '草莓':12.0,
    '哈密瓜':8.8
}
# 1、打印所有水果
for key in fruits:
    print(f'{key} : {fruits[key]}元/斤')
# 2、找到最贵水果
print(max(fruits, key = fruits.get))
print()

# 需求二：学生成绩表
students = [
    {
        'name':'张三',
        'scores':{'语文':88,'数学':92,'英语':95}
    },
    {
        'name':'李四',
        'scores':{'语文':75,'数学':83,'英语':80}
    },
    {
        'name':'王五',
        'scores':{'语文':92,'数学':95,'英语':88}
    },
]
# 1、计算每位学生的平均分
for item in students:
    scores = item['scores']
    avg = sum(scores.values()) / len(scores)
    print(f'学生：{item['name']}的平均分是：{avg:.2f}')
# 2、找到总分最高的学生
best_stu = []
best_score = 0
for item in students:
    total = sum(item['scores'].values())
    if total > best_score:
        best_stu = [item['name']]
        best_score = total
    elif total == best_score:
        best_stu.append(item['name'])
print(f'最高分是：{best_score},学生为：{best_stu}')
print()

# 需求三：评论内容
comment = '这家奶茶真好喝，环境也不错，就是价格有点贵，好喝好喝好喝！强烈推荐！'
# 1、统计'好喝'出现的次数
print(comment.count('好喝'))
# 2、将字符串中的'贵'替换为'略高'
print(comment.replace('贵','略高'))
# 3、是否包含'推荐'两个字
print('推荐' in comment)



