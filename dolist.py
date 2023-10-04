# Define an empty list to store tasks
tasks = []

def display_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added to your to-do list.")

def update_task(index, new_task):
    if 1 <= index <= len(tasks):
        tasks[index - 1] = new_task
        print(f"Task {index} updated to '{new_task}'.")
    else:
        print("Invalid task index. Please enter a valid index.")

def remove_task(index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print(f"Task {index} ('{removed_task}') removed from your to-do list.")
    else:
        print("Invalid task index. Please enter a valid index.")

while True:
    print("\nTo-Do List Menu:")
    print("1. Display tasks")
    print("2. Add a task")
    print("3. Update a task")
    print("4. Remove a task")
    print("5. Quit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        display_tasks()
    elif choice == "2":
        task = input("Enter the task you want to add: ")
        add_task(task)
    elif choice == "3":
        index = int(input("Enter the index of the task you want to update: "))
        new_task = input("Enter the new task description: ")
        update_task(index, new_task)
    elif choice == "4":
        index = int(input("Enter the index of the task you want to remove: "))
        remove_task(index)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")

# Save tasks to a file (optional)
with open("tasks.txt", "w") as file:
    for task in tasks:
        file.write(task + "\n")
