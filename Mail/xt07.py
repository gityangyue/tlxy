# 写一个程序来管理用于登陆系统的用户信息：
# 登陆名字和密码
#已存在用户可以用登录名和密码重返系统
#新用户不能用别人的用户名建立用户账号。

#模拟从数据库里取出来的用户名和密码
user_pass = {"laotie":"password",
             "huniu":"admin"
             }
def create_user(username,passwd):
# User name ：用户提交的用户名
# passwd : 用户提交的密码
    # 判断提交的用户名是否存在
    if username in user_pass.keys():
        print("这个用户已经被注册了")
    else:
        user_pass[username] = passwd
        print("恭喜，注册成功")


create_user("岳洋","password")

print(i for i in user_pass)