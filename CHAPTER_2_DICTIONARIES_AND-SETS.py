"""You are given the following incomplete or incorrect Python code 
that is intended to manage a simple phone book using a dictionary. 
Users should be able to:

View the phone book
Search for a contact
Add a new contact
Delete a contact
Exit the program"""

# Original phoneBook dictionary initialized with three entries
phoneBook = {'Chris':'555-444', 'Katie':'555-222', 'Mark': '555-333'}

#Retrieving a value from a Dictionary
def check_info():
 print(phoneBook)  # Prints the full phone book dictionary

def retrieve_info():
# To retrieve a value from a dictionary
#format : dictionary_name[key]
 print(phoneBook['Chris'])  # Example: retrieving a specific entry directly
 user_key = input("Enter what you are looking for: ")  # Ask user for a name
 if user_key in phoneBook:  # Check if name exists in dictionary
   print(phoneBook[user_key])  # Print the corresponding phone number

def search_info():
#2.2.3 USING in AND not IN OPERATORS TO TEST FOR A VALUE IN A DICTIONARY
 search = input("Enter a name:")  # User enters the name to search
 if search  in phoneBook:  # Check if name is in phoneBook
    print(search, ":", phoneBook[search])  # Display the name and number
 else:
    print("Name not found")  # Display message if name isn't found

def adding_info():
#2.2.4 Adding Elements to an Existing Dictionary
# You can add new key-value pairs to a dictionary with an assignment 
#statement in the following general 
# format: dictionary_name[key] = value

#1. Using Direct Assignment (Square Bracket Notation):
 name = input("Enter your key: ")   #This method is suitable for adding a single key-value pair at a time.
 number = input("Enter your value: ")
 phoneBook[name]= number  # user input is added as a key
 print(name,":",number)
 print("New info has been added")  # Confirmation message

def delete_info():
#2.2.5 Deleting Elements
#You can delete an existing key-value pair from a dictionary with the del statement.
#format: del dictionary_name[key]
 print(phoneBook)  # Display the current phone book before deletion
 delete = input("Enter a name you want to delete: ")  # Ask user for the name to delete
 if delete in phoneBook:  # If the name exists
  del phoneBook[delete]  # Delete the entry
  print(delete,"has been deleted")  # Confirmation message
 else:
   print("Name not found")  # If name not found, notify user

#2.2.6 Mixing Data Types in a Dictionary
#The keys in a dictionary must be immutable objects, but their associated values can be any type of
#object. For example, the values can be lists,

def mixing_dictionary():
  gradeBook = {"Alice": [90,80,67],"Bruce": [34,67,89],"April": [5,89,100]}  # Dictionary with list values
  
  search = input("Enter a name:")  # User inputs a name
  if search  in gradeBook:  # If name is found
    print(search, ":", gradeBook[search])  # Display name and list of grades
  else:
    print("Name not found")  # Notify user if name isn't found

#2.2.7 Creating an Empty Dictionary
#you need to create an empty dictionary and then add elements to it as the program
#executes. You can use an empty set of curly braces to create an empty dictionary
def empty_dictionary():
  phoneBook2 = {}  # Create a new, empty dictionary
  name = input("Enter a name:")  # Ask user for a name
  number = input("enter a number: ")  # Ask user for a number
  phoneBook2[name] = number  # Add the entry to the new dictionary
  print(name, "has been added")  # Confirmation message
  print(phoneBook2)  # Display the new dictionary

def main():
 while True:  # Infinite loop to keep menu running
     print("DICTIONARIES ")
     print("1. Checking Dictionary")
     print("2. Search for Info")
     print("3. Add new info")
     print("4. Delete info")
     print("5. Exit")
     print(" ")
     choice = input("Enter your choice: ")  # Ask user to choose an option

     if choice == "1":
       check_info()  # Call function to display phone book
     elif choice == "2":
       search_info()  # Call function to search contact
     elif choice == "3":
       adding_info()  # Call function to add a new contact
     elif choice == "4":
       delete_info()  # Call function to delete a contact
     elif choice == "5":
       mixing_dictionary()  # NOTE: This does NOT exit the program. It calls mixing_dictionary instead. (Possibly incorrect behavior)
     elif choice == "6":
       empty_dictionary()  # Create and display a new dictionary (not linked to main phoneBook)
     else:
       print("Thank you!")  # Display exit message
       break  # Exit the while loop and end the program
       
main()  # Run the main function
