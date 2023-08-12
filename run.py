"""
Modules
"""
import random
from random import randint
import sys
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2.service_account import Credentials


choice = ["R", "P", "S"]
computer = choice[randint(0,2)]
level = 0
win = 0
lose = 0
total = 0


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
userinfo = SHEET.worksheet('userinfo')




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
    clear() 
    reset()
    global username
    print('')
    username = input(" Please enter username: \n >> ").upper()
    time.sleep(2)
    menu()

def menu():
    """ 
    User can picks there option on where to go.
    """
    clear()
    print("\n Welcome " + username)
    print("\n Please enter your selection.")
    print("\n 1)....Press 1 and then Enter to play Rock Paper Sicssors.")
    print("\n 2)....Press 2 and then Enter to read the instruction's.")
    print("\n 3)....Press 3 and then Enter to see your score.")
    print("\n 4)....Press 4 and then Enter to Enter a new Username.")
    print("\n 5)....Press 5 and then Enter to Exit the Game.")
    #print("\nWould you like to read the Game Instructions " + username)
    answer = input("\n\n Please enter your choice.\n >> ").upper()
    # print(userscore.cell(3,1).value) this works
    print('')
    while True:
        if answer == "1":
            play_game()
        elif answer == "2":
            instructions()
        if answer == "3":
            username_to_search = username
            print_score(username_to_search)
        elif answer =="4":
            enter_username()
        if answer == "5":
            clear()
            print(" Thank you for playing the game.\n\n")
            exit()
        else:
            print('')
            print(" Please enter a valid input of either 1, 2, 4 or 5\n")
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
            clear()
            print("Thank you for playing the game.\n\n")
            exit()

        else:
            print('')
            print(" Please enter a valid input of either P to play, M for Menu or E to exit\n")
            answer = input("").upper()
    clear()


def play_game():
    choice = ["R", "P", "S"]
    computer = choice[randint(0,2)]
    clear()
    global total
    global win
    print(" Enter Q to save your results and Exit the game entirety.")
    print(" Enter M to save your results and go back to the Menu.")
    user = input("\u001b[37m\n Please choose _ R for Rock, P for Paper, and S for Scissors.\n\n >> ").upper()
    if (user == 'R' and computer == 'R'):
        print(" You choose Rock, Computer picked Rock")
        print(" It's a Draw! "+ username)
        total += 1
        input("\u001b[37m \n Press Enter to continue...")
        play_game()
    elif (user == 'P' and computer == 'P'):
        print(" You choose Paper, Computer picked Paper")
        print(" It's a Draw! "+ username)
        total += 1
        input("\u001b[37m \n Press Enter to continue...")
        play_game()
    elif (user == 'S' and computer == 'S'):
        print(" You choose Scissors, Computer picked Scissors")
        print(" It's a Draw! "+ username)
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
            clear()
            userinfo.append_row([username], table_range='A2')
            userinfo.append_row([win], table_range='H2')
            userinfo.append_row([total], table_range='T2')
            print(" Thank you for playing the game.")
            exit()
    elif user == "C":
            clear() 
    elif user == "M":
            userinfo.append_row([username], table_range='A2')
            userinfo.append_row([win], table_range='H2')
            userinfo.append_row([total], table_range='T2')
            reset()
            menu()
    else:
        print(" That input isn't valid.")
        print(" Please enter one of the following letters 'R' OR 'P' OR 'S' during game play.")
        input("\u001b[37m \nPress Enter to continue...")
        play_game()
        



def print_score(username):
    # print(userinfo.range('A2:A28'))
    # time.sleep(5)
    
    # userinfo.resize(10,10) # resize rows and columns of sheet
    # df = userinfo.get_as_df() # create the dataframe 
    # print(df)
    clear()
    data = sheet.get_all_values()
    username = username.lower()

    user_data = [row for row in data if row[0].strip().lower() == username]
    if user_data:
        last_10_scores = user_data[-10:] if len(user_data) > 10 else user_data
        total_wins = sum(int(row[7]) for row in last_10_scores)
        total_games = sum(int(row[19]) for row in last_10_scores)

        # for row in last_10_scores:
        #     print("username: {row[0]}, wins: {row[7]}, Total games: {row[19]}")

        print(f" {username.capitalize()} Over a max of your last 10 Visits you have:")
        print(f" Won: {total_wins} Games out of: {total_games} Games in total\n")
        # print(f"Total Games played over your last 10 visits: {total_games}")
        print("\n Press 1 and then Enter to search for a user name.")
        print(" Press 2 and then Enter to return to the Menu Options.")
        scoresearch = input("\n Please enter your choice.\n >> ").upper()
        while True:
            if scoresearch == "1":
                username_to_search = input(" Enter a username: ")
                print_score(username_to_search)
            elif scoresearch == "2":
                menu()

            else:
                print(" That input isn't valid.")
                input("\u001b[37m \n Press Enter to continue...")
                username_to_search = username
                print_score(username_to_search)

    else:
        print(" No User Name was found.")
        input("\u001b[37m \n Press Enter to continue to return to Menu...")
        menu()

    

    # userinfo = SHEET.worksheet("userinfo")
    # column = userinfo.col_values(1)
    # print(column)






    # for cell in userinfo.range('A2:A8'):
    #     print(cell.value)
    # for cell in userinfo.range('H2:H8'):
    #     print(cell.value)
    # for cell in userinfo.range('T2:T8'):
    #     print(cell.value)
        
    
    # # this code works
    # columns = []
    # for ind in range (1, 2):
    #     column = userinfo.col_values(ind)
    #     columns.append(column[-5:])
    #     print(columns)
    # for ind in range (8, 9):
    #     column = userinfo.col_values(ind)
    #     columns.append(column[-5:])
    #     print("\n")
    #     print(columns)
    # for ind in range (20, 21):
    #     column = userinfo.col_values(ind)
    #     columns.append(column[-5:])
    #     print("\n")
    #     print(columns)
    


    # print(ind)
    # print(name, won, complete)
    # print("%s you won %s games out of %s" % (name, won, complete))
    
    
    
    # sales = sheet.worksheet("sales")
    # userinfo = sales.col_values(0)
    # print(userinfo)

    # results = userinfo.values().get(spreadsheetId=SPREADSHEET_ID, range="userinfo!A1:A20").execute()
    # # values = result.get("values", [])
    # values = result.get('values', [])
    # for row in values:
    #         # Print columns A and H and T, which correspond to indices 0 and 7.
    #         print('%s, %s, %s' % (row[0], row[7], row[19]))

    # for row in values:
    #     print(row)
    # for cell in userinfo.range('A2:A28','H2:H28','T2:T28'):
    #     print(cell.value)
    # time.sleep(5)
    # print("--------*-*-*-*-*-*-*-*-*-*-*-*----------")
    # print(userinfo.acell('A12').value)
    # print("--------*-*-*-*-*-*-*-*-*-*-*-*----------")
    # username = input("Please enter username: \n>> ").upper()
    # userinfo.append_row([username], table_range='A2')
    # userrow = userinfo.row_values(5)
    # userrow2 = userinfo.get_all_records()
    # print(userrow)
    # print("--------*-*-*-*-*-*-*-*-*-*-*-*----------")
    # print(userrow2)
    # print(userinfo.get('A3:T16'))
    # userinfo.get([username], table_range='A2:A200')
    # print("--------*-*-*-*-*-*-*-*-*-*-*-*----------")
    # print('Rows: ',userinfo.row_count)

    exit()



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


# username_to_search = input("Enter a username: ")
# print_score(username_to_search)
reset()
intro()
