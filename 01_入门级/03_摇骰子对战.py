"""
🎲 摇骰子对战游戏
难度：★ 入门级
知识点：函数、随机数、比较运算
"""
import random

def roll_dice():
    """摇骰子，返回1-6的随机数"""
    return random.randint(1, 6)

print("🎲 摇骰子对战游戏！看看谁的点数大！")
print("🤝 规则：你和爸爸轮流摇骰子，点数大的赢，平局就再来一局～\n")

player_score = 0  # 玩家分数
dad_score = 0     # 爸爸分数
round_num = 1     # 第几局

while True:
    print(f"=== 第 {round_num} 局 ===")
    input("👉 按回车开始摇骰子...")
    
    player = roll_dice()
    dad = roll_dice()
    
    print(f"🎯 你摇到了：{player} 点")
    print(f"🎯 爸爸摇到了：{dad} 点\n")
    
    if player > dad:
        print("🎉 你赢啦！太棒了！")
        player_score += 1
    elif player < dad:
        print("😝 爸爸赢啦！再接再厉哦～")
        dad_score += 1
    else:
        print("🤝 平局！再来一局！")
    
    print(f"\n📊 当前比分：你 {player_score} : {dad_score} 爸爸")
    
    # 问要不要继续
    play_again = input("\n还要继续玩吗？(y/n)：").lower()
    if play_again != 'y' and play_again != 'yes':
        print(f"\n🏁 游戏结束！最终比分：你 {player_score} : {dad_score} 爸爸")
        if player_score > dad_score:
            print("🏆 你是最终的胜利者！真棒！")
        elif player_score < dad_score:
            print("💪 没关系，下次再赢回来！")
        else:
            print("🤝 打成平手！下次再分胜负～")
        break
    
    round_num += 1
    print("\n")

# 扩展玩法：
# 1. 可以改成2个骰子，点数相加
# 2. 可以加豹子规则：两个骰子一样的话直接赢
# 3. 可以加入更多玩家，比如妈妈也一起玩
