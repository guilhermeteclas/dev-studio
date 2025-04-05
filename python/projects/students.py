import json
import os

# File to store student data
DATA_FILE = "./python/projects/students.json"

# Function to load student data from the JSON file
def load_students():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

# Function to save student data to the JSON file
def save_students(students):
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)

# Function to register a new student
def register_student(students):
    print("\n--- Register a New Student ---")
    name = input("Enter the student's name: ")
    age = input("Enter the student's age: ")
    registration_id = input("Enter the student's registration ID: ")

    # Create a dictionary for the new student
    student = {
        "name": name,
        "age": age,
        "registration_id": registration_id
    }

    # Add the student to the list
    students.append(student)
    print(f"\nStudent {name} registered successfully!")

# Function to list all registered students
def list_students(students):
    if not students:
        print("\nNo students registered yet.")
    else:
        print("\n--- List of Registered Students ---")
        for student in students:
            print(f"Name: {student['name']}, Age: {student['age']}, Registration ID: {student['registration_id']}")

# Main function to run the app
def main():
    # Load existing student data
    students = load_students()

    while True:
        print("\n--- School Student Registration ---")
        print("1. Register a new student")
        print("2. List all students")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            register_student(students)
        elif choice == "2":
            list_students(students)
        elif choice == "3":
            # Save students to JSON file before exiting
            save_students(students)
            print("\nData saved. Exiting the application. Goodbye!")
            break
        else:
            print("\nInvalid option. Please try again.")

# Run the app
if __name__ == "__main__":
    main()