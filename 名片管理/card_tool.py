# 综合应用--名片管理系统
# 系统需求
# 1.程序启动，显示名片管理系统欢迎界面，并显示功能菜单
# *********************************************
# 欢迎使用【名片管理系统】V1.0
# 1.新建名片
# 2.显示全部
# 3.查询名片
# 0.退出系统
#  *********************************************
# 2.用户用数字选择不同的功能
# 3.根据功能选择，执行不同的功能
# 4.用户名片需要记录用户的姓名、电话、QQ、邮件
# 5.如果查询到指定的名片，用户可以选择修改或者删除名片

arr = []


def init():
    temp = {"name": input("请输入姓名"), "tel": input("请输入电话"), "qq": input("请输入QQ"), "email": input("请输入邮箱")}
    arr.append(temp)
    print("添加成功")


def show():
    if len(arr) == 0:
        print("无名片")
        return
    # 打印表头
    for name in ["name","tel","qq","email"]:
        print(name,end="\t\t")
    print("")
    print("="*50)
    for i in arr:
        print("%s\t\t%s\t\t%s\t\t%s" % (i["name"],
                                        i["tel"],
                                        i["qq"],
                                        i["email"]))

def input_info(m,n):
    """输入名片信息

    :param m:字典原有值
    :param n:提示信息
    :return:返回值
    """
    r = input(n)
    if len(r) > 0:
        return r
    else:
        return m



def deal(i):
    """
    处理查找到的名片
    :param i: 名片
    """
    y = int(input("修改按1 删除按2 无需求按0"))
    if y == 1:
        print("回车不修改")
        i["name"] = input_info(i["name"],"请输入姓名")
        i["tel"] = input_info(i["tel"],"请输入电话")
        i["qq"] = input_info(i["qq"],"请输入QQ")
        i["email"] = input_info(i["email"],"请输入邮箱")
    elif y == 2:
        arr.remove(i)


def find(x):
    flag = 0
    for i in arr:
        if i["name"] == x:
            print("找到了")
            print(i)
            deal(i)
            break

    else:
        print("不存在")


def welcome():
    print("*" * 50)
    print("欢迎使用【名片管理系统】V1.0")
    print("1.新建名片")
    print("2.显示全部")
    print("3.查询名片")
    print("0.退出系统")
    print("*" * 50)
