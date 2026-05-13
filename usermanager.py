# -*- coding: utf-8 -*-
from user import User


class UserManager:

    def __init__(self):
        self.__users : list[User] = []

    def get_users(self) -> list[User]: return self.__users

    def set_users(self, newUsers:list[User]) -> None: self.__users = newUsers

    def add_user(self, userToAdd: User) -> None: self.get_users().append(userToAdd)

    def del_user(self, userToRemove:User) -> None: self.set_users([b for b in self.get_users() if b.get_name() != userToRemove.get_name()])

    def check_user(self, username:str) -> bool:
        return len([u for u in self.get_users() if u.get_name() == username]) == 1