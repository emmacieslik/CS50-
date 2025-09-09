import sys
from utils import clear_screen
from books import get_book_info
from houses import get_house_info
from locations import get_location_info
from nyt import get_list_info

############################################################################################################
### MAIN FUNCTION ###
def main():
    while True:
        clear_screen()
        print_welcome_screen()
        print_main_menu()

        user_input = main_menu_choice()

        if user_input == "":
            sys.exit(0)  # Clean exit for autograder

        elif user_input == "1":
            get_book_info()
        elif user_input == "2":
            get_house_info()
        elif user_input == "3":
            get_location_info()
        elif user_input == "4":
            get_list_info()
        elif user_input == "back":
            print_back_message()
        else:
            print_invalid_selection()

### PRINT WELCOME SCREEN ###
def print_welcome_screen():
    print("Welcome! I am your Game of Thrones Squire.")
    print("Press 'Enter' anytime to quit. Type 'back' to return to the menu.\n")

### PRINT MAIN MENU ###
def print_main_menu():
    print("1. Book Information")
    print("2. House Sigils")
    print("3. Important Locations")
    print("4. Book Recommendations")

### PROMPT AND RETURN USER INPUT ###
def main_menu_choice():
    user_input = input("\nPlease choose a topic: ").strip().lower()
    return user_input

### BACK ERROR MESSAGE ###
def print_back_message():
    print("\nYou cannot go back. Please select a topic or quit the program.\n")
    input("Press 'Enter' to continue.\n")

### INVALID SELECTION ERROR MESSAGE ###
def print_invalid_selection():
    print("Invalid selection. Choose between 1 and 4.")
    input("Press 'Enter' to continue.\n")

### RNU PROGRAM ###
if __name__ == "__main__":
    main()
