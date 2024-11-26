
import add_books
import view_books


file_name = "../Dataset/books.csv"

menu = {
    0: "Exit",
    1: "Add",
    2: "View",    
}


while True:
    for key, value in menu.items():
        print(f"{key} : {value}")

    key = int(input("Your choice : "))

    if key == 0:
        exit()
    if key == 1:
        add_books.AddBooks(file_name)
    elif key == 2:
        view_books.ViewBooks(file_name)
    else:
        print("Invalid Input") 
