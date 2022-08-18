"""
1.从控制台输入要出的拳——石头(1)/剪刀(2)/布(⑶)
2.电脑随机出拳——先假定电脑只会出石头，完成整体代码功能
3.比较胜负

序号	规则
1	石头胜剪刀
2	剪刀胜布
3	布胜石头
"""
import random


player = int(input("请选择：石头(1)/剪刀(2)/布(⑶)"))
computer = random.randint(1, 3)

print("玩家出 %d - 电脑出 %d" % (player, computer))
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):  # 阅读方便 在所有条件外增加括号，再加换行
    print("player win")
elif player == computer:
    print("double win")
else:
    print("computer win")
