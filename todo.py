tasks = []

def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    print("Task added!")

def view_tasks():
    print("\nYour Tasks:")
    for i, task in enumerate(tasks):
        status = "✅" if task["done"] else "❌"
        print(f"{i+1}. {task['task']} [{status}]")

def mark_done():
    view_tasks()
    index = int(input("Enter task number to mark done: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        print("Task marked as done!")
    else:
        print("Invalid number.")

def delete_task():
    view_tasks()
    index = int(input("Enter task number to delete: ")) - 1
    if 0 <= index < len(tasks):
        tasks.pop(index)
        print("Task deleted.")
    else:
        print("Invalid number.")

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
