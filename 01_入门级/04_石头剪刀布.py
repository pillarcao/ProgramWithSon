"""
✊ 石头剪刀布游戏
难度：★ 入门级
知识点：随机数、列表、条件判断
"""
import random

# 定义手势
gestures = ['石头', '剪刀', '布']
# 规则：key 赢 value
win_rules = {
    '石头': '剪刀',
    '剪刀': '布',
    '布': '石头'
}

print("✊ 石头剪刀布游戏！和爸爸对战～")
print("规则：石头赢剪刀，剪刀赢布，布赢石头\n")

player_score = 0
computer_score = 0
round_num = 1

while True:
    print(f"=== 第 {round_num} 局 ===")
    print("请选择：1-石头 2-剪刀 3-布")
    
    # 获取玩家选择
    while True:
        choice = input("请输入数字1/2/3：")
        if choice in ['1', '2', '3']:
            player_choice = gestures[int(choice)-1]
            break
        else:
            print("❌ 输入不对哦，请输入1、2、3中的一个！")
    
    # 电脑随机选择
    computer_choice = random.choice(gestures)
    
    print(f"\n你出了：{player_choice}")
    print(f"爸爸出了：{computer_choice}\n")
    
    # 判断结果
    if player_choice == computer_choice:
        print("🤝 平局！")
    elif win_rules[player_choice] == computer_choice:
        print("🎉 你赢啦！")
        player_score += 1
    else:
        print("😝 爸爸赢啦！")
        computer_score += 1
    
    print(f"\n📊 当前比分：你 {player_score} : {computer_score} 爸爸")
    
    # 要不要继续
    again = input("\n还要继续玩吗？(y/n)：").lower()
    if again != 'y' and again != 'yes':
        print(f"\n🏁 游戏结束！最终比分：你 {player_score} : {computer_score} 爸爸")
        break
    
    round_num += 1
    print("\n")

# 扩展玩法：
# 1. 加入积分制，先赢3局的人获得最终胜利
# 2. 加入5局3胜模式
# 3. 可以出特殊手势，比如"蜥蜴"、"史波克，增加更多玩法
