numbers = []
sum = 0

for i in range(5):
    numbers.append(input('Enter a number: '))

for number in numbers:
    sum = int(number) + sum

print(f"Sum: {sum}")
print(f"Average: {sum/len(numbers)}")
