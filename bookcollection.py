# -*- coding: utf-8 -*-
from book import Book
import json


class BookCollection:

    def __init__(self, books: list) -> None:
        self.__books = books
        self.__firstFreeId:int = 0

    def get_books(self) -> list: return self.__books

    def set_books(self, newBooks:list) -> None: self.__books = newBooks

    def add_book(self, bookToAdd: Book) -> None: 
        self.get_books().append(bookToAdd)
        self.increment_first_free_id()

    def del_book(self, bookToRemove:Book) -> None: self.set_books([b for b in self.get_books() if b.get_id() != bookToRemove.get_id()])

    def get_first_free_id(self) -> int : return self.__firstFreeId

    def set_first_free_id(self, new_id:int) -> None : self.__firstFreeId = new_id

    def increment_first_free_id(self) -> None : self.set_first_free_id(self.get_first_free_id() + 1)

    def save_books(self) -> None:
        first = [b.save_format() for b in self.get_books()]
        with open('books.json', 'w') as file:
            json.dump(first, file)

    def reload_books(self) -> None:
        temp_books:list = []
        temp_first_free_id:int = 0
        with open('books.json', 'r') as file:
            data = json.load(file)
            for item in data:
                temp_saved_book:Book = Book(item['title'], item['author'], item['year'], item['category'])
                temp_saved_book.set_id(item['id'])
                temp_saved_book.set_isAvailable(item['isAvailable'])
                temp_books.append(temp_saved_book)

                if item['id'] > temp_first_free_id:
                    temp_first_free_id = item['id']
                
        self.set_books(temp_books)
        temp_first_free_id += 1
        self.set_first_free_id(temp_first_free_id)