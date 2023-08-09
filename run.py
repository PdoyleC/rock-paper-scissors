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
    print_slow("\t\t\tWelcome to Rock Paper Scissors \n") #comment out for testing
    print('')
    print_slow("\t\t\t     🪨  Vs 📄  Vs ✂️\n") #comment out for testing
    print('')
    time.sleep(2)
    clear()
    username = input("Please enter username: \n")
    # userscore.update_cell(3,1, username) comment out for testing
    userinfo.append_row([username], table_range='A2')
    time.sleep(2)
    clear()
    print("\nWelcome " + username)
    menu()

def menu():
    """ 
    User can picks there option on where to go.
    """
    print("\nPlease enter your selection by pressing the corresponding number.")
    print("\n1)....Press 1 and then Enter to play Rock Paper Sicssors.")
    print("\n2)....Press 2 and then Enter to read the instruction's.")
    #print("\n3)....Press 3 and then Enter to see your score.")  comment out so code can be written
    #print("\n4)....Press 4 and then Enter to see high score's.") comment out so code can be written
    #print("\nWould you like to read the Game Instructions " + username)
    answer = input("\n\nPlease enter your choice - .\n").upper()
    # print(userscore.cell(3,1).value) this works
    print('')
    while True:
        if answer == "1":
            play_game()
        elif answer == "2":
            instructions()
        if answer == "3":
            get_score()
            
        else:
            print('')
            print("Please enter a valid input of either 1 or 2\n")
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
    time.sleep(3)
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
            print("Please enter a valid input of either P to play or M to go to the Menu\n")
            answer = input("").upper()
    clear()


def play_game():
    choice = ["R", "P", "S"]
    computer = choice[randint(0,2)]
    time.sleep(5)
    clear()
    user = input("\u001b[37m\nPlease choose _ R for Rock, P for Paper, and S for Scissors. \nEnter Q to quit the game. \nEnter M to go back to the Menu.\n").upper()
    if user == computer:
        print("It's a Draw! ")
        user_draw()
    elif user == "R":
        if computer == "P":
            print("You choose Rock, Computer picked Paper")
            print("\u001b[31mYou Lose!")
            user_lose()
        else:            
            print("You choose Rock, Computer picked Scissors")
            print("\u001b[32mYou Win!")
            user_win()
    elif user == "P":
        if computer == "S":
            print("You choose Paper, Computer picked Scissors")
            print("\u001b[31mYou Lose!")
            user_lose()
        else:
            print("You choose Paper, Computer picked Rock")
            print("\u001b[32mYou Win!")
            user_win()
    elif user == "S":
        if computer == "R":
            print("You choose Scissors, Computer picked Rock")
            print("\u001b[31mYou Lose")
            user_lose()
        else:            
            print("You choose Scissors, Computer picked Paper")
            print("\u001b[32mYou Win!")
            user_win()

    elif user == "Q":
            clear()
            userinfo.append_row([win], table_range='H2')
            print("Thank you for playing the game.")
            time.sleep(5)
            # intro()
            exit()
    elif user == "C":
            clear() 
    elif user == "M":
            userinfo.append_row([win], table_range='H2')
            menu()
    else:
        print("That input isn't valid. Please enter 'R' OR 'P' OR 'S'!")
        time.sleep(3)







# def get_high_score():
#     """
#     Gets the high score from user who have played the game
#     """

# def quit():
#     global win
#     global lose
#     global draw
#     userscore.append_row([win], table_range='B2')
#     userscore.append_row([lose], table_range='C2')
#     userscore.append_row([level], table_range='D2')
#     exit()

def get_score():
    print(userinfo.get_all_records())
    intro()



def user_win():
    global win
    win += 1    
    #userscore.update_cell(1,1, win)  # for total games played
    #userscore.append_row([win], table_range='B2')
    play_game()

def user_lose():
    global lose    
    lose += 1    
    #userscore.update_cell(1,2, lose)
    #userscore.append_row([lose], table_range='C2')
    play_game()

def user_draw():
    global level    
    level += 1    
    #userscore.update_cell(1,3, level)
    #userscore.append_row([level], table_range='D2')
    play_game()

def user_total():
    global total    
    total += 1    
    #userscore.update_cell(1,4, total)
    play_game()



# def reset():
#     userscore.update_cell(1,1, "0")
#     userscore.update_cell(1,2, "0")
#     userscore.update_cell(1,3, "0")
#     userscore.update_cell(1,4, "=SUM(A1:C1)")

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



get_score()
intro()
# play_game()
