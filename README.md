# GAME OF THRONES SQUIRE
## Note: Run "project.py" to begin the Game of Thrones Squire. 
###

The goal of this project was to test my introduction to Python skills while creating something relevant to my interests. 

This Game of Thrones Squire allows users to learn more about each published book, a few main houses, notable locations, and even discover similar books they may enjoy.

I hope this project displays my developing skills and interest in Python to create meaningful tools. I look forward to updating this program as I learn more.

____
books.py

1. def print_books(): This prints a list of books in the Song of Ice and Fire series
2. def book_choice(): Then, the program prompts the user for input to select one of those books. If the user doesn't type anything and hits enter, the program will quit. If the user types 'back', the program will return to the main starting page. If the user inputs a digit, it will return that number as an integer.
3. def load_books(): This opens a text file that contains information about each book, and separates the information by a "|" and prepares this information to print inside a dictionary.
4. def show_book_info(): This is a formatting function which takes the information gathered into a dictionary from step 3 and prints it in a user friendly manner. Then it asks for user input to continue providing information or to quit the program.
5. def get_book_info(): Puts this all together. If the user's selection is not in the text file, it will ask for another input. Otherwise, it will use the functions above to print information regarding that book.

___
houses.py
1. def print_houses(): This prints a list of popular houses in the Song of Ice and Fire series.
2. def book_choice(): Then, the program prompts the user for input to select one of those houses. If the user doesn't type anything and hits enter, the program will quit. If the user types 'back', the program will return to the main starting page. If the user inputs a digit, it will return that number as an integer.
3. def get_house_info(): This function opens a url to a photo of the house sigil and house words according to the user's input. If the user types 'back' it will return to the main starting page. If the user doesn't type anything and hits enter, the program will quit.


___
locations.py
1. def print_locations(): This prints a list of popular locations in the Song of Ice and Fire series.
2. def location_choice(): Then, the program prompts the user for input to select one of those locations. If the user doesn't type anything and hits enter, the program will quit. If the user types 'back', the program will return to the main starting page. If the user inputs a digit, it will return that number as an integer.
3. def get_location_info(): This function opens a url to a website with loads of information and pictures about the location according to the user's input. If the user types 'back' it will return to the main starting page. If the user doesn't type anything and hits enter, the program will quit.


___
nyt.py
1. def list_choices(): This prompts the user for input. If the user doesn't type anything and hits enter, the program will quit. If the user types 'back', the program will return to the main starting page. If the user inputs a digit, it will return that number as an integer.
2. def hardcover_list() and paperback_list(): These functions are essentially the same, just with different https links for each respective lists. This uses an API key to get information from the New York Times best sellers list for Fiction, parses it using json, then formats it into a user friendly table view using tabulate.
3. def get_list_info(): This calls the functions above depending on the users input. If the user types 'back' it will return to the main starting page. If the user doesn't type anything and hits enter, the program will quit.


___
project.py
1. def main(): Uses the following functions to gather user input and route the user to the proper topic.
2. def print_welcome_screen(): Print the welcome starting menu.
3. def main_menu_choice(): Prompt the user to select a topic and return the input.
4. def print_back_menu(): Let the user know they cannot go 'back' from the main menu.
5. def print_invalid_selection(): Let the user know they entered an invalid selection.

___
test_project.py

This python file tests my code using pytest and monkeypatch. This tests functions inside of the main project.py file. The first function makes sure if the user hits Enter, the program will quit. The second function makes sure the users input is returned properly in an invalid chocie is selected. The third function makes sure the program goes to the previous page if the user types 'back'.
