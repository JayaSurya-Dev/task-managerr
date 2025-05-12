# main.py
from task_manager import TaskManager

def print_menu():
    print("\nTask Manager")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def main():
    manager = TaskManager()

    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Title: ")
            desc = input("Description: ")
            due = input("Due date (YYYY-MM-DD): ")
            priority = input("Priority (Low/Medium/High): ")
            manager.add_task(title, desc, due, priority)

        elif choice == "2":
            manager.list_tasks()

        elif choice == "3":
            task_id = int(input("Enter task ID to update: "))
            task = manager.find_task_by_id(task_id)
            if task:
                print("What do you want to update? (title/description/due_date/priority/status)")
                field = input("Field: ")
                new_value = input("New value: ")
                if manager.update_task(task_id, field, new_value):
                    print("Updated.")
                else:
                    print("Failed.")
            else:
                print("Task not found.")

        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            manager.delete_task(task_id)
            print("Deleted.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
