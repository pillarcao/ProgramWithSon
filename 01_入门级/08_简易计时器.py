"""
⏱️ 简易计时器
难度：★ 入门级
知识点：时间模块、循环、暂停
用途：写作业计时、煮鸡蛋计时、运动计时
"""

import time

print("⏱️ 简易计时器")
print("设置分钟，倒计时结束会提醒你\n")

try:
    minutes = float(input("请输入倒计时分钟数："))
    seconds = int(minutes * 60)
    
    print(f"\n倒计时开始：{minutes} 分钟")
    print("-" * 30)
    
    while seconds > 0:
        mins_left = seconds // 60
        secs_left = seconds % 60
        print(f"\r剩余时间：{mins_left:02d}:{secs_left:02d}", end="")
        time.sleep(1)
        seconds -= 1
    
    print("\n" + "-" * 30)
    print("\n⏰ 时间到了！")
    print("🔔 倒计时结束！")
    
    # 响几下
    for i in range(3):
        print('\a', end='')
        time.sleep(0.5)
        
except ValueError:
    print("请输入有效的数字哦！")
