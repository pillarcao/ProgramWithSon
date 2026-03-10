"""
📱 二维码生成器
难度：★★ 进阶级
知识点：第三方库使用、文件操作
需要先安装qrcode库：pip install qrcode[pil]
"""
import qrcode
from PIL import Image

print("📱 我的二维码生成器")
print("可以把文字、网址、联系方式等变成二维码哦～\n")

while True:
    # 获取输入内容
    content = input("请输入要生成二维码的内容（比如网址、文字）：")
    if not content:
        print("❌ 内容不能为空哦！")
        continue
    
    # 生成二维码
    print("🔄 正在生成二维码...")
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(content)
    qr.make(fit=True)
    
    # 创建图片
    img = qr.make_image(fill_color='black', back_color='white')
    
    # 保存图片
    filename = f"二维码_{content[:10]}.png"
    img.save(filename)
    print(f"✅ 二维码生成成功！已保存为：{filename}")
    
    # 打开二维码图片
    try:
        img.show()
    except:
        print("ℹ️ 可以在当前文件夹找到生成的二维码图片哦")
    
    # 要不要继续生成
    again = input("\n还要生成其他二维码吗？(y/n)：").lower()
    if again != 'y' and again != 'yes':
        print("\n👋 二维码生成器关闭啦，下次再见！")
        break
    print("\n")

# 扩展玩法：
# 1. 可以自定义二维码颜色，比如蓝色前景、黄色背景
# 2. 可以在二维码中间加logo图片
# 3. 可以生成艺术二维码，有不同的样式
# 4. 可以批量生成多个二维码
