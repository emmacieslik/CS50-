import webbrowser
from utils import clear_screen, quit_program

############################################################################################################

## PRINT THE HOUSE MENU ##

def print_houses():
    print("1. House Stark")
    print("2. House Lannister")
    print("3. House Targaryen")
    print("4. House Tyrell")
    print("5. House Greyjoy")
    print("6. House Baratheon\n")

############################################################################################################

## GET THE USERS HOUSE CHOICE ##
def house_choice():
    user_input = input("Select a House to see it's Sigil.\n"
    "Please note, selecting a number will open a link in your web browser. ").strip().lower()

    if user_input == "":
        quit_program()

    elif user_input == "back":
        return "back"

    elif user_input.isdigit():
        return int(user_input)

    else:
        print("Select a valid House.")

############################################################################################################

## SELECT PHOTO ##

def get_house_info():
    while True:
        clear_screen()
        print("Here are a list of Houses I can help you learn more about.\n")
        print_houses()

        user_input = house_choice()

        if user_input == "back":
            return

        elif user_input == 1:
            url = "https://oyster.ignimgs.com/mediawiki/apis.ign.com/game-of-thrones/5/55/Wallpaper-stark-sigil-1600.jpg?width=1920"
            webbrowser.open(url)

        elif user_input == 2:
            url = "https://oyster.ignimgs.com/mediawiki/apis.ign.com/game-of-thrones-telltale/8/81/Lannister.jpg?width=1280"
            webbrowser.open(url)

        elif user_input == 3:
            url = "https://i.sstatic.net/LnmGBl.jpg"
            webbrowser.open(url)

        elif user_input == 4:
            url = "https://oyster.ignimgs.com/mediawiki/apis.ign.com/game-of-thrones/a/ab/House_Tyrell.png?width=230&format=jpg&auto=webp&quality=80"
            webbrowser.open(url)

        elif user_input == 5:
            url = "https://oyster.ignimgs.com/mediawiki/apis.ign.com/game-of-thrones-telltale/0/03/Greyjoy.jpg?width=1920"
            webbrowser.open(url)

        elif user_input == 6:
            url = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiXnomKgrCh1WTk1jOVNAUgN2ktZEQb3HsUgmNjOS3TuI164ptvKhyx_u_UqcOrsdqsFfSvdaUTOSrevEQhQtE0RFLY-v8XyfkCIdghqHdfekvM5tN1LtOT0jkQlUPEiA3kfrrcOj2oB_c/s1600/house_baratheon_wallpaper_by_siriuscrane-d53id3m-600x450.jpg"
            webbrowser.open(url)

        else:
            input(f"\nInvalid selection. Please select a valid location between 1 and 5. ").strip().lower()

        clear_screen()
        user_input = input("\nIf you would like to know more about another House, type 'back' to return to the House menu. " \
        "\n\nOtherwise, press 'Enter' to quit the program. ").strip().lower()

        if user_input == "":
            quit_program()

############################################################################################################
