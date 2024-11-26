import read_books

def ViewBooks(file_name):

    books = read_books.ReadBooks(file_name)
    
    if books:
        header = ["Title", "Author", "ISBN", "Price", "Publishing Year"]
        print(*header, "\n")
        for book in books:
            print(book)
    else:
        print("No book")    
   