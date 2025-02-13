from abc import ABC


class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()

    def add_to_cart(self, restaurant, item_name, quantity):
        item = restaurant.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print("Item quantity exceeded !!")
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print("Item added (:")
        else:
            print("Item not found!")
    
    def view_cart(self):
        print("*** View Cart ***")
        print("Name\tPrice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"Total price: {self.cart.total_price}")


class Order:
    def __init__(self):
        self.items = {}
    
    def add_item(self, item):
        if item in self.items:
            self.items[item] += item.quantity
        else:
            self.items[item] = item.quantity
    
    def remove(self, item):
        if item in self.items:
            del self.items[item]

    @property
    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items())
    
    def clear(self):
        self.items = {}


class Employee(User):
    def __init__(self, name, phone, email, address, salary, age, designation):
        super().__init__(name, phone, email, address)
        self.salary = salary
        self.age = age
        self.designation = designation


class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
    
    def add_employee(self, restaurant, employee):
        restaurant.add_employee(employee)

    def view_employee(self, restaurant):
        restaurant.view_employee()

    def add_new_item(self, restaurant, item):
        restaurant.menu.add_menu_item(item)

    def remove_item(self, restaurant, item_name):
        restaurant.menu.remove_item(item_name)


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = Menu()
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def view_employee(self):
        print("Employee List!!")
        for emp in self.employees:
            print(emp.name, emp.email, emp.phone, emp.address)


class Menu:
    def __init__(self):
        self.items = []

    def add_menu_item(self, item):
        self.items.append(item)

    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None

    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print("Item deleted")
        else:
            print("Item not found!")

    def show_menu(self):
        print("******** Menu *******")
        print("Name\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")


class FoodItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


vhabir_dokan = Restaurant("Vhabir Dokan")

admin = Admin("Omar", "1700", "omar@gmail.com", "Dhaka")
item1 = FoodItem("Pizza", 1200, 10)
item2 = FoodItem("Pizza2", 1200, 30)

admin.add_new_item(vhabir_dokan, item1)
admin.add_new_item(vhabir_dokan, item2)

customer1 = Customer("Rahim", "123456", "rahim@gmail.com", "Dhaka")
customer1.view_menu(vhabir_dokan)

item_name = input("Enter item name: ")
item_quantity = int(input("Enter item quantity: "))

customer1.add_to_cart(vhabir_dokan, item_name, item_quantity)
customer1.view_cart()
