#!/bin/bash

## Vars ##
FILE=""
FILE_ICON=$(echo -e "\U1F4C4")
ARROW_ICON=$(echo -e "\u27A1")

## Functions ##
list_tasks() {
  if [ -s "$FILE" ]; then
    echo -e "---- To-Do List ----\n"
    nl "$FILE"
    echo -e "\n--------------------"
  else
    echo "No tasks found."
  fi
}

add_task() {
  if [ ! -f "$FILE" ]; then
    touch "$FILE.txt"
  fi
  
  echo "Enter the task description:"
  read task
  echo "$task" >>"$FILE"
  echo "Task added."
}

remove_task() {
  echo $FILE

  if [ -s "$FILE" ]; then
    list_tasks

    echo -e "\nEnter the line number of the task to remove:"
    read line_number

    if [ "$line_number" -gt 0 ] && [ "$line_number" -le $(wc -l <"$FILE") ]; then
      sed -i "${line_number}d" "$FILE"
      echo "Task removed."
    else
      echo "Invalid line number."
    fi
  else
    echo ""
    echo "Your to-do list is empty."
  fi
}

list_txt_files() {
  local directory="$1"

  if [ -z "$directory" ]; then
    directory="."
  fi

  txt_files=$(find "$directory" -maxdepth 1 -type f -name "*.txt")

  if [ -z "$txt_files" ]; then
    echo "No .txt files found in $directory"
  else
    for file in $txt_files; do
      echo "$FILE_ICON $file"
    done
  fi
}

choose_file(){
  read -p "Enter the file name: " FILE
}

# Main menu
while true; do

  if [ -z "$FILE" ]; then
    list_txt_files $1
    echo -n -e $ARROW_ICON " Choose an file:\n"
    read FILE
    FILE="${FILE}.txt"

    if [ ! -f "$FILE" ]; then
      touch "$FILE"
      #touch "${FILE}.txt"
    fi

    echo $FILE
  else

    echo ""
    echo "----------------------"
    echo "| To-Do List Manager |"
    echo "----------------------"
    echo "| 1. List tasks      |"
    echo "| 2. Add task        |"
    echo "| 3. Remove task     |"
    echo "| 4. Choose file     |"
    echo "| 0. Exit            |"
    echo "|--------------------|"
    echo ""

    echo $FILE_ICON $FILE

    echo -n -e $ARROW_ICON " Choose an option [1-4]:\n"
    read option

    case $option in
    1 | "list")
      list_tasks
      echo ""
      ;;
    2)
      add_task
      ;;
    3)
      remove_task
      ;;
    4)
      choose_file
      ;;
    0)
      echo "Goodbye!"
      exit 0
      ;;
    *)
      echo "Invalid option. Please try again."
      ;;
    esac
  fi
done
