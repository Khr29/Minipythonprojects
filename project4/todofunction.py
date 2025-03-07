tasks = []

def add_task(task):
    tasks.oppend(task)
    print(f"Task" "{task}" "have been added.")

def delete_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Task" "{removed}" "have been removed")
    else:
        print("invalid task number.")

    
def show_task():
    if tasks:
        print("To Do List: ")
        for i , task in enumerate(tasks):
            print(f"{i+1}. {task}")
    else:
        print("No task found. ")


