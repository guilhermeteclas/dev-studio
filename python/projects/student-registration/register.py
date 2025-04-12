import json
import os

# Constants for menu options
REGISTER_STUDENT = "1"
LIST_STUDENTS = "2"
EXIT = "3"

# File to store student data (absolute path)
DATA_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "students.json"))

# Function to load student data from the JSON file
def load_students():
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as file:
                return json.load(file)
    except json.JSONDecodeError:
        print("Error decoding JSON file. Returning an empty list.")
        return []
    return []

# Function to save student data to the JSON file
def save_students(students):
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)

# Function to register a new student
def register_student(students):
    print("\n--- Register a New Student ---")
    name = input("Enter the student's name: ")

    while True:
        age_str = input("Enter the student's age: ")
        if age_str.isdigit():
            age = int(age_str)
            if age > 0:  # Basic age validation
                break
            else:
                print("Age must be a positive number.")
        else:
            print("Invalid age. Please enter a number.")

    registration_id = input("Enter the student's registration ID: ")

    student = {
        "name": name,
        "age": age,
        "registration_id": registration_id
    }

    students.append(student)
    print(f"\nStudent {name} registered successfully!")

# Function to list all registered students
def list_students(students):
    if not students:
        print("\nNo students registered yet.")
    else:
        print("\n--- List of Registered Students ---")
        for student in students:
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Registration ID: {student['registration_id']}\n")

# Main function to run the app
def main():
    students = load_students()

    while True:
        print("\n--- School Student Registration ---")
        print(f"{REGISTER_STUDENT}. Register a new student")
        print(f"{LIST_STUDENTS}. List all students")
        print(f"{EXIT}. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == REGISTER_STUDENT:
            register_student(students)
        elif choice == LIST_STUDENTS:
            list_students(students)
        elif choice == EXIT:
            save_students(students)
            print("\nData saved. Exiting the application. Goodbye!")
            break
        else:
            print("\nInvalid option. Please try again.")

# Run the app
if __name__ == "__main__":
    main()