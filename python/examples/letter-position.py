phrase = input("Type a sentence:")

count = phrase.count('a')

print(f"Number of letters A: {count}")

first = phrase.find('a')
last = phrase.rfind('a')
print(f"First occurrence: {first}")
print(f"Last occurrence: {last}")