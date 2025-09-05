#====================

#INTRODUCTION TO SETS

#====================

#2.3.1 A set is an object that stores a collection of data in the same way as mathematical sets
                #All the elements in a set must be unique
                #Sets are unorderd
                #The elements that are stored in a set can be of different data types.

#2.3.2 CREATING A SET 
    #To create a set you must call the built in function
def empty_set():
    myset = set()
    
    while True:
        number = input("Please enter a number: ")
        
        print(number, "has been added to the set")
        myset.add(number)
        print(myset)
    






#2.3.3 GETTING THE NUMBER OF ELEMENTS IN A SET
        #As with lists, tuples, and dictionaries you can use th "len" function to get 
        #the number of elements in a set
def mySet():
    myset = set([1,2,3,4,5,6,7,8,9,10,11,23,56,89,453])
    print(len(myset))

#2.3.4 ADDING AND REMOVING
        #Sets are mutable objects so you can add items to them and remove from them
        #You use the "add" method to ad an element to a set 
        
def adding_method():
    myset= set([1,4,6,7,8,9,2,4,67,334,99,556])
    print("This is the set:", myset)
    number = int(input("Enter a number you want to add:"))
    myset.add(number)

#You can remove an item from a set with either the removemethod or the discard method. 
def remove_method():
    myset = set([11,34,67,45,89,56,90,34])
    print(myset)
    number = input("Enter a number you want to remove: ")
    myset.remove(number)
    print("Number being removed: ", number)
    print("Updated set: ",myset)



#You can add a group of elements to a set all at one time with the update method.
def adding_group():
    myset=set([1,2,3,4,5,6])
    print("Original Set: ")
    print(myset)
    myset.update([6,7,8,9,5,4])
    print("Updated set:")
    print(myset)





#2.3.5 Using the for loop to iterate over a Set
        #You can use the for loop in the following 
        # general format to iterate over all the elements in a set:

def loop_set():
    myset =set([2,3,45,67,89,23,45,89])
    for value in myset:         #value is the name of a variable
        print(value)               #Thisloop iterates once for each element in the set.

        
#2.3.6 Using the in and not in Operators to Test for a Value in a Set
        #You can use the in operator to determine whether a value exists in a set.
def search_set():
    myset = set([1,2,4,5,6,7,8,5,3,4,7,9])
    if 1 in myset:
        print("the value of 1 is in thr list")
    else:
        print("Number not found")
    if 99 not in myset:
        print("99 is not in the set")

def main():
    while True:
        print("WELCOME TO INTRODUCTION OF SETS \n")
        print("1. Creating a Set ")
        print("2. Getting the number of elements in a set")
        print("3. Adding  elments to a set")
        print("4. Removing elements from a set")
        print("5. Adding group of elements to a set")
        print("6. Using the for loop to iterate over a Set")
        print("7. Using the in and not in Operators to Test for a Value in a Set ")
        print("8. Finding the Union of Sets")
        print("9. Finding the intersection of Sets")
        print("10 Finding the Difference of Sets")
        print("11.Finding the Symmetric Difference of Sets")
        print("12.Finding Subsets and Supersets")

    
        choice = input("Enter your Choice:  ")
        if  choice == "1":
         empty_set()
        elif choice =="2":
         mySet()
        elif choice == "3":
         adding_method()
        elif choice == "4":
         remove_method()
        elif choice == "5":
         adding_group()
        elif choice == "6":
         loop_set()
        elif choice == "7":
         search_set()


main()
