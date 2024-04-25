class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_index):
        try:
            del self.tasks[task_index]
        except IndexError:
            print("Invalid task index!")

    def display_tasks(self):
        if self.tasks:
            print("To-Do List:")
            for i, task in enumerate(self.tasks):
                print(f"{i+1}. {task}")
        else:
            print("Your to-do list is empty!")

def main():
    todo_list = TodoList()

    while True:
        print("\n1. Add Task\n2. Remove Task\n3. Display Tasks\n4. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
            print("Task added successfully!")
        elif choice == '2':
            if todo_list.tasks:
                task_index = int(input("Enter the index of the task to remove: ")) - 1
                todo_list.remove_task(task_index)
                print("Task removed successfully!")
            else:
                print("No tasks to remove!")
        elif choice == '3':
            todo_list.display_tasks()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
