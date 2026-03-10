"""
🎮 猜数字游戏
难度：★ 入门级
知识点：变量、输入输出、条件判断、循环
"""
import random

# 随机生成1-100的秘密数字
secret_number = random.randint(1, 100)
print("🤖 我想了一个1到100之间的数字，你来猜猜看吧！")
print("💡 提示：输入数字后按回车，我会告诉你太大还是太小哦～\n")

guess_count = 0  # 记录猜的次数

while True:
    # 获取用户输入
    user_input = input("请输入你猜的数字：")
    
    # 检查输入是不是数字
    if not user_input.isdigit():
        print("❌ 请输入有效的数字哦！")
        continue
    
    guess = int(user_input)
    guess_count += 1
    
    # 判断大小
    if guess < secret_number:
        print("📉 太小啦！再试试大一点的数字～")
    elif guess > secret_number:
        print("📈 太大啦！再试试小一点的数字～")
    else:
        print(f"\n🎉 恭喜你猜对啦！秘密数字就是 {secret_number}")
        print(f"👏 你一共猜了 {guess_count} 次，真棒！")
        break

# 扩展玩法：
# 1. 可以设置最大猜测次数，比如最多猜10次
# 2. 可以加入双人对战模式，两个人轮流猜
# 3. 可以把数字范围改成1-1000，增加难度
