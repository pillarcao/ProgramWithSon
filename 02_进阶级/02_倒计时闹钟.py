"""
⏰ 倒计时闹钟
难度：★★ 进阶级
知识点：循环、时间模块、计数器
"""
import time
import sys

print("⏰ 我的倒计时闹钟")
print("可以用来给写作业、玩游戏、运动计时哦～\n")

while True:
    try:
        minutes = int(input("请输入倒计时多少分钟："))
        if minutes <= 0:
            print("❌ 请输入大于0的数字哦！")
            continue
        break
    except ValueError:
        print("❌ 请输入有效的数字哦！")

total_seconds = minutes * 60
print(f"\n⏳ 倒计时开始！一共 {minutes} 分钟，加油！\n")

try:
    for remaining in range(total_seconds, 0, -1):
        # 转换成分:秒格式
        mins = remaining // 60
        secs = remaining % 60
        # 动态显示倒计时（覆盖上一行）
        sys.stdout.write(f"\r🕒 剩余时间：{mins:02d}:{secs:02d}")
        sys.stdout.flush()
        time.sleep(1)
    
    # 时间到了
    print("\n\n🎉 时间到啦！")
    print("🔔 叮叮叮～时间到了哦！")
    
    # 可以扩展：播放提示音（Windows系统）
    # import winsound
    # winsound.Beep(1000, 1000)  # 频率1000Hz，持续1秒
    
except KeyboardInterrupt:
    print("\n\n⏹️ 倒计时已停止！")

# 扩展玩法：
# 1. 加入多种计时模式：写作业模式、休息模式、运动模式
# 2. 时间到了播放音乐或者提示音
# 3. 可以记录本次专注时间，统计每天学习时长
# 4. 加入番茄钟功能：工作25分钟，休息5分钟，循环
