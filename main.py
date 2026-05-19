# -*- coding: utf-8 -*-
from bookcollection import BookCollection
from usermanager import UserManager
from user import User
from book import Book

def add_book() -> None:
    book_title_input = input("Title : \n")
    book_author_input = input("Author : \n")
    book_year_input = input("Year : \n")
    book_category_input = input("Category : \n")
    new_book:Book = Book(book_title_input, book_author_input, book_year_input, book_category_input)
    new_book.set_id(book_collection.get_first_free_id())
    book_collection.add_book(new_book)
    book_collection.save_books()

if __name__ == "__main__":
    print("Starting BookManagerCLI")
    is_user_connected: bool = False
    user_manager = UserManager();
    user_manager.add_user(User("ab"))

    book_collection = BookCollection([])
    book_collection.reload_books()

    menu = {"0" : add_book}
    
    while True:
        if not is_user_connected:
            login_input = input("Login : Enter your username : \n")
            result = user_manager.check_user(login_input)
            if  result == True:
                print("User logged, welcome...")
                is_user_connected = True
            else:
                print("User does not exist...")
        else:
            try:
                menu_input = input("Menu: \n- 1 : Ajouter un livre\n - 2 : Supprimer un livre\n - 3 : Modifier les informations d’un livre\n - 4 : Rechercher un livre\n")
                menu[f"{menu_input}"]()
                print(f"{len(book_collection.get_books())}")
            except KeyError:
                print("Enter a valid option!")

            
