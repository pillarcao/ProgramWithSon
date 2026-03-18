"""
🎨 ASCII字符画生成器
难度：★ 入门级
知识点：字符串、循环、算法
功能：把文字转成ASCII字符画，或者简单图形
"""

# 预定义一些简单字符画
ascii_art = {
    "heart": """
  ♥♥♥♥♥♥
♥♥♥♥♥♥♥♥♥♥
  ♥♥♥♥♥♥♥♥
    ♥♥♥♥♥
      ♥♥
       ♥
""",
    "smile": """
    ^^^^^^
   ^      ^
  ^  o  o  ^
  ^      ^
   ^      ^
    ^^^^^^
     """,
    "cat": """
 /\\_/\\  
( o.o ) 
 > ^ <  
"""
}

print("🎨 ASCII字符画生成器")
print("试试这些：heart(心), smile(笑脸), cat(猫咪)\n")

choice = input("请输入图案名称：").lower().strip()

if choice in ascii_art:
    print("\n" + ascii_art[choice])
else:
    # 让用户输入文字，用字符输出大字母
    text = input("没有这个图案，那我给你输出大文字：")
    print("\n你的文字转换成大写：\n")
    for char in text.upper():
        if char.isalpha():
            print(char, end=" ")
        else:
            print(char, end=" ")
    print("\n")
    print("提示：你可以扩展这个程序，添加更多ASCII艺术图案哦！")
