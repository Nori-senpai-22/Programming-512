# ================================
# CHAPTER 1: LISTS AND TUPLES
# ================================

# --------------------------------
# 1.1 LISTS
# --------------------------------
# A list is a collection of ordered items. Lists are mutable (can change).
fruits = ["apple", "banana", "cherry"]
print(fruits[0])   # apple

# Iterating
for f in fruits:
    print(f)

# Indexing
print(fruits[-1])  # cherry

# Updating values
fruits[1] = "orange"
print(fruits)  # ['apple', 'orange', 'cherry']

# Concatenation
a = [1, 2]
b = [3, 4]
print(a + b)  # [1, 2, 3, 4]

# Slicing
days = ["Mon", "Tue", "Wed", "Thu"]
print(days[1:3])  # ['Tue', 'Wed']

# "in" operator
print("apple" in fruits)  # True

# List methods
nums = [3, 1, 2]
nums.append(4)
nums.sort()
print(nums)  # [1, 2, 3, 4]

# Two-dimensional lists
matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix[1][0])  # 3


# --------------------------------
# 1.2 TUPLES
# --------------------------------
# Tuples are like lists but immutable (cannot be changed).
coordinates = (10, 20)
print(coordinates[0])  # 10

# Packing and unpacking
point = (4, 5)
x, y = point
print(x, y)  # 4 5


# ================================
# CHAPTER 2: DICTIONARIES AND SETS
# ================================

# --------------------------------
# 2.1 DICTIONARIES
# --------------------------------
# A dictionary stores data in key-value pairs.
student = {"name": "Alice", "age": 20, "marks": [85, 90, 95]}
print(student["name"])  # Alice
print(student.get("age"))  # 20

# Adding and updating
student["grade"] = "A"
student["age"] = 21
print(student)

# Removing
del student["marks"]
print(student)

# Methods
print(student.keys())
print(student.values())
print(student.items())

# Looping
for key, value in student.items():
    print(key, ":", value)

# Nested dictionary
school = {
    "101": {"name": "Sam", "marks": [75, 80, 85]},
    "102": {"name": "Lara", "marks": [90, 95, 92]}
}
print(school["101"]["name"])  # Sam


# --------------------------------
# 2.2 SETS
# --------------------------------
# Sets store unique, unordered items.
nums = {1, 2, 3, 3, 4}
print(nums)  # {1, 2, 3, 4}

# Creating from a string
letters = set("banana")
print(letters)  # {'a', 'n', 'b'}

# Adding and removing
s = {1, 2}
s.add(3)
s.remove(2)
s.discard(5)  # no error if not found
print(s)

# Operations
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # Union
print(a & b)  # Intersection
print(a - b)  # Difference
print(a ^ b)  # Symmetric difference

# Subset and superset
x = {1, 2}
y = {1, 2, 3}
print(x.issubset(y))    # True
print(y.issuperset(x))  # True

# Membership
fruits = {"apple", "banana", "cherry"}
print("apple" in fruits)  # True


# ================================
# CHAPTER 3: OBJECT-ORIENTED PROGRAMMING
# ================================

# --------------------------------
# 3.1 OOP vs Procedural
# --------------------------------
# Procedural programming = functions act on data directly.
# OOP = data + functions are grouped inside objects (classes).

# --------------------------------
# 3.2 CLASSES AND OBJECTS
# --------------------------------
class Student:
    def __init__(self, name, age):
        self.name = name      # attribute
        self.age = age

    def greet(self):          # method
        return f"Hello, my name is {self.name}."


s1 = Student("Alice", 21)
print(s1.greet())  # Hello, my name is Alice.

# --------------------------------
# 3.3 HIDING ATTRIBUTES
# --------------------------------
# Private attributes start with "__" (double underscore).
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


acc = Account("Bob", 1000)
acc.deposit(500)
print(acc.get_balance())  # 1500

# --------------------------------
# 3.4 INHERITANCE
# --------------------------------
# A class can inherit attributes and methods from another class.
class Person:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"My name is {self.name}."


class Teacher(Person):    # inherits from Person
    def teach(self):
        return "I am teaching a class."


t1 = Teacher("Mr. Smith")
print(t1.speak())   # My name is Mr. Smith.
print(t1.teach())   # I am teaching a class.

# --------------------------------
# 3.5 POLYMORPHISM
# --------------------------------
# Different classes can have methods with the same name but different behaviors.
class Dog:
    def sound(self):
        return "Woof!"


class Cat:
    def sound(self):
        return "Meow!"


animals = [Dog(), Cat()]
for a in animals:
    print(a.sound())  # Woof! Meow!


# ================================
# FINAL INTEGRATED EXAMPLE
# ================================

# This example uses:
# - List
# - Tuple
# - Dictionary
# - Set
# - OOP (Class)

# List of students
students = ["Alice", "Bob", "Charlie"]

# Tuple of courses (immutable)
courses = ("Math", "Science", "History")

# Dictionary storing student marks
marks = {
    "Alice": [90, 85, 88],
    "Bob": [70, 75, 80],
    "Charlie": [95, 92, 96]
}

# Set of all unique marks
all_marks = set(marks["Alice"] + marks["Bob"] + marks["Charlie"])
print("Unique marks:", all_marks)

# OOP: Create a class for Student
class StudentRecord:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def average(self):
        return sum(self.scores) / len(self.scores)


# Create objects
alice = StudentRecord("Alice", marks["Alice"])
bob = StudentRecord("Bob", marks["Bob"])

print(alice.name, "Average:", alice.average())
print(bob.name, "Average:", bob.average())






# ================================
# ACTIVITIES: CHAPTER 1, 2, AND 3
# ================================

# ----------------
# EASY LEVEL
# ----------------

# 1. Create a list of 5 fruits. Print the second fruit.
# 2. Create a tuple of 3 city names. Unpack them into 3 variables and print each one.
# 3. Given the list numbers = [1, 2, 3, 4, 5],
#    replace the third element with 99 and print the new list.
# 4. Check if "banana" exists in the list fruits = ["apple", "banana", "cherry"].
# 5. Create a set of numbers {1, 2, 2, 3, 4}. Print the set and explain why duplicates are removed.

# ----------------
# MEDIUM LEVEL
# ----------------

# 6. Create a dictionary called "student" with keys: "name", "age", and "marks".
#    Print only the values of the dictionary.
# 7. Given colors = ["red", "blue", "green", "yellow"],
#    print the last two colors using slicing.
# 8. Write a loop that prints each key and value from the dictionary:
#    car = {"brand": "Toyota", "year": 2020, "color": "white"}
# 9. Create two sets: a = {1, 2, 3}, b = {3, 4, 5}.
#    Print their union, intersection, and difference.
# 10. Create a 2D list for exam scores of 3 students (2 subjects each).
#     Print the second subject score of the first student.

# ----------------
# ADVANCED LEVEL
# ----------------

# 11. Write a class "Book" with attributes "title" and "author".
#     Create an object and print a message like: "The book <title> was written by <author>".
# 12. Extend the class "Book" by creating a subclass "EBook" with an extra attribute "filesize".
#     Create an object and print its details.
# 13. Create a dictionary where the key is a student's name and the value is a list of their marks.
#     Write code to calculate and print each student’s average.
# 14. Write a program that takes two lists:
#     list1 = [1, 2, 3, 4], list2 = [3, 4, 5, 6].
#     Print numbers that are in one list but not both (symmetric difference).
# 15. Write a class "BankAccount" with private attribute "__balance".
#     Add methods to deposit, withdraw, and check balance.
#     Create an object and test all methods.
# 16. Create two classes "Dog" and "Cat" with a method "sound()".
#     Make a list containing both objects and use a loop to call sound() for each (demonstrating polymorphism).
# 17. Create a program that:
#     - Stores a list of students (list)
#     - Stores the subjects offered (tuple)
#     - Stores marks of students (dictionary)
#     - Finds all unique marks (set)
#     - Uses a class "Student" with a method to calculate average marks.
#     Test the class with at least 2 students.

