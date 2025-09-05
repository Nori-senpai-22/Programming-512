#You are given the following incomplete or incorrect Python code that is
#intended to manage a simple student gradebook using a dictionary. """

#Users should be able to:
#    View all student grades
#   Search for a specific student's grade
#    Add a new student and their grade
#   Delete a student's record
#   Exit the program


gradeBook = {"Alice": [90,80,67],"Bruce": [34,67,89],"April": [5,89,100]}




def student_grades():
    print("This is thr Students grades:")
    print(gradeBook)    

def search_student():
    search = input("Enter student Name: ")

    if  search in gradeBook:
        print(search , ":", gradeBook[search])
    
   

def add_student():
    
    student_name = input("Enter student name: ")
    student_grades = input("enter Student grades: ")
    gradeBook[student_name] = student_grades
    print(student_name, "and", student_grades, "has been added")

def delete_student():
    name = input("Enter name: ")
    if name in gradeBook:
        del gradeBook[name]
        print(name, "has been deleted from the Grade Book")
    else:
     print("Name not found")


def main():
    while True:
        print("====== \n Welcome to our Grading System \n =====")
        print("1. View all student grades")
        print("2. Search for a specific student's grade")
        print("3. Add a new student and their grade")
        print("4. Delete a student's record")
        print("5.Exit the program ")
        print("")
        choice = input("Enter your choice: ")

        if choice == "1":
            student_grades()
        elif choice == "2":
            search_student()
        elif choice == "3":
            add_student()
        elif choice == "4":
            delete_student()
        else:
            print("Thank you!")
            break


main()






