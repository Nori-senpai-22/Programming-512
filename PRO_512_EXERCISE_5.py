"""e-commerce Product Inheritance"""




# ✅ Base class: Product
# This class represents a general product in the store
class Product():
    def __init__(self, name, price):
        # Set the name of the product
        self.name = name
        # Set the price of the product
        self.price = price


# ✅ Subclass: Electronics
# Inherits from Product and adds warranty as a specific attribute
class Electronics(Product):
    def __init__(self, name, price, warranty):
        # Call the constructor of the parent class to set name and price
        super().__init__(name, price)
        # Set the warranty (in years) for electronics
        self.warranty = warranty

    # Method to display details of an electronic product
    def product_details(self):
        print("----Electronic Products---- ")
        print(f"Name: {self.name}")                  # Display product name
        print(f"Price: R{self.price}")               # Display price in rands
        print(f"Warranty: {self.warranty} years")    # Display warranty
        print()  # Blank line for formatting


# ✅ Subclass: Clothing
# Inherits from Product and adds size as a specific attribute
class Clothing(Product):
    def __init__(self, name, price, size):
        # Call the constructor of the parent class to set name and price
        super().__init__(name, price)
        # Set the clothing size (e.g., UK 12)
        self.size = size

    # Method to display details of a clothing product
    def product_details(self):
        print("-----Clothing Products-----")
        print(f"Name: {self.name}")                  # Display product name
        print(f"Price: R{self.price}")               # Display price
        print(f"Size: UK{self.size} size")           # Display size
        print()  # Blank line for formatting


# ✅ Creating instances (objects) of Electronics
# Each has a name, price, and warranty
electronic1 = Electronics("Samsung TV", 5000, 3)
electronic2 = Electronics("Oppo 1234", 3000, 4)

# ✅ Creating instances of Clothing
# Each has a name, price, and size
clothing1 = Clothing("Apple Bottoms", 500, 12)
clothing2 = Clothing("Slip Dress", 300, 10)

# ✅ Store all product objects in a list
# This list holds different types of products (Electronics and Clothing)
items = [electronic1, electronic2, clothing1, clothing2]

# ✅ Loop through the list and call product_details()
# This demonstrates polymorphism: the same method name does different things
for item in items:
    item.product_details()





"""  OUTPUT
----Electronic Products---- 
Name: Samsung TV
Price: R5000
Warranty: 3 years

----Electronic Products---- 
Name: Oppo 1234
Price: R3000
Warranty: 4 years

-----Clothing Products-----
Name: Apple Bottoms
Price: R500
Size: UK12 size

-----Clothing Products-----
Name: Slip Dress
Price: R300
Size: UK10 size"""

