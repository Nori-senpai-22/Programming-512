# Define a class called Book
class Book:
    
    # Constructor method to initialize title, author, and price of the book
    def __init__(self, title, author, price):
        self.title = title      # Public attribute: title of the book
        self.author = author    # Public attribute: author of the book
        self.price = price      # Public attribute: price of the book

    # Accessor (getter) method for title
    def get_title(self):
        return self.title

    # Accessor (getter) method for author
    def get_author(self):
        return self.author

    # Accessor (getter) method for price
    def get_price(self):
        return self.price

    # Mutator (setter) method to update title
    def set_title(self, titl):
        self.title = titl

    # Mutator (setter) method to update author
    def set_author(self, autho):
        self.author = autho

    # Mutator (setter) method to update price
    def set_price(self, pric):
        self.price = pric


# Create a Book object with initial values
book1 = Book("King Slayer", "Audrey Brown", 200)

# Update the author of the book using the mutator method
book1.set_author("Jet Lee")

# Print book details using accessor methods
print("Book Author: ", book1.get_author())   # Outputs: Jet Lee
print("Book Title:  ", book1.get_title())    # Outputs: King Slayer
print("Book Price:  ", book1.get_price())    # Outputs: 200


# Define a subclass Novel that inherits from Book
class Novel(Book):
    
    # Constructor for Novel takes only category as a parameter
    def __init__(self, category):
        # This constructor overrides the Book class constructor,
        # so title, author, and price are NOT initialized here
        self.category = category  # Category of the novel (e.g., Fiction, Romance)


# Create an object of the Novel class with category "Fiction"
novel1 = Novel("Fiction")

# Set inherited attributes using Book's mutator methods
novel1.set_author("April Moon")
novel1.set_title("April Fools")
novel1.set_price(450)

# Print novel details using inherited accessor methods
print(novel1.get_author())    # Outputs: April Moon
print(novel1.category)        # Outputs: Fiction
