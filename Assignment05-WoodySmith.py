# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   Wsmith,7/27/2024,Created Script
#   
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

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # One row of student data.
students: list = []  # A table of student data.
json_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Holds the choice made by the user.

# Populate with test data
students = [{"student_first_name": "Woody", "student_last_name": "Smith", "course_name": "Python 101"}]

try:
    with open(FILE_NAME, 'w') as file:
        json.dump({"students": students}, file)
except IOError as err:
    print(f"An I/O error occurred: {err}")
else:
    print(f"Write to file {FILE_NAME} successful")
finally:
    print(json.dumps({"students": students}, indent=4))  # beautify the JSON data

# When the program starts, read the file data into a list of lists (table)
try:
    with open(FILE_NAME, 'r') as file:
        data = json.load(file)
        students = data.get("students", [])
except FileNotFoundError:
    print(f"The file {FILE_NAME} does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print(f"Read file successful")

# Present and Process the data
while True:
    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        student_first_name = input("Enter the student's first name: ")
        if not student_first_name.isalpha():
            raise ValueError('Student First Name needs to be characters only')
        student_last_name = input("Enter the student's last name: ")
        if not student_last_name.isalpha():
            raise ValueError('Student Last Name needs to be characters only')
        course_name = input("Please enter the name of the course: ")
        if len(course_name) < 5 or course_name.isnumeric():
            raise ValueError('Course name length or value is not correct. Please try again')

        student_data = {'student_first_name': student_first_name,
                        'student_last_name': student_last_name,
                        'course_name': course_name}
        students.append(student_data)
        print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
    elif menu_choice == "2":
        print(json.dumps({"students": students}, indent=4))
    elif menu_choice == "3":
        # Save the data to a JSON file
        try:
            with open(FILE_NAME, "w") as file:
                json.dump({"students": students}, file)
        except IOError as err:
            print(f"An I/O error occurred: {err}")
        else:
            print("The following data was saved to file!")
            for student in students:
                print(
                    f"Student {student['student_first_name']} {student['student_last_name']} "
                    f"is enrolled in {student['course_name']}")
        continue
    elif menu_choice == "4":
        break
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
