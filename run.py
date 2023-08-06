"""
Modules
"""
import random
from random import randint
import sys
import time
import gspread
from google.oauth2.service_account import Credentials

choice = ["R", "P", "S"]
computer = choice[randint(0,2)]
level = 0
win = 0
lose = 0
total = 0


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('rock_paper_scissors')

userinfo = SHEET.worksheet('userinfo')
userscore = SHEET.worksheet('userscore')

# data = sales.get_all_values()

# print(data)




def intro():
    """
    This is the opening to the game
    User can pick to play or read the instructions.
    """
    clear()
    print('')
    print_slow("Welcome to Rock Paper Scissors \n") #comment out for testing
    print('')
    print_slow("     🪨  Vs 📄  Vs ✂️\n") #comment out for testing
    print('')
    time.sleep(5)
    clear()
    username = input("Please enter username: ")
    # userscore.update_cell(3,1, username) comment out for testing
    userinfo.append_row([username], table_range='A2')
    time.sleep(2)
    clear()
    print("\nWelcome " + username)
    menu()

def menu():
    print("\nPlease enter your selection by pressing the corresponding number.")
    print("\n1)....Press 1 and then Enter to play Rock Paper Sicssors.")
    print("\n2)....Press 2 and then Enter to read the instruction's.")
    # print("\nWould you like to read the Game Instructions " + username)
    answer = input("\n\nPlease enter your choice - .\n").upper()
    # print(userscore.cell(3,1).value) this works
    print('')
    while True:
        if answer == "1":
            play_game()
        elif answer == "2":
            instructions()
            
        else:
            print('')
            print("Please enter a valid input of either Y or N\n")
            answer = input("").upper()


def instructions():
    """ 
    Game instructions will be printed if the user
    has never played the game.
    """
    clear()
    print(" 1) Game is played against the computer.")
    print(" 2) User enters either 'R'-(Rock) or 'P'-(Paper) or 'S'-(Scissors).")
    print(" 3) Rock wins against scissors.")
    print(" 4) Scissors win against paper.")
    print(" 5) Paper wins against rock.")
    print(" 6) Enter Q to stop the game.")
    print(" 7) Enter C to to clear the console.")
    print(' ')
    time.sleep(8)
    print("Would you like to Play the game or Quit and exit?")
    answer = input("Enter P to play or M to go to the Menu\n").upper()
    print('')
    while True:
        if answer == "P":
            play_game()
        elif answer == "M":
            menu()
            break

        else:
            print('')
            print("Please enter a valid input of either Y to play or N to Quit\n")
            answer = input("").upper()
    clear()


def play_game():
    choice = ["R", "P", "S"]
    computer = choice[randint(0,2)]
    time.sleep(2)
    clear()
    user = input("\u001b[37m\nPlease choose _ R for Rock, P for Paper, and S for Scissors or (Q to quit the game)\n").upper()
    if user == computer:
        print("It's a Draw! ")
        user_draw()
    elif user == "R":
        if computer == "P":
            print("\u001b[31mYou Lose!")
            user_lose()
        else:            
            print("\u001b[32mYou Win!")
            user_win()
    elif user == "P":
        if computer == "S":
            print("\u001b[31mYou Lose!")
            user_lose()
        else:
            print("\u001b[32mYou Win!")
            user_win()
    elif user == "S":
        if computer == "R":
            print("\u001b[31mYou Lose")
            user_lose()
        else:            
            print("\u001b[32mYou Win!")
            user_win()

    elif user == "Q":
            clear()
            userscore.append_row([username], table_range='B2')

            userscore.append_row([username], table_range='C2')

            userscore.append_row([username], table_range='D2')

            userscore.append_row([username], table_range='E2')

            print("Thank you for playing the game.")
            time.sleep(5)
            # intro()
            exit()
    elif user == "C":
            clear()            
    else:
        print("That input isn't valid. Please enter 'R' OR 'P' OR 'S'!")
        time.sleep(3)







# def get_high_score():
#     """
#     Gets the high score from user who have played the game
#     """

def user_win():
    global win
    win += 1    
    userscore.update_cell(1,1, win)  # for total games played
    #userscore.append_row([win], table_range='B2')
    play_game()

def user_lose():
    global lose    
    lose += 1    
    userscore.update_cell(1,2, lose)
    #userscore.append_row([lose], table_range='C2')
    play_game()

def user_draw():
    global level    
    level += 1    
    userscore.update_cell(1,3, level)
    #userscore.append_row([level], table_range='D2')
    play_game()

def user_total():
    global total    
    total += 1    
    userscore.update_cell(1,4, total)
    play_game()



def reset():
    userscore.update_cell(1,1, "0")
    userscore.update_cell(1,2, "0")
    userscore.update_cell(1,3, "0")
    userscore.update_cell(1,4, "=SUM(A1:C1)")

def clear():
    """
        Clears the screen
    """
    print("\033c")
    
def print_slow(ltr):
    """
    Creates a slow typing effect
    """
    for letter in ltr:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)


def you_win():
    print(' ')
    print('                     __ __ _____ _____    _ _ _ _____ _____ ')
    print('                    |  |  |     |  |  |  | | | |     |   | |')
    print('                    |_   _|  |  |  |  |  | | | |  |  | | | |')
    print('                      |_| |_____|_____|  |_____|_____|_|___|')
    print(' ')




reset()
intro()
# play_game()
