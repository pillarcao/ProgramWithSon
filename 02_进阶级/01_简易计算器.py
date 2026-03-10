"""
🧮 简易计算器
难度：★★ 进阶级
知识点：算术运算、多条件判断、异常处理
"""
print("🧮 我的小计算器")
print("支持运算：加(+)、减(-)、乘(*)、除(/)\n")

while True:
    try:
        # 获取输入
        num1 = float(input("请输入第一个数字："))
        op = input("请输入运算符号(+-*/)：")
        num2 = float(input("请输入第二个数字："))
        
        # 计算结果
        if op == "+":
            result = num1 + num2
            print(f"\n✅ 计算结果：{num1} + {num2} = {result}")
        elif op == "-":
            result = num1 - num2
            print(f"\n✅ 计算结果：{num1} - {num2} = {result}")
        elif op == "*":
            result = num1 * num2
            print(f"\n✅ 计算结果：{num1} × {num2} = {result}")
        elif op == "/":
            if num2 == 0:
                print("\n❌ 错误：除数不能为0哦！")
            else:
                result = num1 / num2
                print(f"\n✅ 计算结果：{num1} ÷ {num2} = {result}")
        else:
            print("\n❌ 错误：输入的运算符号不对，请输入+-*/中的一个！")
    
    except ValueError:
        print("\n❌ 错误：请输入有效的数字哦！")
    
    # 问要不要继续计算
    again = input("\n还要继续计算吗？(y/n)：").lower()
    if again != 'y' and again != 'yes':
        print("\n👋 计算器关闭啦，下次再见！")
        break
    print("\n")

# 扩展玩法：
# 1. 加入乘方运算：比如2^3=8
# 2. 加入取余运算：比如10%3=1
# 3. 可以连续计算，比如上一次的结果作为下一次的第一个数字
# 4. 加入括号功能，支持复杂运算
