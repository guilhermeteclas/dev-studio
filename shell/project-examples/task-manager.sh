#!/bin/bash

TODO_FILE="tasks.txt"

# Functions
list_tasks() {
  if [ -s "$TODO_FILE" ]; then
    echo "To-Do List:"
    cat "$TODO_FILE"
  else
    echo "Your to-do list is empty."
  fi
}

add_task() {
  echo "Enter the task description:"
  read task
  echo "$task" >>"$TODO_FILE"
  echo "Task added."
}

remove_task() {
  list_tasks
  echo "Enter the line number of the task to remove:"
  read line_number

  if [ "$line_number" -gt 0 ] && [ "$line_number" -le $(wc -l <"$TODO_FILE") ]; then
    sed -i "${line_number}d" "$TODO_FILE"
    echo "Task removed."
  else
    echo "Invalid line number."
  fi
}

# Main menu
while true; do
  echo
  echo "To-Do List Manager"
  echo "1. List tasks"
  echo "2. Add task"
  echo "3. Remove task"
  echo "4. Exit"
  echo -n "Choose an option [1-4]: "
  read option

  case $option in
  1)
    list_tasks
    ;;
  2)
    add_task
    ;;
  3)
    remove_task
    ;;
  4)
    echo "Goodbye!"
    exit 0
    ;;
  *)
    echo "Invalid option. Please try again."
    ;;
  esac
done
