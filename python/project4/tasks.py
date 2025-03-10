#List to store tasks
tasks = []

# Function to add a task
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' has been added.")

# Function to delete a task
def delete_task(index):
    if len(tasks) == 0:
        print("No tasks to remove. ")
    elif index < 0 or index >= len(tasks):
        print("invalid task number.")
    else:
        removed = tasks.pop(index)
        print(f"Task '{removed}' has been removed.")
    

# Function to show all tasks    
def show_tasks():
    if tasks:
        print("\nTo-Do-List: ")
        for i , task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("No task found. ")


