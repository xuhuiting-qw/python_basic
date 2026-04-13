from datetime import datetime


# 学生管理
# 1、添加学生
# 2、删除学生
# 3、查看所有学生
# 4、录入成绩
# 5、退出

class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

class Student(Person):
    # 计数器
    count = 0
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        Student.count += 1
        self.stu_id = f'{datetime.now().year}{Student.count:03d}'   # 03d--- 三位数不够则用0补齐
        self.scores = {}
    # 录入成绩
    def add(self,subject,score):
        self.scores[subject] = score

    #  计算平均分
    def avg(self):
        if self.scores:
            return sum(self.scores.values()) / len(self.scores)
        else:
            return 0

    # 魔法方法
    def __str__(self):
        return  f'{self.name}-{self.age}-{self.gender}-{self.stu_id},成绩是{self.scores}，平均分是{self.avg()}'

class Manager:
    def __init__(self):
        self.stu_list = []

    # 添加学生
    def add_stu(self):
        name = input('请输入姓名：')
        age = int(input('请输入年龄：'))
        gender = input('请输入性别：')
        stu = Student(name, age, gender)
        self.stu_list.append(stu)
        print(f'添加成功！学号是{stu.stu_id}')

    #  删除学生
    def del_stu(self):
        sid = input('请输入删除学号：')
        del_sid = None
        for stu in self.stu_list:
            if stu.stu_id == sid:
                del_sid = stu
                break
        if del_sid:
            self.stu_list.remove(del_sid)
            print('删除成功')
        else:
            print('学号不存在，请重新确认输入学号')

    # 查看所有学生
    def all_stu(self):
        if self.stu_list:
            for stu in self.stu_list:
                print(stu)
        else:
            print('暂无学生！')

    # 录入成绩
    def set_score(self):
        sid= input('请输入学号：')
        for stu in self.stu_list:
            if stu.stu_id == sid:
               scores = input('请输入学生成绩，示例【学科-分数，学科-分数】：')
               l1 = scores.replace('，',',').split(",")
               for s in l1:
                   subject, score = s.split('-')
                   subject = subject.strip()
                   score = float(score.strip())
                   stu.add(subject,score)
            print('添加成功！')
            return
        print('添加失败，学号有误！')

    def run(self):
        while True:
            print('学生管理')
            print('1、添加学生')
            print('2、删除学生')
            print('3、查看所有学生')
            print('4、录入成绩')
            print('5、退出')

            choice = input('请输入操作编号：')
            if choice == '1':
                self.add_stu()
            elif choice == '2':
                self.del_stu()
            elif choice == '3':
                self.all_stu()
            elif choice == '4':
                self.set_score()
            elif choice == '5':
                print('退出！')
                break
            else:
                print('输入有误！')

Manager().run()



