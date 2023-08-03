"""
Modules
"""
import random
from random import randint
import time
import gspread
from google.oauth2.service_account import Credentials

choice = ["R", "P", "S"]
computer = choice[randint(0,2)]

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('rock_paper_scissors')

userscore = SHEET.worksheet('userinfo')

# data = sales.get_all_values()

# print(data)




def intro():
    """
    This is the opening to the game
    User can pick to play or read the instructions.
    """
    clear()
    print('')
    print("Welcome to Rock Paper Scissors \n")
    username = input("Please enter username: ")
    sales_worksheet = SHEET.worksheet("userinfo")
    clear() 
    print("\nWould you like to read the Game Instructions " + username)
    answer = input("\nEnter Y to read the instructions or N to continue to game.\n").upper()
    print('')
    while True:
        if answer == "Y":
            instructions()
        elif answer == "N":
            play_game()

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
    print(" 2) User enter either R-(Rock) or P-(Paper) or S-(Scissors).")
    print(" 2) Rock wins against scissors.")
    print(" 3) Scissors win against paper.")
    print(" 4) Paper wins against rock.")
    print(" 5) Enter Q to stop the game.")
    print(' ')
    time.sleep(8)
    print("Would you like to Play the game or Quit and exit?")
    answer = input("Enter Y to play or N to Quit\n").upper()
    print('')
    while True:
        if answer == "Y":
            play_game()
        elif answer == "N":
            break

        else:
            print('')
            print("Please enter a valid input of either Y to play or N to Quit\n")
            answer = input("").upper()
    clear()

# def print_board():
def play_game():
    choice = ["R", "P", "S"]
    computer = choice[randint(0,2)]
    user = input("Please choose _ R for Rock, P for Paper, and S for Scissors or (Q to quit the game)\n").upper()
    if user == computer:
        print("Draw!")
    elif user == "R":
        if computer == "P":
            print("You lose!")
        else:
            print("You win!")
    elif user == "P":
        if computer == "S":
            print("You lose!")
        else:
            print("You win!")
    elif user == "S":
        if computer == "R":
            print("You lose...")
        else:
            print("You win!")

    elif user == "Q":
            clear()
            print("Thank you for playing the game.")
            time.sleep(5)
            # intro()
            exit()
    elif user == "C":
            clear()            
    else:
        print("That's not a valid play. Check your spelling! Enter Q to quit the game.")


# def get_high_score():
#     """
#     Gets the high score from user who have played the game
#     """

def clear():
    """
        Clears the screen
    """
    print("\033c")
    

def you_win():
    print(' ')
    print('                     __ __ _____ _____    _ _ _ _____ _____ ')
    print('                    |  |  |     |  |  |  | | | |     |   | |')
    print('                    |_   _|  |  |  |  |  | | | |  |  | | | |')
    print('                      |_| |_____|_____|  |_____|_____|_|___|')
    print(' ')



intro()

