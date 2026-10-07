# Personal Mini-Toolkit

print("Welcome to my Personal Mini-Toolkit!")

# This tool calculates two numbers using different operations.

def calculator():
print("\n--- Simple Calculator ---")

```
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation = input("Choose an operation: ")

if operation == "1":
    result = num1 + num2
    print(f"The answer is {result}")
elif operation == "2":
    result = num1 - num2
    print(f"The answer is {result}")
elif operation == "3":
    result = num1 * num2
    print(f"The answer is {result}")
elif operation == "4":
    if num2 != 0:
        result = num1 / num2
        print(f"The answer is {result}")
    else:
        print("Sorry, you cannot divide by zero.")
else:
    print("Sorry, that operation is not available.")
```

# This tool lets the user add, view, and remove tasks.

def todo_list():
tasks = []

```
while True:
    print("\n--- To-Do List ---")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Back to main menu")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print(f"Task '{task}' was added.")

    elif choice == "2":
        if len(tasks) == 0:
            print("Your to-do list is empty.")
        else:
            print("Your tasks:")
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("There are no tasks to remove.")
        else:
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")

            task_number = int(input("Enter the task number to remove: "))

            if 1 <= task_number <= len(tasks):
                removed = tasks.pop(task_number - 1)
                print(f"Task '{removed}' was removed.")
            else:
                print("That task number is not valid.")

    elif choice == "4":
        print("Returning to the main menu.")
        break

    else:
        print("Sorry, that choice is not valid.")
```

# This tool checks whether a number is even or odd.

def number_checker():
print("\n--- Number Checker ---")

```
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")
```

# Main menu loop keeps the program running until the user chooses Quit.

while True:
print("\n=== PERSONAL MINI-TOOLKIT ===")
print("1. Simple Calculator")
print("2. To-Do List")
print("3. Number Checker")
print("4. Quit")

```
choice = input("Enter your choice: ")

if choice == "1":
    calculator()

elif choice == "2":
    todo_list()

elif choice == "3":
    number_checker()

elif choice == "4":
    print("\nThank you for using my Personal Mini-Toolkit!")
    print("Goodbye!")
    break

else:
    print("Sorry, that choice is not on the menu. Please try again.")
```
