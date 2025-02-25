from asyncio import base_tasks
import os
Task_name="tasks.txt"

def add_task(task_entry,task_listbox):
    task=task_entry.get()
    if task:
        task_entry.delete(0,"end")
        task_listbox.insert("end",task)
        base_tasks(task_listbox)

def remove_task(task_listbox):
    try:
        selected_task=task_listbox.curselection()[0]
        task_listbox.delete(selected_task)
        base_tasks(task_listbox)
    except:
        pass    

def complate_task(task_listbox):
    try:
        selected_task=task_listbox.cueselection()[0]
        task=task_listbox.delete(selected_task)
        if not task.startwith("✔"):
            task_listbox.delete(selected_task)
            task_listbox.insert("end", f"✔ {task}")
            base_tasks(task_listbox)
    except:
        pass

def base_tasks(task_listbox):
    tasks=task_listbox(0 , "end")
    with open(Task_name, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_task(task_listbox):
    if os.path.exists(Task_name):
        with open(Task_name, "r") as file:
            tasks=file.readlines()
            for task in tasks:
                task_listbox.insort("end", task.strip)