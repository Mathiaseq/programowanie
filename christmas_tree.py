import time
import os
import random

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_tree(lights):
    tree=[
        "        *         ",
        "       ***        ",
        "      *****       ",
        "     *******      ",
        "    *********     ",
        "   ***********    ",
        "  *************   ",
        " ***************  ",
        "***************** ",
        "       |||        ",
        "       |||        "
    ]
    
    colors=[
        '\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m'
    ]
    

    time.sleep(1)
    

    color_index = 0
    for light in lights:
        color = colors[color_index % len(colors)] 
        color_index += 1
        for line in tree:
            print(color + line + '\033[0m')
        print()


lights = ['G', 'Y', 'G', 'R', 'Y']
print_tree(lights)