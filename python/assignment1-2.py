class OnlineShop:
    def __init__(self, name,URL):
        self.name = name
        self.URL = URL
        self.Product = []

    def addingItemsToCart(self, product):
        self.Product.append(product)

    def checkOut(self, order):
        self.Product = self.Product - order

    def orderTracking(self):
        print("Your Count Product:" + str(self.Product))

    def show1(self):
        print(self.Product[0].description)
        print(self.Product[0].price)
        print(self.Product[0].Onlineshop)

class Product:
    def __init__(self, description, price, OnlineShop):
        self.description = description
        self.price = price
        self.Onlineshop = OnlineShop

class Customer:
    def __init__(self, name, email, address, PastOrders):
         self.name = name
         self.email = email
         self.address = address
         self.PastOrders = PastOrders

    def show2(self):
        print(self.name)
        print(self.email)
        print(self.address)
        print(self.PastOrders)

print("CUSTOMER LIST")
customer01 = Customer("Naruekawin", "tonkla@gmail.com", "Nonthaburi", 7)
customer01.show2()

print("PRODUCT LIST")
shopping01 = OnlineShop("Apple Studio", "https:")
product01 = Product("Iphone 15", 30000, "Apple Studio")

shopping01.addingItemsToCart(product01)
shopping01.show1()