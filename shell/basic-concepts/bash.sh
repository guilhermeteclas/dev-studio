#!/bin/bash

# Variables
name="Guilherme"
age=34
echo "Hello, $name!"

# Control structures
if [ $age -ge 18 ]; then
    echo "You are an adult."
else
    echo "You are a minor."
fi

for i in {1..5}; do
    echo "Number $i"
done

counter=1
while [ $counter -le 5 ]; do
    echo "Counter $counter"
    counter=$((counter + 1))
done

# Functions
greet() {
    echo -e "Hello, $1!\n"
}
greet "Moraes"

# File manipulation
echo "Hello, World!" > hello.txt
echo ""
echo "View file?"
echo "1 - Yes"
echo "2 - No"
read input

if [ "$input" -eq 1 ]; then
    echo "------"
    cat hello.txt
    echo ""
else
    echo -e "Bye! \n"
fi
