import card_tool

while True:
    # TODO
    card_tool.welcome()
    action_str = input("请输入选择")
    if action_str in ["1", "2", "3"]:
        if action_str == "1":
            card_tool.init()
        elif action_str == "2":
            card_tool.show()
        else:
            card_tool.find(input("输入姓名"))

    elif action_str == "0":
        break
    else:
        print("错误，失败")
