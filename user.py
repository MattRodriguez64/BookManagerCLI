# -*- coding: utf-8 -*-

class User:

    def __init__(self, name:str) -> None:
        self.__name = name

    def get_name(self) -> str: return self.__name
    def set_name(self, newName:str) -> None: self.__name = newName