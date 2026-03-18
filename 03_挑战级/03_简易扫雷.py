"""
💣 经典扫雷游戏
难度：★★★★ 挑战级
知识点：二维列表、递归、事件处理、pygame图形编程
玩法：和Windows自带的扫雷一样，点开不是雷的格子，插旗子标记雷
需要安装：pip install pygame
"""
import random
import pygame
import sys

# 游戏配置
ROW = 9
COL = 9
MINES = 10
CELL_SIZE = 40
MARGIN = 2

# 颜色
BLACK = (0, 0, 0)
GRAY = (189, 189, 189)
DARK_GRAY = (160, 160, 160)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 128, 0)
GRAY_BLUE = (100, 100, 150)

# 数字颜色
NUMBER_COLORS = [
    BLACK,
    BLUE,
    GREEN,
    RED,
    (128, 0, 128),
    (128, 0, 0),
    (0, 128, 128),
    BLACK,
    GRAY_BLUE
]

class Minesweeper:
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = [[0 for _ in range(cols)] for _ in range(rows)]
        self.revealed = [[False for _ in range(cols)] for _ in range(rows)]
        self.flagged = [[False for _ in range(cols)] for _ in range(rows)]
        self.game_over = False
        self.won = False
        self.first_click = True
        
    def place_mines(self, exclude_row, exclude_col):
        # 在首次点击位置不放雷
        count = 0
        while count < self.mines:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)
            # 不在点击位置，也不重复放雷
            if (abs(r - exclude_row) > 1 or abs(c - exclude_col) > 1) and self.board[r][c] != -1:
                self.board[r][c] = -1
                count += 1
        
        # 计算每个格子周围雷数
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] != -1:
                    self.board[r][c] = self.count_adjacent_mines(r, c)
    
    def count_adjacent_mines(self, row, col):
        count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                r = row + dr
                c = col + dc
                if 0 <= r < self.rows and 0 <= c < self.cols and self.board[r][c] == -1:
                    count += 1
        return count
    
    def reveal(self, row, col):
        if self.game_over or self.revealed[row][col] or self.flagged[row][col]:
            return
        
        if self.first_click:
            self.place_mines(row, col)
            self.first_click = False
            
        self.revealed[row][col] = True
        
        if self.board[row][col] == -1:
            # 踩雷了
            self.game_over = True
            self.won = False
            return
        
        # 如果周围没雷，递归展开
        if self.board[row][col] == 0:
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    r = row + dr
                    c = col + dc
                    if 0 <= r < self.rows and 0 <= c < self.cols:
                        self.reveal(r, c)
        
        self.check_win()
    
    def toggle_flag(self, row, col):
        if self.game_over or self.revealed[row][col]:
            return
        self.flagged[row][col] = not self.flagged[row][col]
    
    def check_win(self):
        # 所有非雷格子都被点开就算赢
        revealed_count = sum(sum(row) for row in self.revealed)
        total_cells = self.rows * self.cols
        if revealed_count == total_cells - self.mines:
            self.won = True
            self.game_over = True
    
    def draw(self, screen):
        for r in range(self.rows):
            for c in range(self.cols):
                x = c * CELL_SIZE + MARGIN
                y = r * CELL_SIZE + MARGIN
                w = CELL_SIZE - MARGIN * 2
                h = CELL_SIZE - MARGIN * 2
                
                if self.revealed[r][c]:
                    pygame.draw.rect(screen, WHITE, (x, y, w, h))
                    if self.board[r][c] == -1:
                        # 地雷
                        pygame.draw.circle(screen, BLACK, (x + w//2, y + h//2), w//3)
                    elif self.board[r][c] > 0:
                        # 数字
                        font = pygame.font.Font(None, 24)
                        text = font.render(str(self.board[r][c]), True, NUMBER_COLORS[self.board[r][c]])
                        text_rect = text.get_rect(center=(x + w//2, y + h//2))
                        screen.blit(text, text_rect)
                else:
                    # 未点开
                    pygame.draw.rect(screen, GRAY, (x, y, w, h))
                    if self.flagged[r][c]:
                        # 旗子
                        font = pygame.font.Font(None, 24)
                        text = font.render("🚩", True, RED)
                        text_rect = text.get_rect(center=(x + w//2, y + h//2))
                        screen.blit(text, text_rect)
        
        if self.game_over:
            # 显示游戏结束文字
            font = pygame.font.Font(None, 36)
            if self.won:
                text = font.render("恭喜你赢了！🎉", True, GREEN)
            else:
                text = font.render("游戏结束！💥", True, RED)
            text_rect = text.get_rect(center=(self.cols * CELL_SIZE // 2, self.rows * CELL_SIZE + 20))
            screen.blit(text, text_rect)

def main():
    pygame.init()
    
    width = COL * CELL_SIZE
    height = ROW * CELL_SIZE + 40
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("简易扫雷")
    
    game = Minesweeper(ROW, COL, MINES)
    
    # 游戏主循环
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN and not game.game_over:
                x, y = pygame.mouse.get_pos()
                col = x // CELL_SIZE
                row = y // CELL_SIZE
                if 0 <= row < ROW and 0 <= col < COL:
                    if event.button == 1:
                        # 左键点开
                        game.reveal(row, col)
                    elif event.button == 3:
                        # 右键插旗子
                        game.toggle_flag(row, col)
            
            if event.type == pygame.KEYDOWN:
                if game.game_over and event.key == pygame.K_r:
                    # R重新开始
                    game = Minesweeper(ROW, COL, MINES)
        
        # 绘制
        screen.fill(DARK_GRAY)
        game.draw(screen)
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    print("💣 简易扫雷游戏")
    print("玩法：")
    print("- 左键点击：点开格子")
    print("- 右键点击：标记/取消旗子")
    print("- 游戏结束后按 R 重新开始")
    print("\n需要先安装pygame：pip install pygame")
    print("游戏启动中...\n")
    main()
