import time
import os
import random

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_tree():
    clear_console()
    print("    *")
    print("   * *")
    print("  *   *")
    print(" *     *")
    print("*       *")
    print(" *     *")
    print("  *   *")
    print("   * *")
    print("    *")
    time.sleep(1)