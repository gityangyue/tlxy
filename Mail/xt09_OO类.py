'''
定义一个学生类，有下面的类属性
1、姓名
2、年龄
3、成绩（语文，数学，英语）每课成绩类型为整数类方法
4、获取学生的姓名：get_name() 返回类型：str
5、获取学生的年纪：get_age() 返回类型：int
6、返回3门科目中最高的分数，get_course()返回类型：init
'''

class Student():
    def __init__(self, name, age, scores):
        self.name = name
        self.age = age
        self.scores = scores

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_scoures(self):
        return max(self.scores)

#s = Student("小明", 16, [100,99,105])
#print(s.get_name())
#print(s.get_age())
#print(s.get_scoures())

'''
定义一个字典类：DictClass完成如下功能：
1、删除某个key, del_dict(key)
2、判断某个键是否在字典里。如果在，返回键对应的值；不在则返回 not found .get_dict()
3、返回键组成的列表，返回类型：list_get(key)
4、合并字典，并且反馈合并后字典的values组成的列表，返回类型list update_dict()
'''

class DictClass():
    def __init__(self,dict):
        self.dict = dict

    def del_dict(self,key):
        if key in self.dict.keys():
            self.dict.pop(key)
            return "删除成功"
        else:
            return "Not Found"

    def get_dict(self, key):
        if key in self.dict.keys:
            return self.dict[key]
        else:
            return "Not Found"

    def get_key(self):
        return self.dict.keys()

    def update_dict(self,dict2):
        self.dict.update(dict2)
        return self.dict.values()

d = DictClass({"a":90, "b":91, "c":100})
print(d.update_dict({"d":200}))