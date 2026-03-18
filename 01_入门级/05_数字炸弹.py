"""
💣 数字炸弹游戏
难度：★ 入门级
知识点：随机数、循环、条件判断、用户输入
玩法：系统随机生成一个1-100的炸弹数字，玩家猜，系统提示变大变小，直到猜中爆炸
"""
import random

print("💣 数字炸弹游戏！")
print("系统会随机生成一个1-100之间的秘密数字，你来猜，我告诉你太大还是太小")
print("猜到炸弹你就输了！\n")

# 生成秘密炸弹数字
secret_num = random.randint(1, 100)
min_num = 1
max_num = 100
guesses = 0

while True:
    # 获取玩家输入
    try:
        guess = int(input(f"请猜一个{min_num} - {max_num} 之间的数字："))
        guesses += 1
        
        if guess < min_num or guess > max_num:
            print(f"超出范围了哦，请输入{min_num} - {max_num} 之间的数字！")
            continue
            
        if guess == secret_num:
            print(f"\n💥 BOOM! 你猜中炸弹了！")
            print(f"游戏结束！你一共猜了{guesses}次")
            break
        elif guess < secret_num:
            print("🔼 太小了！再猜大一点")
            min_num = guess
        else:
            print("🔽 太大了！再猜小一点")
            max_num = guess
            
    except ValueError:
        print("请输入有效的数字哦！")
