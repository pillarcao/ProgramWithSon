"""
🔢 九九乘法表生成器
难度：★★ 进阶级
知识点：嵌套循环、字符串格式化
"""
print("🔢 我的九九乘法表")
print("=" * 50)

# 生成九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        # 格式化输出，每个占7个字符宽度
        print(f"{j} × {i} = {i*j:<2d}", end="  ")
    print()  # 换行

print("\n" + "=" * 50)
print("✨ 厉害吧！这是程序自动生成的九九乘法表哦～\n")

# 进阶：随机出题练习
import random
print("🎯 要不要来做乘法题练习？")
while True:
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    answer = a * b
    
    user_input = input(f"\n{a} × {b} = ")
    if not user_input.isdigit():
        print("❌ 请输入数字哦！")
        continue
    
    user_answer = int(user_input)
    if user_answer == answer:
        print("🎉 答对啦！真棒！")
    else:
        print(f"❌ 答错啦，正确答案是 {answer}，下次加油哦！")
    
    again = input("还要继续做题吗？(y/n)：").lower()
    if again != 'y' and again != 'yes':
        print("\n👋 练习结束，下次再来玩哦！")
        break

# 扩展玩法：
# 1. 可以设置难度，比如10以内、20以内的乘法
# 2. 记录正确率，统计做对了多少题
# 3. 做错的题目自动加入错题本，之后再练习
