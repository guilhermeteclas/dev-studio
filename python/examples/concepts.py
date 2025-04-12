# Examples of variables
name = "John"  # String
age = 25       # Integer
height = 1.75  # Float
is_student = True  # Boolean

# Displaying values
print(name)
print(age)
print(height)
print(is_student)

# Example of if, else, elif
if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You just became an adult.")
else:
    print("You are an adult.")

# Example of a for loop
for i in range(5):  # range(5) generates numbers from 0 to 4
    print(i)

# Example of a while loop
counter = 0

while counter < 5:
    print(counter)
    counter += 1  # Increment the counter

# Example of a function


def greet(name):
    return f"Hello, {name}!"


# Calling the function
message = greet(name)
print(message)


# Example of a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."


# Creating an object of the Person class
person1 = Person("Carlos", 30)
print(person1.introduce())

# Defining a class


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self, sound):
        return f"{self.name} says {sound}!"

# Function to list animals


def list_animals(animals):
    for animal in animals:
        print(f"{animal.name} is a {animal.species}")


# Creating objects
dog = Animal("Rex", "Dog")
cat = Animal("Mimi", "Cat")

# List of animals
animals = [dog, cat]

# Listing animals
list_animals(animals)

# Calling object methods
print(dog.make_sound("woof woof"))
print(cat.make_sound("meow"))
