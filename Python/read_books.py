
def ReadBooks(file_name):
    
    with open(file_name, 'r') as file:
        lines = file.readlines()
    
    books = []
    for  line in lines:
        books.append(line)
    
    return books