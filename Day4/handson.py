# Scenario: Bookstore Inventory Management
# Main Options:
# 1. Add a book to inventory
# 2. Display current inventory
# 3. Update book quantity
# 4. Exit


def add_book(a):
    name=input("Enter Name : ")
    qunitity=int(input("Enter Number of qunitity : "))
    a[name]=qunitity
    print(a)

def show_book(a):
    print("Available books")
    print("Book name   Quantity")
    for b,i in a.items():
        print(b ," :    ", i)

def update_quantity(a):
    print("show books which book update ")
    print("Book name   Quantity")
    for b,i in a.items():
        print(b ," : ", i)

    name=input("Enter book name : ")
    if name in a:
        qun=int(input("Enter update quantity : "))
        a[name]=qun

def main():
    a={}
    while True:
        print("1. Add book")
        print("2. Show Books")
        print("3. Update quantity")
        print("4. Exit")
        choice=int(input("Enter Number : "))

        if choice==1:
            add_book(a)
        elif choice==2:
            show_book(a)
        elif choice==3:
            update_quantity(a)
        else :
            print("Exit Program")
            break


if __name__ == "__main__":
    main()