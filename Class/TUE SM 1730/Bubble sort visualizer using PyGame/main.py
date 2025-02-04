import pygame
import random
import time

# Variables (Constants)
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255) # Red / Green / Blue
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BAR_COLOR = (0, 150, 200) # Light Blue
FPS = 60

# Functions
def build_bars(num, maxh) :
    bars = [random.randint(20, maxh) for _ in range(num)]

    return bars

def draw_bars(win, bars, bar_width, compare_bars=(), sorted_bars=(), swap_bars=()) :
    win.fill(BLACK)

    for i, bar_height in enumerate(bars) :
        x = i * bar_width
        y = HEIGHT - bar_height
        bar_color = BAR_COLOR

        if i in compare_bars :
            bar_color = RED
        elif i in sorted_bars :
            bar_color = GREEN
        elif i in swap_bars :
            bar_color = WHITE

        pygame.draw.rect(win, bar_color, (x, y, bar_width, bar_height))

    pygame.display.update()

def bubble_sort(win, bars, bar_width) :
    n = len(bars)
    sorted_bars = []

    for i in range(n) :
        swapped = False

        for j in range(0, n-i-1) :
            draw_bars(win, bars, bar_width, compare_bars=(j, j+1))
            time.sleep(0.05)

            if bars[j] > bars[j+1] :
                draw_bars(win, bars, bar_width, swap_bars=(j, j+1))
                time.sleep(0.05)

                bars[j], bars[j+1] = bars[j+1], bars[j]

                draw_bars(win, bars, bar_width, swap_bars=(j, j+1))
                time.sleep(0.05)

                swapped = True

        sorted_bars.append(n-i-1)
        draw_bars(win, bars, bar_width, sorted_bars=sorted_bars)
        time.sleep(0.05)

        if not swapped :
            break

    draw_bars(win, bars, bar_width, sorted_bars=range(n))

# Main Program
if __name__ == '__main__' :
    pygame.init()

    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bubble Sort Visualizer")
    clock = pygame.time.Clock()

    num_bars = 50
    max_bar_height = HEIGHT - 100
    bars = build_bars(num_bars, max_bar_height)
    bar_width = WIDTH // num_bars

    running = True
    started = False

    while running :
        clock.tick(FPS)

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False
            if event.type == pygame.KEYDOWN :
                if not started :
                    started = True
                    bubble_sort(win, bars, bar_width)

        if not started :
            draw_bars(win, bars, bar_width)

    pygame.quit()
