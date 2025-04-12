def generate (num):
    for i in range(11):
        print(f"{num} x {i} = {num * i}")

for x in range(10):
    print(f"\nTable of {x+1}\n")
    generate(x+1)