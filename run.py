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
    #print_slow("\t\t\tWelcome to Rock Paper Scissors \n") #comment out for testing
    print('')
    #print_slow("\t\t\t     🪨  Vs 📄  Vs ✂️\n") #comment out for testing
    print('')
    time.sleep(2)
    clear()
    enter_username()

def enter_username():  
    clear() 
    reset()
    global username 
    username = input("Please enter username: \n")
    # userscore.update_cell(3,1, username) comment out for testing
    # userinfo.append_row([username], table_range='A2')
    time.sleep(2)
    clear()
    print("\nWelcome " + username)
    menu()

def menu():
    """ 
    User can picks there option on where to go.
    """
    clear()
    print("\nPlease enter your selection by pressing the corresponding number.")
    print("\n1)....Press 1 and then Enter to play Rock Paper Sicssors.")
    print("\n2)....Press 2 and then Enter to read the instruction's.")
    #print("\n3)....Press 3 and then Enter to see your score.")  comment out so code can be written
    #print("\n4)....Press 4 and then Enter to see high score's.") comment out so code can be written
    print("\n4)....Press 4 and then Enter to Enter new Username.")
    print("\n5)....Press 5 and then Enter to Exit the Game.")
    #print("\nWould you like to read the Game Instructions " + username)
    answer = input("\n\nPlease enter your choice - .\n").upper()
    # print(userscore.cell(3,1).value) this works
    print('')
    while True:
        if answer == "1":
            play_game()
        elif answer == "2":
            instructions()
        if answer == "5":
            clear()
            print("Thank you for playing the game.")
            exit()
        elif answer =="4":
            enter_username()
        else:
            print('')
            print("Please enter a valid input of either 1, 2, 4 or 5\n")
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
    print(' ')
    print(' ')
    print("Would you like to Play the game, go back to the Menu or Exit?")
    answer = input("Enter P to play\nEnter M to go to the Menu\nEnter E to exit game.\n").upper()
    print('')
    while True:
        if answer == "P":
            play_game()
        elif answer == "M":
            menu()
        if answer =="E":
            menu()
            print("Thank you for playing the game.")
            exit()

        else:
            print('')
            print("Please enter a valid input of either P to play, M for Menu or E to exit\n")
            answer = input("").upper()
    clear()


def play_game():
    choice = ["R", "P", "S"]
    computer = choice[randint(0,2)]
    clear()
    global total
    global win
    user = input("\u001b[37m\nPlease choose _ R for Rock, P for Paper, and S for Scissors. \nEnter Q to quit the game. \nEnter M to go back to the Menu.\n\n").upper()
    if user == computer:
        print("It's a Draw! "+ username)
        total += 1
        input("\u001b[37mPress Enter to continue...")
        play_game()
    elif user == "R":
        if computer == "P":
            print("You choose Rock, Computer picked Paper")
            print("\u001b[31mYou Lose! " + username)
            input("\u001b[37mPress Enter to continue...")
            total += 1
            play_game()
        else:            
            print("You choose Rock, Computer picked Scissors")
            print("\u001b[32mYou Win! " + username)
            win += 1
            total += 1
            input("\u001b[37mPress Enter to continue...")
            play_game()
    elif user == "P":
        if computer == "S":
            print("You choose Paper, Computer picked Scissors")
            print("\u001b[31mYou Lose! " + username)
            input("\u001b[37mPress Enter to continue...")
            total += 1
            play_game()
        else:
            print("You choose Paper, Computer picked Rock")
            print("\u001b[32mYou Win! " + username)
            win += 1
            total += 1
            input("\u001b[37mPress Enter to continue...")
            play_game()
    elif user == "S":
        if computer == "R":
            print("You choose Scissors, Computer picked Rock")
            print("\u001b[31mYou Lose " + username)
            input("\u001b[37mPress Enter to continue...")
            total += 1
            play_game()
        else:            
            print("You choose Scissors, Computer picked Paper")
            print("\u001b[32mYou Win! " + username)
            win += 1
            total += 1
            input("\u001b[37mPress Enter to continue...")
            play_game()

    elif user == "Q":
            clear()
            userinfo.append_row([username], table_range='A2')
            userinfo.append_row([win], table_range='H2')
            userinfo.append_row([total], table_range='T2')
            print("Thank you for playing the game.")
            time.sleep(5)
            menu()
    elif user == "C":
            clear() 
    elif user == "M":
            userinfo.append_row([username], table_range='A2')
            userinfo.append_row([win], table_range='H2')
            userinfo.append_row([total], table_range='T2')
            reset()
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


# def user_win():
#     global win
#     win += 1    
#     #userscore.update_cell(1,1, win)  # for total games played
#     #userscore.append_row([win], table_range='B2')
#     play_game()

# def user_lose():
#     global lose    
#     lose += 1    
#     #userscore.update_cell(1,2, lose)
#     #userscore.append_row([lose], table_range='C2')
#     play_game()

# def user_draw():
#     global level    
#     level += 1    
#     #userscore.update_cell(1,3, level)
#     #userscore.append_row([level], table_range='D2')
#     play_game()

# def user_total():
#     global total    
#     total += 1    
#     #userscore.update_cell(1,4, total)
#     play_game()



def reset():
    global total
    total = 0
    global win
    win = 0
    
    
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



reset()
intro()
# play_game()
