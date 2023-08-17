"""
Modules
"""
from random import randint
import sys
import os
import time
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2.service_account import Credentials


choice = ["R", "P", "S"]
computer = choice[randint(0, 2)]
win = 0
total = 0
incorrect = 4


SCOPE = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('rock_paper_scissors')
credentials = ServiceAccountCredentials.from_json_keyfile_name('creds.json', SCOPE)
client = gspread.authorize(credentials)
sheet = client.open('rock_paper_scissors').sheet1
SPREADSHEET_ID = "1L2qcyBdDqffBuXtvUyqKk49c5hauk4lLj9g8aNBwbmA"

userinfo = SHEET.worksheet('userinfo')
userdate = SHEET.worksheet('userdate')


def intro():
    """
    This is the opening to the game
    User can pick to play or read the instructions.
    """
    clear()
    print('')
    print('')
    print_slow("\n\n\n\t\t\tWelcome to Rock Paper Scissors \n")
    print('')
    print_slow("\t\t\t\t🪨  Vs 📄  Vs ✂️\n")
    print('')
    time.sleep(2)
    clear()
    enter_username()


def enter_username():
    """
    This is for the username,
    at the start of the game and when searching in the game area.
    """
    global username
    global incorrect
    clear()
    print('')
    print(" Your username can't be just spaces.")
    print(" Also your username must be 12 or less characters.")
    username = input("\n Please enter username: \n >> ").upper()
    if len(username) > 12:
        clear()
        global incorrect
        incorrect -= 1
        if incorrect == 0:
            clear()
            print(" \n I'm afraid you've entered an incorrect Username.")
            print(" The Program will end now.\n")
            exit()
        else:
            print(f" You only have {incorrect} more attempts \
at a valid Username,")
            print(" Before the program ends.")
            print(" Only a max of 12 characters allowed!")
            input("\n Press Enter and then input a valid username.\n")
            enter_username()
    elif username.strip() != "":
        menu()
    elif incorrect == 1:
        clear()
        print(" \n I'm afraid you've entered an incorrect Username.")
        print(" The Program will end now.\n")
        exit()
    else:
        clear()
        incorrect -= 1
        print(" Spaces or Enter only aren't a valid username.")
        print(f" You only have {incorrect} more attempts at a valid Username,")
        print(" Before the program ends.")
        input(" Press Enter and then input a valid username.\n")
        enter_username()
    menu()


def menu():
    """
    User can pick their option on where to go.
    """
    clear()
    print("\n Welcome " + username)
    menu_list()
    answer = input("\n\n Enter your number choice.\n >> ").upper()
    print('')
    while True:
        if answer == "1":
            play_game()
        elif answer == "2":
            instructions()
        if answer == "3":
            username_to_search = username
            print_score(username_to_search)
        elif answer == "4":
            enter_username()
        if answer == "5":
            clear()
            print(" Thank you for playing the game.\n\n")
            exit()
        else:
            clear()
            print(f" \u001b[31m{answer}\u001b[0m isn't a valid choice")
            menu_list()
            print(" \nPlease enter a valid input of either 1, 2, 3, 4 or 5")
            answer = input("").upper()


def instructions():
    """
    Game instructions will be printed if the user
    has never played the game.
    """
    clear()
    print(" 1) Game is played against the computer.")
    print(" 2) User enters either 'R'-Rock or 'P'-Paper or 'S'-Scissors.")
    print(" 3) Rock wins against scissors.")
    print(" 4) Scissors win against paper.")
    print(" 5) Paper wins against rock.")
    print(" 6) The user can see their score in section 3 of the main menu.")
    print(' ')
    print(' ')
    print(" Would you like to Play the game, go back to the Menu or Exit?")
    print(" Enter P to play")
    print(" Enter M to go to the Menu")
    answer = input(" Enter Q to exit game.\n >> ").upper()
    print('')
    while True:
        if answer == "P":
            play_game()
        elif answer == "M":
            menu()
        if answer == "Q":
            clear()
            print("Thank you for playing the game.\n\n")
            exit()

        else:
            clear()
            print(f"\n \u001b[31m{answer}\u001b[0m isn't a valid choice")
            print(" Please enter a valid input of either,")
            print(" 'P' to play, 'M' for Menu or 'Q' to exit.")
            answer = input("\n >> ").upper()
    clear()


def menu_list():
    print("\n Please enter your selection.")
    print(" 1). Play Rock Paper Scissors.")
    print(" 2). Read the instructions.")
    print(" 3). Enter to see your score.")
    print(" 4). Enter a new Username.")
    print(" 5). Exit the Game.")


def play_game():
    """
    Game is played here, enter R,P,S and computer picks random,
    if else to decide the winner. Results are displayed when enter is pressed.
    """
    choice = ["R", "P", "S"]
    computer = choice[randint(0, 2)]
    clear()
    global total  # Data for total games played for google sheets
    global win  # Data for games won for google sheets
    print(" Enter Q to save your results and Exit the game entirety.")
    print(" Enter M to save your results and go back to the Menu.")
    print("\n Please Enter R for Rock, P for Paper, and S for Scissors.")
    user = input("\n\n >> ").upper()
    if (user == 'R' and computer == 'R'):
        print(" You choose Rock, Computer picked Rock")
        print(" It's a Draw! " + username)
        total += 1
        input("\u001b[37m \n Press Enter to continue...")
        play_game()
    elif (user == 'P' and computer == 'P'):
        print(" You choose Paper, Computer picked Paper")
        print(" It's a Draw! " + username)
        total += 1
        input("\u001b[37m \n Press Enter to continue...")
        play_game()
    elif (user == 'S' and computer == 'S'):
        print(" You choose Scissors, Computer picked Scissors")
        print(" It's a Draw! " + username)
        total += 1
        input("\u001b[37m \n Press Enter to continue...")
        play_game()

    elif user == "R":
        if computer == "P":
            print(" You choose Rock, Computer picked Paper")
            print("\u001b[31m You Lose! " + username)
            input("\u001b[37m \n Press Enter to continue...")
            total += 1
            play_game()
        else:
            print(" You choose Rock, Computer picked Scissors")
            print("\u001b[32m You Win! " + username)
            win += 1
            total += 1
            input("\u001b[37m \n Press Enter to continue...")
            play_game()
    elif user == "P":
        if computer == "S":
            print(" You choose Paper, Computer picked Scissors")
            print("\u001b[31m You Lose! " + username)
            input("\u001b[37m \n Press Enter to continue...")
            total += 1
            play_game()
        else:
            print(" You choose Paper, Computer picked Rock")
            print("\u001b[32m You Win! " + username)
            win += 1
            total += 1
            input("\u001b[37m \n Press Enter to continue...")
            play_game()
    elif user == "S":
        if computer == "R":
            print(" You choose Scissors, Computer picked Rock")
            print("\u001b[31m You Lose " + username)
            input("\u001b[37m \n Press Enter to continue...")
            total += 1
            play_game()
        else:
            print(" You choose Scissors, Computer picked Paper")
            print("\u001b[32m You Win! " + username)
            win += 1
            total += 1
            input("\u001b[37m \n Press Enter to continue...")
            play_game()

    elif user == "Q":
        if total == 0:  # This stops a zero results going to google sheets.
            clear()
            print(" Thank you for playing the game.\n")
            exit()
        else:
            clear()
            update_sheets()  # updates google sheets with score and date.
            print(" Thank you for playing the game.\n")
            exit()
    elif user == "M":
        if total == 0:
            reset()
            menu()
        else:
            update_sheets()  # updates google sheets with score and date.
            reset()
            menu()
    else:
        print(f" \u001b[31m{user}\u001b[0m isn't a valid choice")
        print(" Please enter 'R' OR 'P' OR 'S' during game play.")
        input("\n Press Enter to continue...")
        play_game()


def print_score(username):
    """
    Gets data from google sheets(Username, Wins, Games, Date).
    Manipulates data in google sheets by showing only the current username.
    Uses addition sum to add the Wins and Games to a total.
    Can search for a user.
    """
    clear()
    data = sheet.get_all_values()
    username = username.lower()

    user_data = [row for row in data if row[0].strip().lower() == username]
    if user_data:
        last_10_scores = user_data[-10:] if len(user_data) > 10 else user_data
        total_wins = sum(int(row[7]) for row in last_10_scores)
        total_games = sum(int(row[19]) for row in last_10_scores)
        print(f" {username.upper()} :Over your last 10 Visits you have:")
        print(f" Won: {total_wins} Games out of: {total_games} Games in total")
        print(f"\n 1). To see {username.upper()} last 10 individual games.")
        print(" 2). Enter to search for a user name.")
        print(" 3). Return to the Menu Options.")
        scoresearch = input("\n Enter your number choice.\n >> ").upper()
        while True:
            if scoresearch == "1":
                clear()
                print(f" Up to your last 10 Scores: {username}")
                for row in last_10_scores:
                    print(f" {row[0]}, \
    Wins: {row[7]}, \
    Out of {row[19]} Games. \
    Date {row[28]}/{row[36]}/{row[45]}")  # prints username,wins,games and date
                print(f" {row[0]} \
    Total Wins: {total_wins} \
    Total Games: {total_games}\n")  # prints username,wins&games totals
                input("\u001b[37m \n Press Enter to continue.")
                username_to_search = username
                print_score(username_to_search)
            elif scoresearch == "2":
                username_to_search = input(" Enter a username: ")
                print_score(username_to_search)
            elif scoresearch == "3":
                menu()
            else:
                clear()
                print(f"\u001b[31m{scoresearch}\u001b[0m isn't a valid choice")
                input("\nPress Enter to return.")
                username_to_search = username
                print_score(username_to_search)

    else:
        print(" The user doesn't exist")
        print(" If this is your first time here,")
        print(" Please play the game to view a score.")
        input("\u001b[37m \n Press Enter to continue to return to Menu...")
        menu()


def update_sheets():
    """
    Sends total games and wins along,
    with date to google sheets.
    """
    userinfo.append_row([username], table_range='A2')
    userinfo.append_row([win], table_range='H2')
    userinfo.append_row([total], table_range='T2')
    x = datetime.datetime.now()
    year = (x.year)
    userinfo.append_row([year], table_range='AT2')
    month = (x.strftime("%b"))
    userinfo.append_row([month], table_range='AK2')
    day = (x.strftime("%d"))
    userinfo.append_row([day], table_range='AC2')


def reset():
    """
    Returns variables to their settings.
    """
    global total
    total = 0
    global win
    win = 0
    global incorrect
    incorrect = 4


def clear():
    """
    Clears the screen.
    """
    os.system('clear')


def print_slow(ltr):
    """
    Creates a slow typing effect.
    """
    for letter in ltr:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)


reset()
intro()
