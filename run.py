import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('tic_tac_toe')

sales = SHEET.worksheet('userinfo')

# data = sales.get_all_values()

# print(data)




def intro():
    """
    This is the opening to the game
    User can pick to play or read the instructions.
    """
    clear()
    print('')
    print("Welcome to Tic Tac Toe\n")
    username = input("Please enter username:")
    print("\nWould you like to read the Game Instructions " + username)
    answer = input("Enter Y to read or N to continue to game\n").upper()
    print('')
    while True:
        if answer == "Y":
            instructions()
        elif answer == "N":
            clear()
            opening()

        else:
            print('')
            print("Please enter a valid input of either Y or N\n")
            answer = input("").upper()


# def instructions():
    """ 
    Game instructions will be printed if the user
    has never played the game.
    """
    clear()
    print(" 1) Game is played on a grid of 3x3 for 2 players.")
    print(" 2) X's and O's are used for each player.")
    print(" 3) A player takes turns againest the compluter.")
    print(" 4) The idea is to get 3 in a row.")
    print(' ')
    time.sleep(15)
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
# def play_game():
# def get_high_score():
#     """
#     Gets the high score from user who have played the game
#     """

def clear():
    """
        Clears the screen
    """
    print("\033c")
    
intro()