"""
    创建北京和成都两个校区
    创建Linux\Python 两个课程
    创建北京小区的python 3期课程和成都校区的Linux 1期课程
    管理员创建了北京校区的学员小张，并将其分配在了python 3期中。
    管理员创建了讲师小周，并将其分配给了 python 3期
    讲师小周创建了一条 Python 3期的上课记录 Day02
    讲师小周为DDay02这节课所有的学员批改了作业，小张得了A,小王得了B
    学员小张查看了自己所报的课程
    学员小张在查看了自己在python3的成绩列表然后退出了
    学员小张给了讲师小周好评
"""

# 课程列表
course_list = []
stu_num_id = 00
tea_num_id = 00

#创建 学校类
class School(object):
    def __init__(self, school_name):
        self.school_name = school_name
        self.students_list = []
        self.teachers_list = []
        #self.site = school_site
        global course_list

#添加学生方法。student是一个list,包含学生的各个信息[姓名，年龄，]
    def add_students(self, obj):
        self.students_list.append(obj.name)
        print("{}校区现在有了一个新学员{}".format(self.name, obj.name))

    def add_teacher(self,obj):
        self.teachers_list.append(obj.name)
        print("{}校区聘请了一个新老师{}".format(self.school_name, obj.name))


class Grade(School):

    def __init__(self, school_name, grade_code, grade_course):
        super(Grade,self).__init__(school_name)
        self.code = grade_code
        self.course = grade_course
        self.members = []
        course_list.append(self.course)
        print("我们现在有了在{}校区的{}期的{}课程".format(self.school_name, self.code, self.course))

    def course_info(self):
        print("{}课程的大纲为：".format(self.course))
        for i in range(1, int(self.code)):
            print("Day" + str(i).zfill(3) + " ,",end = "")


class SchoolMember(object):

    def __init__(self, name, age, sex, role):
        self.name = name
        self.age =age
        self.sex = sex
        self.role = role
        self.course_list = []
        print("我是{},一个{}".format(self.name, self.role))


class Student(SchoolMember):
    def __init__(self, name, age, sex, role, course):
        super(Student, self).__init__(name, age, sex, role)
        global stu_num_id
        stu_num_id += 1
        stu_id = course.school_name + "S" + str(course.code) + str(stu_num_id).zfill(2)
        self.id = stu_id
        self.mark_list = {}

    def study(self, course):
        print("{}学习了{}课程，学号是{}".format(self.name, course.course, self.id))

    def pay(self, course):
        self.course_list.append(course.course)
        print("{}付费了{}课程".format(self.name, course.course))

    def praise(self,course):
        print("{}点赞了{}，觉得这个课真棒".format(self.name, course.course))

    def mark_check(self):
        print("{}参与的课程为：".format(self.name))
        for i in self.mark_list.items():
            print(i)

    def out(self):
        print("{}离开了".format(self.name))


class Teacher(SchoolMember):

    def __init__(self, name, age, sex, role, course):
        super().__init__(name, age, sex, role)
        global tea_num_id
        tea_num_id += 1
        tea_id = course.school_name + "T" + str(course.code) + str(tea_num_id).zfill(2)
        self.id = tea_id

    def teach(self, course):
        print("{}来讲{}课，我得ID是{}".format(self.name, course.course, self.id))

    def record_mark(self, date, course, obj, level):
        obj.mark_list["Day" + date] = level


grade_python = Grade("北京", 5, "Python")
grade_linux = Grade("成都", 1, "Linux")
xiaozhang = Student("小张", 18, "男", "学生",  )
a.course_info()