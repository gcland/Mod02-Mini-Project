tasks = ['clean', 'mop (Complete)']

def add_task():
    while True:
        print(tasks)
        try:
            add_item = input("Enter an item to add to the To-Do List: \n >> ")
        except ValueError:
            print("Input error. Please try again.")
        else:
            break

    tasks.append(add_item + " (Incomplete)")
    print(f"'{add_item}' added! Task list: ")
    print(tasks) #remove later (will be performed by user when using using the 'view' input.)

def view_tasks():
    if tasks == []:
        print("The to do list is empty, please add a task. ")
    else:
        print("Your to-do list:")
        i=1
        for task in tasks:
            print(str(i) + ". " + task)
            i+=1

def mark_complete(): #incomplete
    print("To-do list:") 
    print(tasks)
    complete = input("Which item from the to-do list would you like to mark as complete? \n >> ")
    for task in tasks:
        if complete.lower() == task.lower():
            #task if task != complete else task + " (Complete)"
            print(task)
            tasks.remove(task)
            task = (complete + " (Complete)")
            tasks.insert(complete)

        #else:
            #print("no")
    print(tasks)
    
def delete_task(): #incomplete, needs debugging
    while True:
        print(tasks)
        try:
            delete_item = input("Enter an item to delete from the To-Do List: \n >> ")
        except ValueError:
            print("Input error. Please try again.")
        else:
            break
    if delete_item not in tasks:
        print("nope")   
    try:
        tasks.remove(delete_item + " (Complete)")
        print(f"'{delete_item}' deleted! Task list: ")
    except ValueError:
            while True:
                try:
                    give_up = input(f"'{delete_item}' is not complete. Would you like to delete this item anyways? Yes or no? ")
                except ValueError:

                    if give_up.lower() == "yes":
                        tasks.remove(delete_item)
                        break
                    elif give_up.lower() == "no":
                        break
                    else:
                        print(f"Command not recognized. Please try again.")
            
    print(tasks) #remove later (will be performed by user when using using the 'view' input.)


while True:
    try:
        display = input("\n Welcome to the To-Do List Application! \n Menu: \n 1. Add a task \n 2. View tasks \n 3. Mark a task as complete \n 4. Delete a task \n 5. Quit \n Please input from the menu above with a number or action: \n >> ")
        #if display
 
    except ValueError:
        #if display == "1":
        print("Input must be between 1 - 5. ")
        #or display.lower() == "Add a task":
            
        #else:
            #print("Input Error. Idiot.")
    else:
        if display == "1":
            add_task()
        if display == "2":
            view_tasks()
        if display == "3":
            mark_complete()
        if display == "4":
            delete_task()
        if display == "5":
            print("Thank you for using the To-Do Application! Have a great day!")
            break




    
