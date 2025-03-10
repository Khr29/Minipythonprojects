# importing tasks module 
import tasks  
 

def main():
    while True:   # Keep the program running
        print("\n Option to choice : add, remove, show, exit") # Get user input and convert to lowercase
        choice = input("Enter command: ").strip().lower()

        # Adding a task
        if choice == "add":
            task = input("Enter task: ")
            tasks.add_task(task)

        # Removing a task
        elif choice == "remove":
            if not tasks.tasks:
                print("No tasks to remove. ")
            else:
                tasks.show_tasks()
                try:
                    index = int(input("Enter task number to remove: "))-1
                    tasks.delete_task(index)
                except ValueError:
                    print("Please enter a valid number. ")
        
        # Showing the task list
        elif choice == "show":
            tasks.show_tasks()
        
        # Exiting the program
        elif choice == "exit":
            print("Goodbye!")
            break
        
        else:
            print("Invalid command")

# Program entry point
if __name__ == "__main__":
    main()

