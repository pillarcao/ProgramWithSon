"""
🔐 随机密码生成器
难度：★★★ 进阶级
知识点：字符串、随机数、列表、用户交互
功能：生成不同强度的安全密码
"""
import random
import string

print("🔐 随机密码生成器")
print("生成安全的随机密码\n")

# 定义字符集
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
symbols = "!@#$%^&*()-_=+"

try:
    length = int(input("请输入密码长度（建议8-16位）："))
    include_symbols = input("是否包含特殊符号？(y/n)：").lower().strip() == 'y'
    
    # 构建字符池
    chars = lowercase + uppercase + digits
    if include_symbols:
        chars += symbols
    
    # 生成密码
    password = ''.join(random.choice(chars) for _ in range(length))
    
    # 计算强度
    strength = "弱"
    if length >= 8 and (include_symbols):
        strength = "强"
    elif length >= 8:
        strength = "中"
    
    print(f"\n✅ 生成的密码： {password}")
    print(f"📊 密码强度： {strength}")
    print("\n记得保存好密码哦！")
    
except ValueError:
    print("请输入有效的数字！")
