
file_name = "../Dataset/books.txt"


class Library:
    
    def __init__(self):
        print("Welcone to Library")
    
    def add(self, book):
        with open(file_name, 'r') as file:
            global books
            books = [line.strip() for line in file]
        books.append(book)
        with open(file_name, 'w') as file:
            for b in books:
                file.write(b + "\n")
        


    
    def display(self):
       with open(file_name, 'r') as file:
           books = [line.strip() for line in file]
           print(f"Books are : {books}")



menu = {
    0: "Exti",
    1: "Add",
    2: "View",    
}

ob = Library()

while True:
    for key, value in menu.items():
        print(f"{key} : {value}")

    key = int(input("Your choice : "))

    if key == 0:
        exit()
    if key == 1:
        book = input("Book name : ")
        ob.add(book)
    elif key == 2:
        ob.display()
    else:
        print("Invalid Input") 
