import pygame

# === SETUP ===
pygame.init()
SIZE = 15                  # 15x15 board
CELL = 40                  # size of one square
screen = pygame.display.set_mode((SIZE*CELL, SIZE*CELL))
pygame.display.set_caption("Simple Gomoku - Click to play!")

board = [[0 for _ in range(SIZE)] for _ in range(SIZE)]   # 0=empty, 1=black, 2=white
player = 1                # 1 = Black, 2 = White (Black starts)

# Colors
WOOD = (220, 180, 100)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# === DRAW THE BOARD ONCE ===
def draw_board():
    screen.fill(WOOD)
    for x in range(SIZE):
        pygame.draw.line(screen, BLACK, (x*CELL+20, 20), (x*CELL+20, SIZE*CELL-20), 2)
        pygame.draw.line(screen, BLACK, (20, x*CELL+20), (SIZE*CELL-20, x*CELL+20), 2)

draw_board()
pygame.display.update()

# === MAIN GAME LOOP ===
running = True
winner = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Left mouse click = place a stone
        if event.type == pygame.MOUSEBUTTONDOWN and winner == 0:
            x, y = event.pos
            col = (x // CELL)          # which column?
            row = (y // CELL)          # which row?

            # Check if the spot is empty and inside the board
            if 0 <= col < SIZE and 0 <= row < SIZE and board[row][col] == 0:
                board[row][col] = player

                # Draw the stone
                center_x = col * CELL + 20
                center_y = row * CELL + 20
                if player == 1:
                    pygame.draw.circle(screen, BLACK, (center_x, center_y), 16)
                else:
                    pygame.draw.circle(screen, WHITE, (center_x, center_y), 16)
                    pygame.draw.circle(screen, BLACK, (center_x, center_y), 16, 2)

                # Simple win check: look in 4 directions for 5 same stones
                for dr, dc in [(0,1),(1,0),(1,1),(1,-1)]:  # → ↓ ↘ ↗
                    count = 1
                    # one direction
                    for i in range(1, 5):
                        r = row + i*dr
                        c = col + i*dc
                        if not (0<=r<SIZE and 0<=c<SIZE and board[r][c]==player):
                            break
                        count += 1
                    # opposite direction
                    for i in range(1, 5):
                        r = row - i*dr
                        c = col - i*dc
                        if not (0<=r<SIZE and 0<=c<SIZE and board[r][c]==player):
                            break
                        count += 1
                    if count >= 5:
                        winner = player

                # Switch player
                player = 3 - player   # 1 → 2, 2 → 1

                # Show winner
                if winner:
                    font = pygame.font.SysFont(None, 80)
                    text = font.render("BLACK WINS!" if winner==1 else "WHITE WINS!", True, RED)
                    screen.blit(text, (SIZE*CELL//2 - text.get_width()//2, SIZE*CELL//2 - 40))

                pygame.display.flip()

pygame.quit()
