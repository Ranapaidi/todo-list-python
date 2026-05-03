task = []

def show_menu():
    print("\n--- To_Do List Menu ---")
    print("1. Add a task")
    print("2. View tasks")  
    print("3. Mark task as Done")
    print("4. Delete Task")
    print("5. Exit ")

def add_task():
    new_task = input("Enter a new task: ")
    task.append(new_task)
    print("Task added successfully!")
def view_task():
    if not task:
        print("No tasks in the list.")
    else:
        print("\n--- To_Do List ---")
        for idx, t in enumerate(task, start=1):
            print(f"{idx}. {t}")
def mark_task_done():
    view_task()
    if task:
        try:
            task_num = int(input("Enter the task number to mark as done: "))
            if 1 <= task_num <=len(task):
                print(f"Task '{task[task_num - 1]}' marked as done!")
                del task[task_num - 1]
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
def delete_task():
    view_task()
    if task:
        try:
            task_num = int(input("Enter the task number to delete: "))
            if 1 <= task_num <= len(task):
                print(f"Task '{task[task_num - 1]}' deleted!")
                del task[task_num - 1]
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
def main():
    while True:
        show_menu()
        choice = input("Enter your choice(1-5): ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_task()
        elif choice == '3':
            mark_task_done()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting the To_Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()


