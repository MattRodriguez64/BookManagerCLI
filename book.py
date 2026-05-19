# -*- coding: utf-8 -*-


class Book:
    def __init__(self, title:str, author:str, year:int, category:str):
        self.__id = -1
        self.__title = title
        self.__author = author
        self.__year = year
        self.__category = category
        self.__isAvailable = True

    def __str__(self):
        return f"{self.get_id()} : {self.get_title()} : {self.get_author()} : {self.get_year()} : {self.get_category()} : {self.get_isAvailable()}"
    
    def __repr__(self):
        return f"Book({self.get_id()}, {self.get_title()}, {self.get_author()}, {self.get_year()}, {self.get_category()}, {self.get_isAvailable()})"

    def get_id(self) -> int: return self.__id
    def set_id(self, newId:int) -> None: self.__id = newId

    def get_title(self) -> str: return self.__title
    def set_title(self, newTitle:str) -> None: self.__title = newTitle

    def get_author(self) -> str: return self.__author
    def set_author(self, newAuthor:str) -> None: self.__author = newAuthor

    def get_year(self) -> int: return self.__year
    def set_year(self, newYear:int) -> None: self.__year = newYear

    def get_category(self) -> str: return self.__category
    def set_category(self, newCategory:str) -> None: self.__category = newCategory

    def get_isAvailable(self) -> bool: return self.__isAvailable
    def set_isAvailable(self, newIsAvailable:bool) -> None: self.__isAvailable = newIsAvailable

    def save_format(self) -> dict : 
        return {"id": self.get_id(), "title":self.get_title(), "author":self.get_author(), "year": self.get_year(), "category": self.get_category(), "isAvailable":self.get_isAvailable()}