import json
from book import Book

class Library:
    def __init__(self, filename='library.json'):
        self.books = []
        self.filename = filename
        self.load_from_file()

    def add_book(self, book):
        self.books.append(book)

    def view_books(self):
        return self.books

    def search_books(self, query):
        results = []
        for book in self.books:
            if query.lower() in book.title.lower() or query.lower() in book.author.lower():
                results.append(book)
        return results 

    def update_book(self, old_title, new_title, new_author, new_year, new_isbn):
        for book in self.books: 
            if book.title.lower() == old_title.lower(): 
                book.title = new_title
                book.author = new_author
                book.year = new_year 
                book.isbn = new_isbn
                return True
        return False 

    def delete_book(self, title):
        initial_count = len(self.books)
        self.books = [book for book in self.books if book.title != title]
        return len(self.books) < initial_count

    def save_to_file(self):
        with open(self.filename, 'w') as f:
            json.dump([book.to_dict() for book in self.books], f)

    def load_from_file(self):
        try:
            with open(self.filename, 'r') as f:
                books_data = json.load(f)
                self.books = [Book.from_dict(data) for data in books_data]
        except FileNotFoundError:
            self.books = []