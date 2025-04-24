lst=[]
def view_todo_list():
    if len(lst)!=0:
        for i in range(len(lst)):
            print(i+1,":",lst[i])
    else:
        print("No task has been provided")

def add_task(task):
    lst.append(task)
    print("Your task has been added")

def mark_task_done(done_task):
    for i in range(len(lst)):
        if 1 <= done_task <= len(lst):
            s=lst.pop(done_task-1)
            print("Your task","(",s,")","has been marked as done")
            break
        else:
            print("Index not matched !!!")

def updated_task(update_task):
    lst[update_task-1]=change_task
    print("Your selected task has been updated as",change_task)

while True:
    print("**** TO-DO LIST ****")
    print("1. View To-Do list")
    print("2. Add Task")
    print("3. Mark Task as done")
    print("4. Update Task")
    print("5. Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        view_todo_list()
    elif choice==2:
        task=input("Enter your task:")
        add_task(task)
    elif choice==3:
        done_task=int(input("Enter the index of task which you want to mark as done:"))
        mark_task_done(done_task)
    elif choice==4:
        update_task=int(input("Enter the index of task which you want to update:"))
        change_task=input("Enter updated task:")
        updated_task(update_task)
    elif choice==5:
        print("!!! Thank you for using this To-Do application !!!")
        break
    else:
        print("Please select choice between 1 and 4 !!!")

