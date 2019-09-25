import random
from random import *
import time 
import sys
import os

slot1 = ''
slot2 = ''
slot3 = ''
current_bet = 0
bank = 0



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
    global slot1, slot2, slot3, bank, current_bet
    if bank <= 0:
        print("You're all out of cash, game over!")
    while bank > 0:
        if current_bet > 0 and bank >= current_bet:
            bet_repeat = input('[Enter] to place same bet, or enter no to place a new bet!')
            if bet_repeat == "":
                bet = current_bet
            else:
                current_bet = 0
                bet = 0
                run_game()
        else:
            try:
                bet = int(input("Place your bet!: "))
            except ValueError:
                return run_game()
        if bet >= 0 and bank >= bet:
            bank -= bet
            current_bet = bet
            try:
                slot1 = ['1', '2', '2', '3', '3', '3', '4', '4', '4', '4', '5', '5', '5', '5', '5']
                slot2 = ['1', '2', '2', '3', '3', '3', '4', '4', '4', '4', '5', '5', '5', '5', '5']
                slot3 = ['1', '2', '2', '3', '3', '3', '4', '4', '4', '4', '5', '5', '5', '5', '5']
                slot1 = choice(slot1)
                slot2 = choice(slot2)
                slot3 = choice(slot3)
                print('Spinning slots!')        
                for choice in slot1:
                    time.sleep(0.5)
                    print(choice)
                for choice in slot2:
                    time.sleep(0.5)
                    print(choice)
                for choice in slot3:
                    time.sleep(0.5)    
                    print(choice)
                print("-------------")    
start()
