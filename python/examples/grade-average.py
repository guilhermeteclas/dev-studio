notes = []

quantity = int(input("Enter how many grades you want to calculate: "))

while quantity <= 0:
    print("It must be greater than zero")
    quantity = int(input("Enter how many grades you want to calculate: "))

for index in range(quantity):
    note = -1
    while note < 0 or note > 10:
        print(f"Grade {index + 1} must be between 0 and 10")
        note = int(input(f'Enter grade {index + 1}: '))
    
    notes.append(note)

print(f"Average of grades: {sum(notes, 0) / quantity}")