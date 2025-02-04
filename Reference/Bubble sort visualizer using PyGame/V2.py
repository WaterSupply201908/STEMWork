'''
Okay, let's create a Bubble Sort visualizer using PyGame. I'll provide the code with explanations, and some comments to help you understand how it works.
'''

import pygame
import random
import time

# --- Constants ---
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BAR_COLOR = (0, 150, 200) # Light blue color
FPS = 60  # Frames per second

# --- Bar Creation helper function ---
def build_bars(num, maxh):
    """Creates bars with random heights up to maxh"""
    bars = [random.randint(20, maxh) for _ in range(num)]
    return bars

# --- DrawBars function ---
def draw_bars(win, bars, bar_width, compare_bars=(), sorted_bars=(), swap_bars=()):
    """Draws the bars with appropriate colors"""
    win.fill(BLACK)

    for i, bar_height in enumerate(bars):
        x = i * bar_width
        y = HEIGHT - bar_height
        bar_color = BAR_COLOR # default color
        
        if i in compare_bars:
            bar_color = RED # red for comparison
        elif i in sorted_bars:
            bar_color = GREEN # green for sorted
        elif i in swap_bars:
            bar_color = WHITE # white during swap

        pygame.draw.rect(win, bar_color, (x, y, bar_width, bar_height))
    
    pygame.display.update()

# --- Bubble Sort Algorithm ---
def bubble_sort(win, bars, bar_width):
    n = len(bars)
    sorted_bars = [] # Keep track of which bars are sorted
    for i in range(n):
        swapped = False # Check for optimization
        for j in range(0, n - i - 1):
            draw_bars(win, bars, bar_width, compare_bars=(j, j+1)) # Draw comparison
            time.sleep(0.05)

            if bars[j] > bars[j + 1]:
                draw_bars(win, bars, bar_width, swap_bars=(j, j+1)) # Draw before swap
                time.sleep(0.05)
                bars[j], bars[j + 1] = bars[j + 1], bars[j]
                draw_bars(win, bars, bar_width, swap_bars=(j, j+1)) # Draw after swap
                time.sleep(0.05)
                swapped = True
            
        sorted_bars.append(n-i-1);  # The Last element is sorted
        draw_bars(win, bars, bar_width, sorted_bars=sorted_bars) # update screen
        time.sleep(0.05)
        if not swapped: # Optimization, if no swap
            break
        
    draw_bars(win, bars, bar_width, sorted_bars=range(n)) # Final draw with all bars green

# --- Main Game Loop ---
def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bubble Sort Visualizer")
    clock = pygame.time.Clock() # Clock to control FPS

    num_bars = 50
    max_bar_height = HEIGHT - 100
    bars = build_bars(num_bars, max_bar_height)
    bar_width = WIDTH // num_bars

    running = True
    started = False
    
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:  # Start the sorting on a key press
                if not started:
                    started = True
                    bubble_sort(win, bars, bar_width)
        
        if not started:
            draw_bars(win, bars, bar_width) # For Initial screen

    pygame.quit()

if __name__ == '__main__':
    main()

'''
How this Code Works:

1. Setup:

  - Imports: Imports libraries for graphics (pygame), random numbers, and timing.
  - Constants: Defines essential colors, window dimensions, FPS, and a default bar color.
  - build_bars(): This function creates a list of random numbers that represent the height of our bars.
  
2. Drawing:

  - draw_bars(): Clears the screen, draws the bars as rectangles. It takes the list of bars as input and their index to highlight comparison vs swapping vs sorted.

3. Bubble Sort:

  - bubble_sort(): The core of the visualizer.
    . Iterates through the list, comparing adjacent elements.
    . It draws bars before the comparison and swap operation to highlight the comparison and swapping.
    . It sleeps for a bit using the time.sleep function to slow down the process so you can actually see it happen.
    . It updates on every outer loop

4. Main Game Loop

  - main(): The core of the visualizer.
    . Initializes Pygame window, clock.
    . Sets up the bar list bars, num_bars, and bar_width.
    . Starts the main game loop.
    . Controls FPS.
    . When any key is pressed, the sorting routine begins.
    . The window gets updated to keep showing the list until the user quits

How to Run this Code:

1. Make sure you have Pygame installed. If not you can install it using pip install pygame
2. Save the code: Save the code as a Python file (e.g., bubble_sort_vis.py).
3. Run from command line: Open a terminal or command prompt, navigate to the directory where you saved the file, and run the code using: python bubble_sort_vis.py.
4. A window will open, showing the unsorted bars. Press any key to start

Key improvements:

  - Clear Separation Responsibilities : Different section are responsible for different tasks.
  - Clear Colors: The colors now makes sense.
  - Optimization: Added the bubble sort optimization where the algo will stop when the list is sorted.
  - Commented: The code has appropriate comments.
  - Proper Variable Names: Better names for variables.
  - FPS: The visualization is controlled via FPS to slow down the visualization
  - time.sleep: To allow visual slow down of the process.
  - Key press: The algorithm starts on any key press instead of immediately.

Feel free to modify the constants, the size of the bars, and the colors to experiment and make it your own. Let me know if you have any questions!
'''
