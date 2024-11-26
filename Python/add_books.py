
import write_books
import read_books


def AddBooks(file_name):
    
    book = {}
    book["title"] = input("Title : ")
    book["author"] = input("Author : ")
    book["isbn"] = input("ISBN : ")
    book["price"] = input("Price : ")
    book["publishing_year"] = input("Publishing Year : ")


    book_line = f"{book["title"]}, {book["author"]}, {book["isbn"]}, {book["price"]}, {book["publishing_year"]}\n"
    
    books = read_books.ReadBooks(file_name)
    books.append(book_line)
    write_books.WriteBooks(file_name, books)


