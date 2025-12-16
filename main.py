todo_list = []

def add_task():
    task = input("Enter a new task: ")
    todo_list.append(task)
    print("Task added successfully")

def view_task():
    if len(todo_list) == 0:
        print("No tasks are available")
    else:
        print("\nYour tasks are:")
        for i in range(len(todo_list)):
            print(f"{i + 1}. {todo_list[i]}")

def update_task():
    view_task()
    if len(todo_list) == 0:
        return

    task_num = int(input("Enter the task number to update: "))
    if 1 <= task_num <= len(todo_list):
        new_task = input("Enter the new task: ")
        todo_list[task_num - 1] = new_task
        print("Task updated successfully")
    else:
        print("Invalid task number")

def delete_task():
    view_task()
    if len(todo_list) == 0:
        return

    remove_num = int(input("Enter task number to delete: "))
    if 1 <= remove_num <= len(todo_list):
        removed = todo_list.pop(remove_num - 1)
        print("Task removed successfully:", removed)
    else:
        print("Invalid task number")

def menu():
    while True:
        print("\n--- TO DO LIST MENU ---")
        print("1. Add task")
        print("2. View tasks")
        print("3. Update task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting the To-Do List application")
            break
        else:
            print("Invalid choice. Please try again")

if __name__ == "__main__":
    menu()
