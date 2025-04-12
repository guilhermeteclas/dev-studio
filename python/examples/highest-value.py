elements = [55,48,98,6,23,84,54]

def highest_value (arr):
    highest = 0
    for i in arr:
        if i > highest:
            highest = i
    print(f"Highest value is {highest}")


highest_value(elements)