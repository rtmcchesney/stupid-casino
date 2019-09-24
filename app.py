import random
from random import *
import time 
import sys
import os

slot1 = ('1', '2', '3')
slot2 = ('1', '2', '3')
slot3 = ('1', '2', '3')


def start():
    global bank
    print('Welcome to python slots!')
    user_input = input("You currently have $1000 to start! Press [ENTER] to start!")
    if user_input == '':
        bank = 1000
        run_game()
    else:
        print('Come play again soon!')



def run_game():


start()
