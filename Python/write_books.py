

def WriteBooks(file_name, books):
    
    with open(file_name, 'w') as file:
        for book in books:
            file.write(book)
    