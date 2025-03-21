```python
import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Reaction Time Game")
clock = pygame.time.Clock()

running = True
rect_visible = False
rect_x, rect_y = 0, 0
reaction_time = 0
start_time = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and rect_visible:
            reaction_time = pygame.time.get_ticks() - start_time
            print(f"Reaction Time: {reaction_time} ms")
            rect_visible = False

    screen.fill((0, 0, 0))

    if not rect_visible and random.random() < 0.05:
        rect_visible = True
        rect_x = random.randint(0, WIDTH - 50)
        rect_y = random.randint(0, HEIGHT - 50)
        start_time = pygame.time.get_ticks()

    if rect_visible:
        pygame.draw.rect(screen, (255, 0, 0), (rect_x, rect_y, 50, 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

### Overview

The provided Python file uses the Pygame library to create a simple reaction time game. The game displays a window where a red square appears randomly, and players must click on it to measure their reaction time.

### Code Structure

1. **Library Imports**:
   - `pygame`: Used for creating the game window and handling events.
   - `random`: Used for generating random numbers.

2. **Pygame Initialization**:
   - Initializes Pygame and sets up the window dimensions and title.
   - Creates a clock object to control the frame rate.

3. **Main Game Loop**:
   - Continuously runs until the user closes the window.
   - Handles events such as closing the window or mouse clicks.
   - Updates game states like the appearance of the square and recording reaction times.

4. **Game Logic**:
   - The square appears randomly with a 5% chance each frame.
   - Records the reaction time when the square appears and prints it when clicked.

5. **Rendering**:
   - Clears the screen.
   - Draws the square if it is visible.
   - Updates the display.

6. **Exiting the Game**:
   - Exits Pygame.

### Suggestions for Improvement

1. **Code Organization**: Break down different functionalities into separate functions for better readability.
2. **User Experience**: Add feedback or prompts to let players know when they can click the square.

### Example Optimized Code

```python
import pygame
import random

def draw_rect(screen, rect_x, rect_y):
    pygame.draw.rect(screen, (255, 0, 0), (rect_x, rect_y, 50, 50))

def main():
    pygame.init()

    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Reaction Time Game")
    clock = pygame.time.Clock()

    running = True
    rect_visible = False
    rect_x, rect_y = 0, 0
    reaction_time = 0
    start_time = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and rect_visible:
                reaction_time = pygame.time.get_ticks() - start_time
                print(f"Reaction Time: {reaction_time} ms")
                rect_visible = False

        screen.fill((0, 0, 0))

        if not rect_visible and random.random() < 0.05:
            rect_visible = True
            rect_x = random.randint(0, WIDTH - 50)
            rect_y = random.randint(0, HEIGHT - 50)
            start_time = pygame.time.get_ticks()

        if rect_visible:
            draw_rect(screen, rect_x, rect_y)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
```

### Summary

The code provides a basic framework for a reaction time game. With some optimizations and expansions, it can be further enhanced to improve user experience and playability.
