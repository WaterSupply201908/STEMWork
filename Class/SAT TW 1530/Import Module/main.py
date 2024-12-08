# Import Module 1

import random
'''
print('\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518')
'''

dice_art = {
    1: ('┌─────────┐', '│         │', '│    ●    │', '│         │',
        '└─────────┘'),
    2: ('┌─────────┐', '│  ●      │', '│         │', '│      ●  │',
        '└─────────┘'),
    3: ('┌─────────┐', '│  ●      │', '│    ●    │', '│      ●  │',
        '└─────────┘'),
    4: ('┌─────────┐', '│  ●   ●  │', '│         │', '│  ●   ●  │',
        '└─────────┘'),
    5: ('┌─────────┐', '│  ●   ●  │', '│    ●    │', '│  ●   ●  │',
        '└─────────┘'),
    6:
    ('┌─────────┐', '│  ●   ●  │', '│  ●   ●  │', '│  ●   ●  │', '└─────────┘')
}

dice = []
total = 0
num_of_dice = int(input('How many dice? '))

for die in range(num_of_dice):
  dice.append(random.randint(1, 6))

for die in dice:
  total += die
  for line in dice_art.get(die) :
    print(line)

print(f'Total: {total}')
