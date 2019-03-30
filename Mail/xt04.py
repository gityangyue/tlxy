#!/usr/local/bin/python3.6
def auth(realpw):
    csq = 0
    while True:
        passwd = input('请输入密码:')
        passwd = str(passwd)
        if "*" in passwd:
            print('您输入的密码有误，请再次输入')
            continue
        else:
            if passwd == realpw:
                print('恭喜，您的密码对了')
                break
            else:
                if csq < 3:
                    csq += 1
                    print('密码错了，重新输入')
                else:
                    print('抱歉，三次机会已经用完。无法登陆')
                    break

if __name__ == '__main__':
    realpw = "141234123qwe"
    auth(realpw)