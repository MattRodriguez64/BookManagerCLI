# -*- coding: utf-8 -*-
from bookcollection import BookCollection
from usermanager import UserManager
from user import User


if __name__ == "__main__":
    print("Starting BookManagerCLI")
    is_user_connected: bool = False
    user_manager = UserManager();
    user_manager.add_user(User("ab"))
    
    while True:
        if not is_user_connected:
            login_input = input("Login : Enter your username : \n")
            result = user_manager.check_user(login_input)
            if  result == True:
                print("User logged, welcome...")
                is_user_connected = True
            else:
                print("User does not exist...")
