"""
🎲 随机抽签器
难度：★ 入门级
知识点：列表、随机数、用户输入
用法：输入一堆候选人，随机抽一个出来，适合决定谁洗碗、看什么电影
"""
import random

print("🎲 随机抽签器")
print("请输入候选人名单，每行一个名字，输入空行结束开始抽签\n")

# 读取所有候选人
names = []
while True:
    name = input("请输入名字：")
    if name.strip() == "":
        break
    if name.strip() not in names:
        names.append(name.strip())

if len(names) == 0:
    print("还没有输入任何人呢！")
    exit()

print(f"\n一共 {len(names)} 位候选人：{', '.join(names)}")
input("按回车开始抽签...")

# 抽签
winner = random.choice(names)
print(f"\n🎉 抽中了：【 {winner} 】")
print("\n恭喜！今天洗碗就归你啦～😁")
