
from menu import Menu
from users import Customer, Admin, Employee
from restaurant import Restaurant
from orders import Order

mamar_restaurant = Restaurant("Mamar Restaurant")
def Customer_menu():
    name=input("Enter your name: ")
    email=input("Enter your email: ")
    phone=input("Enter your phone: ")
    address=input("Enter your address: ")

    customer=Customer(name=name, email=email, phone=phone, address=address)

    while True:
        print(f"Welcome {customer.name} ):")
        print("1. View Menu")
        print("2. Add item to cart")
        print("3. View Cart")
        print("4. Pay Bill")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            customer.view_menu(mamar_restaurant)
        elif choice == 2:
            item_name = input("Enter item name: ")
            item_quantity = input("Enter item quantity: ")
            customer.add_to_cart(mamar_restaurant, item_name, item_quantity )
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.bay_bill()
        elif choice == 5:
            break
        else:
            print("Invalid Input")


def admin_menu():
    name=input("Enter your name: ")
    email=input("Enter your email: ")
    phone=input("Enter your phone: ")
    address=input("Enter your address: ")

    admin=Admin(name=name, email=email, phone=phone, address=address)

    while True:
        print(f"Welcome {admin.name} ):")
        print("1. Add new Item")
        print("2. Add new Employee")
        print("3. View Employee")
        print("4. View Items")
        print("5. Delete Items")
        print("6. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            item_name = input("Enter Your item Name: ")
            item_price = int(input("Enter Your Item Price: "))
            item_quantity = int(input("Enter Your Item Quantity: "))
            item = FoodItem(item_name, item_price, item_quantity)
            admin.view_menu(mamar_restaurant, item)

        elif choice == 2:
            name = input("Enter employee name: ")
            phone = input("Enter employee phone: ")
            email = input("Enter employee email: ")
            designation = input("Enter employee designation: ")
            age= input("Enter employee age: ")
            salary= input("Enter employee salary: ")
            address = input("Enter employee address: ")
            admin.add_employee(name, phone, email, address, salary, age, designation)

        elif choice == 3:
            admin.view_employee(mamar_restaurant)
        elif choice == 4:
            admin.view_menu(mamar_restaurant)
        elif choice == 5:
            item_name = input("Enter item name: ")
            admin.remove_item(mamar_restaurant,item_name)
        elif choice == 6:
            break
        else:
            print("Invalid Input")


while True:
    print("Welcome !!")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    choice = int (input("Enter your choice: "))
    if choice ==1:
        Customer_menu()
    elif choice ==2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid Input.")