APP_SIZE = (400,700)
MAIN_ROWS = 7
MAIN_COLUMNS = 4

FONT = 'Helvetica'
OUTPUT_FONT_SIZE = 70
NORMAL_FONT_SIZE = 32

STYLING = {
    'gap': 0.5,
    'corner-radius': 0
}

NUM_POSITIONS = {
    '.' : {'col': 2, 'row': 6, 'span': 1},
    0 : {'col': 0, 'row': 6, 'span': 2},
    1 : {'col': 0, 'row': 5, 'span': 1},
    2 : {'col': 1, 'row': 5, 'span': 1},
    3 : {'col': 2, 'row': 5, 'span': 1},
    4 : {'col': 0, 'row': 4, 'span': 1},
    5 : {'col': 1, 'row': 4, 'span': 1},
    6 : {'col': 2, 'row': 4, 'span': 1},
    7 : {'col': 0, 'row': 3, 'span': 1},
    8 : {'col': 1, 'row': 3, 'span': 1},
    9 : {'col': 2, 'row': 3, 'span': 1},
}

MATH_POSITIONS = {
    '/' : {'col': 3, 'row': 2, 'character':'', 'operator':'/', 'image path': {'light':'img/light_div.png','dark':'img/dark_div.png'}},
    '*' : {'col': 3, 'row': 3, 'character':'x', 'operator':'*', 'image path': None},
    '-' : {'col': 3, 'row': 4, 'character':'-', 'operator':'-', 'image path': None},
    '+' : {'col': 3, 'row': 5, 'character':'+', 'operator':'+', 'image path': None},
    '=' : {'col': 3, 'row': 6, 'character':'=', 'operator':'=', 'image path': None},
}

OPERATORS = {
    'clear' : {'col': 0, 'row': 2, 'text':'AC','image path': None},
    'invert' : {'col': 1, 'row': 2, 'text':'', 'image path': {'light':'img/light_invert.png','dark':'img/dark_invert.png'}},
    'percent' : {'col': 2, 'row': 2, 'text':'%', 'image path': None}
}

COLORS = {
    'light-gray': {'fg': ('#505050','#D4D4D2'), 'hover': ('#686868','#efefed'), 'text': ('white', 'black')},
    'dark-gray': {'fg': ('#D4D4D2','#505050'), 'hover': ('#efefed','#686868'), 'text': ('black', 'white')},
    'orange': {'fg': '#FF9500', 'hover': '#ffb143', 'text': ('black', 'white')},
    'orange-highlight': {'fg': 'white', 'hover': 'white', 'text': ('black', '#FF9500')},
}

TITLE_BAR_HEX_COLORS = {
    'dark': 0x00000000,
    'light': 0x00EEEEEE
}

BLACK = '#000000'
WHITE = '#EEEEEE'
