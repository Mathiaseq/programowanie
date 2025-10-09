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
    
    colors={
        'R': '\033[31m',
        'G': '\033[32m',
        'Y': '\033[33m',
        'B': '\033[34m',
        'M': '\033[35m',
        'C': '\033[36m',
        'W': '\033[37m'
    }
    