from art import logo
import os
import time

def clear_screen():
    '''Clears the terminal screen using the 'cls' command on Windows.'''
    os.system('cls')


print(logo)
time.sleep(2)
clear_screen()