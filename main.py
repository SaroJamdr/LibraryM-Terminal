from library import Library
from book import Book

def main():
    library = Library()
    
    while True:
        print("\n--- Personal Library Management System ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Books")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == '1':
            title = input("Enter book title: ").strip()
            if not title:
                print("Title cannot be empty.")
                continue

            author = input("Enter book author: ").strip()
            if not author:
                print("Author cannot be empty.")
                continue

            year = input("Enter book year: ").strip()
            if not year.isdigit():
                print("Year must be a number.")
                continue

            isbn = input("Enter book ISBN: ").strip()
            if not isbn:
                print("ISBN cannot be empty.")
                continue
            if any(book.title == isbn for book in library.view_books()):
                print("A book with this ISBN already exists.")
                continue

            book = Book(title, author, year, isbn)
            library.add_book(book)
            library.save_to_file()
            print("Book added successfully.")

        elif choice == '2':
            books = library.view_books()
            if books:
                print("\n--- Books in Library ---")
                for book in books:
                    print(book)
            else:
                print("No books in the library.")


        elif choice == '3':
            query = input("Enter title or author to search: ").strip()
            if not query:
                print("Search query cannot be empty.")
                continue

            results = library.search_books(query)
            if results:
                print("\n--- Search Results ---")
                for book in results:
                    print(book)
            else:
                print("No books found.")


        elif choice == '4':
            search_title = input("Enter the title of the book to update: ").strip()

            if not search_title:
                print("Title cannot be empty.")
                continue

            if not any(book.title.lower() == search_title.lower() for book in library.view_books()):
                print("Book with this title does not exist.")
                continue

            new_title = input("Enter new book title: ").strip()
            new_author = input("Enter new book author: ").strip()
            new_year = input("Enter new book year: ").strip()
            new_isbn = input("Enter new book ISBN: ").strip()

            if not new_title or not new_author or not new_year.isdigit() or not new_isbn.isdigit():
                print("Invalid input. Make sure all fields are filled and year is numeric.")
                continue

            if library.update_book(search_title, new_title, new_author, new_year, new_isbn):
                library.save_to_file()
                print("Book updated successfully.")
            else:
                print("Book not found.")


        elif choice == '5':
            title = input("Enter title of the book to delete: ").strip()
            if not title:
                print("Title cannot be empty.")
                continue
            if library.delete_book(title):
                library.save_to_file()
                print("Book deleted successfully.")
            else:
                print("Book not found.")


        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid option (1-6).")

if __name__ == "__main__":
    main()
