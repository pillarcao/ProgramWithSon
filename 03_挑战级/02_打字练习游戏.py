"""
⌨️ 打字练习游戏
难度：★★★ 挑战级
知识点：时间计算、字符串操作、计分系统
"""
import time
import random
import sys

# 练习用的词语
words = [
    '苹果', '香蕉', '橘子', '葡萄', '西瓜', '桃子', '梨子', '草莓', '芒果', '菠萝',
    '小猫', '小狗', '老虎', '兔子', '熊猫', '大象', '猴子', '长颈鹿', '鸭子', '小鸡',
    '红色', '蓝色', '绿色', '黄色', '紫色', '白色', '黑色', '粉色', '橙色', '灰色',
    '爸爸', '妈妈', '爷爷', '奶奶', '哥哥', '姐姐', '弟弟', '妹妹', '老师', '同学'
]

print("⌨️ 打字练习小游戏")
print("规则：屏幕上会出现词语，你需要准确输入，输入正确就算得分\n")
print("准备好了吗？按回车开始游戏！")
input()

# 游戏设置
total_rounds = 10  # 一共10轮
correct = 0  # 正确数量
start_time = time.time()

print(f"\n游戏开始！一共 {total_rounds} 题，加油！\n")

for i in range(total_rounds):
    # 随机选一个词
    target_word = random.choice(words)
    print(f"第 {i+1} 题：{target_word}")
    
    # 记录开始时间
    round_start = time.time()
    
    # 获取用户输入
    user_input = input("请输入：")
    
    # 判断是否正确
    if user_input == target_word:
        round_time = time.time() - round_start
        print(f"✅ 答对了！用时 {round_time:.1f} 秒\n")
        correct += 1
    else:
        print(f"❌ 答错了，正确答案是：{target_word}\n")

# 计算成绩
total_time = time.time() - start_time
accuracy = correct / total_rounds * 100
wpm = (correct * 60) / total_time  # 每分钟输入的字数

print("=" * 40)
print("🏁 游戏结束！你的成绩：")
print(f"✅ 正确题数：{correct}/{total_rounds}")
print(f"🎯 正确率：{accuracy:.1f}%")
print(f"⏱️  总用时：{total_time:.1f} 秒")
print(f"⚡ 速度：{wpm:.1f} 字/分钟")

# 评价
if accuracy == 100:
    print("🏆 太棒了！全对！你是打字小能手！")
elif accuracy >= 80:
    print("🎉 很棒哦！继续加油就可以全对啦！")
elif accuracy >= 60:
    print("👍 不错哦，多练习就会越来越快的！")
else:
    print("💪 没关系，多练习几次就会越来越厉害的！")

# 扩展玩法：
# 1. 加入难度选择：简单（2字词）、中等（3字词）、困难（4字成语）
# 2. 加入连击系统，连续答对有额外加分
# 3. 记录历史最高成绩，下次可以挑战自己
# 4. 加入英文单词练习模式
