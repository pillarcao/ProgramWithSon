"""
🎨 小画家画图
难度：★ 入门级
知识点：循环、角度计算、坐标概念
需要安装turtle库（Python自带，一般不用额外安装）
"""
import turtle

# 创建画笔
pen = turtle.Turtle()
pen.speed(5)  # 画图速度：1最慢，10最快，0最快无动画
pen.color('blue')  # 画笔颜色

print("🎨 开始画小房子啦！")

# 画正方形（房子主体）
pen.fillcolor('lightblue')
pen.begin_fill()
for _ in range(4):
    pen.forward(150)  # 往前走150像素
    pen.right(90)     # 向右转90度
pen.end_fill()

# 画三角形（屋顶）
pen.fillcolor('brown')
pen.begin_fill()
pen.left(45)
pen.forward(106)  # 正方形对角线长度≈150*√2/2≈106
pen.right(90)
pen.forward(106)
pen.end_fill()

# 移动到门的位置
pen.penup()  # 抬起笔，移动的时候不画线
pen.goto(60, -150)  # 移动到坐标(x, y)
pen.pendown()  # 放下笔

# 画门
pen.fillcolor('yellow')
pen.begin_fill()
pen.setheading(0)  # 调整画笔方向朝右
for _ in range(2):
    pen.forward(30)
    pen.left(90)
    pen.forward(50)
    pen.left(90)
pen.end_fill()

# 画窗户
pen.penup()
pen.goto(20, -80)
pen.pendown()
pen.fillcolor('white')
pen.begin_fill()
for _ in range(4):
    pen.forward(40)
    pen.right(90)
pen.end_fill()

# 画窗户十字
pen.penup()
pen.goto(40, -80)
pen.pendown()
pen.goto(40, -120)
pen.penup()
pen.goto(20, -100)
pen.pendown()
pen.goto(60, -100)

# 隐藏画笔
pen.hideturtle()
print("✅ 小房子画完啦！")

# 保持窗口显示，点击关闭才会退出
turtle.done()

# 扩展玩法：
# 1. 试试画小花、太阳、小汽车
# 2. 改变画笔颜色和填充颜色
# 3. 画一个圆形的太阳，用circle()函数
# 4. 画一条弯弯曲曲的小路
