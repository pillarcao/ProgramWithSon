"""
📖 成语接龙游戏
难度：★★★ 进阶级
知识点：文件读取、列表、字符串处理、逻辑判断
玩法：玩家说一个成语，电脑接最后一个字，看看你能赢电脑不！
"""
import random

# 常用成语列表（只保留四个字的成语）
idioms = [
    "一举两得", "一帆风顺", "三言两语", "五光十色", "六亲不认",
    "七上八下", "八面玲珑", "九牛一毛", "十全十美", "百发百中",
    "千山万水", "万无一失", "天长地久", "日新月异", "山高水长",
    "风和日丽", "云淡风轻", "花好月圆", "鸟语花香，"东张西望",
    "南来北往", "左顾右盼", "前仆后继", "惊天动地", "翻天覆地",
    "自言自语", "自由自在", "无忧无虑", "一心一意", "三心二意",
    "四面八方", "五湖四海，"六神无主", "八仙过海，"十拿九稳",
    "百战百胜", "千辛万苦，"万紫千红，"白纸黑字，"白里红，"
    "红颜知己，"知己知彼，"比翼双飞，"飞蛾扑火，"火上浇油，
    "油腔滑调，"调虎离山，"山崩地裂，"裂石穿云，"云开见日，
    "日新月异，"异口同声，"声东击西，"西窗剪烛，"烛照数计，
    "计上心来，"来日方长，"长治久安，"安贫乐道，"道听途说"
]

print("📖 成语接龙游戏")
print("规则：你先说一个四字成语，电脑用你成语的最后一个字开头接一个成语\n")

# 获取成语最后一个字
def get_last_char(idiom):
    return idiom[-1]

# 找以某个字开头的成语
def find_idiom_start_with(char):
    candidates = [i for i in idioms if i[0] == char]
    if candidates:
        return random.choice(candidates)
    return None

# 游戏主循环
player_turn = True
current_char = None
used = set()

# 玩家先手
while True:
    if player_turn:
        if current_char is None:
            # 第一步，玩家随便出
            player_idiom = input("请你出第一个四字成语：").strip()
        else:
            player_idiom = input(f"该你了，要接'{current_char}'开头：").strip()
        
        # 验证
        if len(player_idiom) != 4:
            print("请输入四字成语哦！")
            continue
        if player_idiom in used:
            print("这个成语已经用过了，换一个！")
            continue
        # 检查开头是否正确
        if current_char is not None and player_idiom[0] != current_char:
            print(f"不对哦，必须以'{current_char}'开头！")
            continue
        
        # 正确
        used.add(player_idiom)
        current_char = get_last_char(player_idiom)
        player_turn = False
    else:
        # 电脑回合
        print(f"电脑找...（接'{current_char}'开头）")
        computer_idiom = find_idiom_start_with(current_char)
        if computer_idiom is None:
            print(f"电脑找不到了！你赢了！🎉")
            break
        print(f"电脑接：{computer_idiom}")
        used.add(computer_idiom)
        current_char = get_last_char(computer_idiom)
        player_turn = True

print(f"\n游戏结束！一共用了{len(used)}个成语！")
