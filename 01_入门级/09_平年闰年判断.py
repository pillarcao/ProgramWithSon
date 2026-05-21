"""
09_平年闰年判断.py
==================
难度：★ 入门级
作者：和儿子一起写的小程序 🏗️

【这个程序能干嘛？】
    输入一个年份，告诉你是「平年」还是「闰年」，
    顺便告诉你这一年的 2 月有多少天、全年多少天。

【为啥要分平年和闰年？】
    地球绕太阳转一圈，其实不是正好 365 天，
    而是 365 天 5 小时 48 分 46 秒 ≈ 365.2422 天。
    多出来的那一点点，攒 4 年差不多就够 1 整天啦，
    所以每 4 年就要补一天，那一年就叫「闰年」，2 月有 29 天。

【判断口诀（背下来超简单）】
    四年一闰，百年不闰，四百年再闰。
    也就是说：
        1) 能被 4 整除         → 闰年
        2) 但能被 100 整除     → 又变回平年
        3) 但能被 400 整除     → 还是闰年
    用代码表示就是下面那一行 if 啦 👇
"""

import sys

# Windows 控制台默认是 GBK，会把 emoji 打成乱码或者直接报错。
# 这里把标准输出强制改成 UTF-8，小朋友直接双击运行也不会崩 ✨
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


def is_leap_year(year: int) -> bool:
    """判断一个年份是不是闰年，返回 True / False。

    规则一行就能写完：
        - 能被 4 整除 且 不能被 100 整除   → 闰年
        - 或者 能被 400 整除               → 闰年
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def explain(year: int) -> str:
    """把判断过程一步一步写出来，方便小朋友看懂为什么。"""
    steps = [f"🔍 来看看 {year} 年："]

    if year % 400 == 0:
        steps.append(f"  • {year} ÷ 400 = {year // 400}，能整除 ✅")
        steps.append("  • 根据「四百年再闰」→ 是闰年 🎉")
    elif year % 100 == 0:
        steps.append(f"  • {year} ÷ 100 = {year // 100}，能整除")
        steps.append(f"  • 但 {year} ÷ 400 除不尽")
        steps.append("  • 根据「百年不闰」→ 是平年")
    elif year % 4 == 0:
        steps.append(f"  • {year} ÷ 4 = {year // 4}，能整除 ✅")
        steps.append(f"  • {year} ÷ 100 除不尽")
        steps.append("  • 根据「四年一闰」→ 是闰年 🎉")
    else:
        steps.append(f"  • {year} ÷ 4 = {year / 4}，除不尽 ❌")
        steps.append("  • 连第一关都没过 → 是平年")

    return "\n".join(steps)


def describe(year: int) -> None:
    """打印完整的判断结果（包括 2 月天数、全年天数）。"""
    leap = is_leap_year(year)
    print(explain(year))

    if leap:
        print(f"\n📅 结论：{year} 年是【闰年】🎉")
        print(f"   ➜ 2 月有 29 天")
        print(f"   ➜ 全年一共 366 天")
    else:
        print(f"\n📅 结论：{year} 年是【平年】")
        print(f"   ➜ 2 月只有 28 天")
        print(f"   ➜ 全年一共 365 天")


def main():
    print("=" * 40)
    print("  🗓️  平年 / 闰年 小判官  🗓️")
    print("=" * 40)
    print("输入一个年份，我来告诉你是闰年还是平年～")
    print("（输入 q 退出，输入两个年份用空格隔开可以一次判断多个）\n")

    while True:
        user_input = input("👉 请输入年份：").strip()

        if user_input.lower() in ("q", "quit", "exit"):
            print("👋 拜拜，下次再玩！")
            break

        if not user_input:
            continue

        # 支持一次输入多个年份，例如：2024 2025 2100 2400
        parts = user_input.split()
        for part in parts:
            try:
                year = int(part)
            except ValueError:
                print(f"⚠️ 「{part}」不是一个有效的年份，跳过。\n")
                continue

            if year <= 0:
                print(f"⚠️ 年份要大于 0 哦，「{year}」不太对劲。\n")
                continue

            describe(year)
            print("-" * 40)


if __name__ == "__main__":
    main()
