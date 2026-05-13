# -*- coding: utf-8 -*-
from book import Book


class BookCollection:

    def __init__(self, books: list) -> None:
        self.__books = books

    def get_books(self) -> list: return self.__books

    def set_books(self, newBooks:list) -> None: self.__books = newBooks

    def add_book(self, bookToAdd: Book) -> None: self.get_books().append(bookToAdd)

    def del_book(self, bookToRemove:Book) -> None: self.set_books([b for b in self.get_books() if b.get_id() != bookToRemove.get_id()])

    
