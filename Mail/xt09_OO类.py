"""
定义一个学生类，有下面的类属性
1、姓名
2、年龄
3、成绩（语文，数学，英语）每课成绩类型为整数类方法
4、获取学生的姓名：get_name() 返回类型：str
5、获取学生的年纪：get_age() 返回类型：int
6、返回3门科目中最高的分数，get_course()返回类型：init

"""


class Student(object):

    def __init__(self, name, age, scores):
        #需要提供的三个参数，name,age,scores
        #name : 字符
        #age : int
        #scores: list
        self.name = name
        self.age = age
        self.scores = scores

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_scores(self):
        return max(self.scores)

#s = Student("小明", 16, [100,99,105])
#print(s.get_name())
#print(s.get_age())
#print(s.get_scores())


'''
定义一个字典类：DictClass完成如下功能：
1、删除某个key, del_dict(key)
2、判断某个键是否在字典里。如果在，返回键对应的值；不在则返回 not found .get_dict()
3、返回键组成的列表，返回类型：list_get(key)
4、合并字典，并且反馈合并后字典的values组成的列表，返回类型list update_dict()
'''


class DictClass(object):
    def __init__(self,dict1):
        #需要提供的参数，一个字典类型的dict1
        self.dict = dict1

    def del_dict(self, key):
        #key 表示需要删除的key
        if key in self.dict.keys():
            self.dict.pop(key)
            return "删除成功"
        else:
            return "Not Found"

    def get_dict(self, key1):
        #key1表示需要判断的key
        if key1 in self.dict.keys:
            return self.dict[key1]
        else:
            return "Not Found"

    def get_key(self):
        return self.dict.keys()

    def update_dict(self,dict2):
        #dict2标识需要合并的dict
        self.dict.update(dict2)
        return self.dict.values()


#d = DictClass({"a": 90, "b": 91, "c": 100})
#print(d.update_dict({"d":200}))

'''
定义一个列表得操作类 ListInfo
包括方法
    1、列表元素添加 ：add_key()
    2、列表元素取值 ：get_key()
    3、列表合并     ：update_list(list)
    4、删除并返回最后一个元素：del_key()
'''


class ListInfo(object):
    def __init__(self, list_val):
        #list1表示需要操作的List，
        self.list = list_val

    def add_key(self, key_name):
        #key表示需要添加的值
        #添加的key必须是字符串或者数字
        if isinstance(key_name, (str, int)):
            self.list.append(key_name)
            return "添加成功"
        else:
            return "没那么牛X，目前只支持数字和字符"

    def get_key(self, index):
        #no表示相应的list 值的序号
        #判断传入的索引是否超出了列表
        if index < 0:
            return "哥们，序号别用负数"
        if 0 <= index < len(self.list):
            return self.list[index]
        if index > len(self.list):
            return "序号只到{0}".format(len(self.list)-1)
    def update_list(self, list2):
        #list2是需要合并的list
        self.list.extend(list2)
        return self.list

    def del_key(self):
        #删除最后一个
        self.list.pop()
        return self.list[-1]


#l1 = [1, 2, 3, 4, "a", "b", "c", "d"]
#instance = ListInfo(l1)
#print(instance.add_key(6))
#print(instance.get_key(9))


'''
定义一个集合的操作类 
包括的方法：
    1、集合元素添加：add_setinfo()
    2、集合的交集：get_intersection()
    3、集合的并集：get_union()
    4、集合的差集：del_difference()
'''

class SetInfo(object):
    def __init__(self, my_set):
        if isinstance(my_set, set):
            self.set=my_set
        else:
            #print("传入的数据必须是集合")
            raise TypeError("传入的数据必须是集合")


    def add_setinfo(self, key):
        if isinstance(key, (str, int)):
            self.set.add(key)
            return "添加成功"
        else:
            return "只允许输入字符和数字"

    def get_intersection(self, my_set2):
        if isinstance(my_set2, set):
            return self.set & my_set2
        else:
            return "你传入的不是set"
    def get_union(self, my_set2):
        if isinstance(my_set2, set):
            return self.set | my_set2
        else:
            return "你传入的不是set"

    def del_difference(self, my_set2):
        if isinstance(my_set2, set):
            return self.set - my_set2
        else:
            return "你传入的不是集合"


"""
my_set = SetInfo([1, 2, 3, 4, 5, 6])
my_set2 = {0, 9, 8, 7, 5}
print(my_set.add_setinfo(9))
print(my_set.set)
#print(my_set.set)
"""


