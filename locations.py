
import webbrowser
from utils import clear_screen, quit_program

############################################################################################################

## PRINT LOCATION MENU ##

def print_locations():
    print("1. King's Landing")
    print("2. Winterfell")
    print("3. The Wall")
    print("4. Dragonstone")
    print("5. Braavos\n")

############################################################################################################

## GET THE USERS LOCATION CHOICE ##
def location_choice():
    user_input = input("Select a location you would like to learn more about.\n"
    "Please note, selecting a number will open a link in your web browser. ").strip().lower()

    if user_input == "":
        quit_program()

    elif user_input == "back":
        return "back"

    elif user_input.isdigit():
        return int(user_input)

    else:
        print("Select a valid location")


## SELECT PHOTO ##

def get_location_info():
    while True:
        clear_screen()
        print("Here are a list of locations I can help you learn more about.\n")
        print_locations()

        user_input = location_choice()
        if user_input == "back":
            return

        elif user_input == 1:
            url = "https://www.ign.com/wikis/game-of-thrones/King's_Landing"
            webbrowser.open(url)

        elif user_input == 2:
            url = "https://www.ign.com/wikis/game-of-thrones/winterfell"
            webbrowser.open(url)

        elif user_input == 3:
            url = "https://www.ign.com/wikis/game-of-thrones/The_Wall"
            webbrowser.open(url)

        elif user_input == 4:
            url = "https://www.ign.com/wikis/game-of-thrones/Isle_of_Dragonstone"
            webbrowser.open(url)

        elif user_input == 5:
            url = "https://www.ign.com/wikis/game-of-thrones/braavos"
            webbrowser.open(url)

        else:
            input(f"\nInvalid selection. Please select a valid location between 1 and 5. ").strip().lower()

        user_input = input("\nIf you would like to know more about another House, type 'back' to return to the House menu. " \
        "\n\nOtherwise, press 'Enter' to quit the program. ").strip().lower()

        if user_input == "":
            quit_program()
