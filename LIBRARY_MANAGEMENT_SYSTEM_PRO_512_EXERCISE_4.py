# 🔷 Base class representing any library item
class LibraryItem:
    # Constructor method to initialize common attributes
    def __init__(self, title, year):
        self.title = title  # Store the title of the item
        self.year = year    # Store the year of publication/release
      
# 🔶 Subclass representing a Book, which inherits from LibraryItem
class Book(LibraryItem):
    # Constructor with an additional attribute 'author'
    def __init__(self, title, year, author):
        super().__init__(title, year)  # Call the constructor of the parent class
        self.author = author           # Store the name of the book's author
    
    # Method to display book information
    def get_info(self):
        print("Book Information")
        print(f"Title: {self.title}")    # Print the title
        print(f"Author: {self.author}")  # Print the author
        print(f"Year: {self.year}")      # Print the year of publication
        print()  # Blank line for better readability in output
# 🔶 Subclass representing a DVD, which also inherits from LibraryItem
class DVD(LibraryItem):
    # Constructor with an additional attribute 'duration'
    def __init__(self, title, year, duration):
        super().__init__(title, year)    # Call the constructor of the parent class
        self.duration = duration         # Store the duration of the DVD (in minutes)

    # Method to display DVD information
    def get_info(self):
        print("DVD Information")
        print(f"Title: {self.title}")      # Print the title
        print(f"Year: {self.year}")        # Print the year of release
        print(f"Duration: {self.duration}")  # Print duration in minutes
# ✅ Creating an object (instance) of the Book class
# "Apple Pie" is the title, 2018 is the year, and "Katy Price" is the author
book1 = Book("Apple Pie", 2018, "Katy Price")
book1.get_info()  # Call method to display the book's info
# ✅ Creating an object of the DVD class
# "Bleach" is the title, 2013 is the year, 160 is the duration in minutes
DVD1 = DVD("Bleach", 2013, 160)
DVD1.get_info()  # Call method to display the DVD's info
 #OUTPUT



Book Information
Title: Apple Pie 
Author: 2018
Year: Katy Price

DVD Information
Title: Bleach
Year: 2013
Duration: 160
