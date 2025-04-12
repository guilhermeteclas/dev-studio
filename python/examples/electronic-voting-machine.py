records = []

while True:
    print("Electronic Voting Machine. Select your vote or enter 0 to exit")
    print("1 - Candidate 1")
    print("2 - Candidate 2")
    print("3 - Candidate 3")
    print("4 - Candidate 4")
    print("5 - Null vote")
    print("6 - Blank vote")
    option = int(input("Enter your option: "))

    if option > 0:
        print(option)
        records.append(option)
    elif option == 0 :
        for c in range(6):
            if (c + 1) < 5:
                print(f"Total for candidate {c+1}: {records.count(c+1) }")
            elif (c+1) == 5:
                print(f"Total null votes: {records.count(5) } {round(records.count(5) / len(records) * 100, 2)}%")
            elif (c+1) == 6:
                print(f"Total blank votes: {records.count(6) } {round(records.count(6) / len(records) * 100, 2)}%")
        break
