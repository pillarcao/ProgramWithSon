"""
🐍 简易贪吃蛇游戏
难度：★★★ 挑战级
知识点：pygame基础、事件处理、坐标移动、碰撞检测
需要先安装pygame：pip install pygame
"""
import pygame
import random
import sys

# 初始化pygame
pygame.init()

# 游戏设置
WIDTH = 400
HEIGHT = 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 创建窗口
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 贪吃蛇小游戏")

# 时钟控制游戏速度
clock = pygame.time.Clock()

def draw_snake(snake):
    """画蛇"""
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE - 1, GRID_SIZE - 1))

def draw_food(food):
    """画食物"""
    pygame.draw.rect(screen, RED, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE - 1, GRID_SIZE - 1))

def main():
    # 初始化蛇的位置（初始长度3）
    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
    direction = (1, 0)  # 初始方向向右
    
    # 生成食物
    food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    
    score = 0
    game_over = False
    
    while not game_over:
        # 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # 方向控制，不能反向走
                if event.key == pygame.K_UP and direction != (0, 1):
                    direction = (0, -1)
                elif event.key == pygame.K_DOWN and direction != (0, -1):
                    direction = (0, 1)
                elif event.key == pygame.K_LEFT and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                    direction = (1, 0)
        
        if not game_over:
            # 移动蛇头
            head_x, head_y = snake[0]
            new_head = (head_x + direction[0], head_y + direction[1])
            
            # 碰撞检测：撞墙
            if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or 
                new_head[1] < 0 or new_head[1] >= GRID_HEIGHT):
                game_over = True
            
            # 碰撞检测：撞到自己
            if new_head in snake:
                game_over = True
            
            # 吃到食物
            if new_head == food:
                score += 1
                # 生成新的食物，不能在蛇身上
                while food in snake:
                    food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            else:
                # 没吃到食物，去掉尾巴
                snake.pop()
            
            # 加入新蛇头
            snake.insert(0, new_head)
            
            # 画图
            screen.fill(BLACK)
            draw_snake(snake)
            draw_food(food)
            
            # 显示分数
            font = pygame.font.Font(None, 36)
            score_text = font.render(f"分数: {score}", True, WHITE)
            screen.blit(score_text, (10, 10))
            
            if game_over:
                game_over_text = font.render("游戏结束！", True, WHITE)
                screen.blit(game_over_text, (WIDTH // 2 - 70, HEIGHT // 2 - 20))
                final_score = font.render(f"最终分数: {score}", True, WHITE)
                screen.blit(final_score, (WIDTH // 2 - 70, HEIGHT // 2 + 20))
            
            # 更新显示
            pygame.display.flip()
            
            # 控制游戏速度
            clock.tick(10)
    
    # 游戏结束后等3秒再退出
    pygame.time.wait(3000)
    pygame.quit()

if __name__ == "__main__":
    print("🐍 贪吃蛇游戏开始啦！")
    print("🎮 用方向键控制蛇的移动，吃红色的食物长大，不要撞墙也不要撞到自己哦！")
    main()

# 扩展玩法：
# 1. 增加难度：随着分数增加，游戏速度变快
# 2. 加入关卡：不同关卡速度不同
# 3. 加入特殊食物：吃了可以减速或者加分
# 4. 加入穿墙功能：从左边出去从右边进来
