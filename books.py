from utils import clear_screen, quit_program

############################################################################################################

## PRINT THE BOOK MENU ##

def print_books():
    print("1. A Game of Thrones")
    print("2. A Clash of Kings")
    print("3. A Storm of Swords")
    print("4. A Feast for Crows")
    print("5. A Dance with Dragons\n")

############################################################################################################

## GET THE USERS BOOK CHOICE ##
def book_choice():
    user_input = input("Select a book you would like to know more information about. ").strip().lower()

    if user_input == "":
        quit_program()

    elif user_input == "back":
        return "back"

    elif user_input.isdigit():
        return int(user_input)

    else:
        return None

############################################################################################################

## LOAD INFORMATION FROM FILE ##
def load_books(filename):
    books = {}
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("|", 4)  # Number|Title|Author|Published|Summary
                if len(parts) < 5:
                    print(f"Skipping malformed line: {line}")
                    continue
                number = int(parts[0])
                books[number] = {
                    "Title": parts[1],
                    "Author": parts[2],
                    "Published": parts[3],
                    "GoodReads Summary": parts[4]
                }
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

    return books

############################################################################################################

## SHOW BOOK INFO ##
def show_book_info(book):
    clear_screen()
    print(f"Title: {book['Title']}\n")
    print(f"Author: {book['Author']}\n")
    print(f"Published: {book['Published']}\n")
    print(f"GoodReads Summary:\n{book['GoodReads Summary']}\n")

    user_input = input("If you would like to know more about another book, type 'back' to return to the book menu. " \
    "\n\nOtherwise, press 'Enter' to quit the program. ").strip().lower()

    if user_input == "":
        quit_program()

############################################################################################################

## GET BOOK INFO FROM BOOKS.TXT ##
def get_book_info():
    books = load_books("books.txt")
    if not books:
        input("Please select a valid book between 1 and 5.").strip().lower()
        return

    while True:
        clear_screen()
        print("Here are the currently released books in George R.R. Martin's series 'A Song of Ice and Fire':\n")
        print_books()
        user_input = book_choice()

        if user_input == "back":
            return

        elif user_input is None:
            input("Invalid selection. Please select a valid book between 1 and 5.").strip().lower()
            continue

        elif user_input in books:
            show_book_info(books[user_input])

        else:
            input(f"\nInvalid selection. Please select a valid book between 1 and 5. ").strip().lower()

############################################################################################################
