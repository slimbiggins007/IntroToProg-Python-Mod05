# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Jett Magnuson,11/12/2025,Created Script
# ------------------------------------------------------------------------------------------ #

import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
-----------------------------------------
'''

FILE_NAME: str = "Enrollments.json"

# Define data varibles
student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
student_data: dict = {}
students: list = []
file = None
menu_choice: str = ""

# When program starts, read file data into list of dictionary rows
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
except FileNotFoundError as e:
    print("Text file must exist before running this script!\n")
    print("-- Technical Error Message --")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if file is not None and not file.closed:
        file.close()

# Present and process the data
while True:

    # Present menu choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":
        try:
            student_first_name = input("Enter the students first name: ")
            if not student_first_name.isalpha():
                raise ValueError("the first name should not contain numbers.")
        except ValueError as e:
            print(e)
            print("-- Technical Error Message --")
            print(e.__doc__)
            print(type(e))
            continue

        try:
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("the last name should not contain numbers.")
        except ValueError as e:
                print(e)
                print("-- Technical Error Message --")
                print(e.__doc__)
                print(type(e))
                continue

        course_name = input("Please enter the name of the course: ")
        student_data = {"FirstName": student_first_name,
                        "LastName": student_last_name,
                        "CourseName": course_name}
        students.append(student_data)
        print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        continue

    # Present current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f'{student["FirstName"]},{student["LastName"]},{student["CourseName"]}')
            print("-"*50)
            continue

    # Save data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
            print("The following data was saved to file!")
            for student in students:
                print(f'{student["FirstName"]},{student["LastName"]},{student["CourseName"]}')
        except Exception as e:
            print("There was a non-specific error\n")
            print("-- Technical Error Message --")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if file is not None and not file.closed:
                file.close()
        continue

    # Stop the loop
    elif menu_choice == "4":
        break
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")