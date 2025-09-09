import requests
from utils import clear_screen, quit_program
from tabulate import tabulate


############################################################################################################
## GET THE USERS LIST CHOICE ##
def list_choice():
    user_input = input("Would you like to see hardcover or paperback recommendations? ").strip().lower()

    if user_input == "":
        quit_program()

    elif user_input == "back":
        return "back"

    elif user_input.isdigit():
        return int(user_input)

    else:
        return None

############################################################################################################
def hardcover_list():
    API_KEY = "QtJafAsmDkNgAz6v1eGOgdPzpTWFGmex"

    url = "https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json"
    params = {"api-key": API_KEY}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        books = data["results"]["books"]

        table = []

        for i, book in enumerate(books, start = 1):
            table.append([i, book['title'].title(), book['author'], book['weeks_on_list']])

        headers = ["Rank", "Title", "Author", "Weeks on List"]
        print(tabulate(table, headers, tablefmt = "fancy_grid"))

    else:
        print("Error:", response.status_code, response.text)

############################################################################################################
def paperback_list():
    clear_screen()
    print("NYT Best Sellers List for Paperback Fiction:\n")
    API_KEY = "QtJafAsmDkNgAz6v1eGOgdPzpTWFGmex"

    url = "https://api.nytimes.com/svc/books/v3/lists/current/trade-fiction-paperback.json"
    params = {"api-key": API_KEY}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        books = data["results"]["books"]

        table = []

        for i, book in enumerate(books, start = 1):
            table.append([i, book['title'].title(), book['author'], book['weeks_on_list']])

        headers = ["Rank", "Title", "Author", "Weeks on List"]
        print(tabulate(table, headers, tablefmt = "fancy_grid"))

    else:
        print("Error:", response.status_code, response.text)

############################################################################################################
def get_list_info():
    while True:
        clear_screen()
        print("Here are two book recommendation options from the New York Times Best Sellers list.\n" \
        "These lists are current.\n\n"
        "1. Hardcover Fiction\n" \
        "2. Paperback Trade Fiction\n")

        user_input = list_choice()

        if user_input == "back":
            return

        elif user_input == 1:
            clear_screen()
            print("NYT Best Sellers List for Hardcover Fiction:\n")
            hardcover_list()

        elif user_input == 2:
            paperback_list()

        else:
            input(f"\nInvalid selection. Please select list 1 or 2. ").strip().lower()

        user_input = input("\nIf you would like to know more about another list, type 'back' to return to the list menu. " \
        "\n\nOtherwise, press 'Enter' to quit the program. ").strip().lower()

        if user_input == "":
            quit_program()

############################################################################################################
