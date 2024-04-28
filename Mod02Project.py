tasks = []

def view_tasks():
    if tasks == []:
        print("The to do list is empty, please add a task. ")
    else:
        print("Your to-do list:")
        i=1
        for task in tasks:
            print(str(i) + ". " + task)
            i+=1

def add_task():
    while True:
        print(tasks)
        try:
            add_item = input("Enter an item to add to the To-Do List: \n >> ")
        except ValueError:
            print("Input error. Please try again.")
        if add_item.lower() + " (Incomplete)" in tasks:
                print(f"{add_item} is already in the to-do list!")
        else:
                tasks.append(add_item + " (Incomplete)")
                print(f"'{add_item}' added! Task list: ")
        view_tasks()
        while True:
            again = input("Would you like to add more items to the to-do list? Yes or no? ")
            if again.lower() == "no":
                break
            elif again.lower() == "yes":
                break
            else:
                print(f"{again.upper()} not recognized. Please try again.")
        if again.lower() == "no":
            break

def mark_complete(): #fix function to congratulate user on completing all tasks
    y = tasks.count(" (Complete)")
    view_tasks()
    while True:
        if tasks == []:
            break
        i = 0
        view_tasks()
        n = input("Which item from the to-do list would you like to mark as complete? \n >> ")
        inc = n + " (Incomplete)"
        com = n + " (Complete)"
        if com in tasks:
            print(f"{n} is already complete!")
        elif inc not in tasks:
            print(f"{n} is not in the to-do list.")
        for task in tasks:
            i+=1
            if inc == task:
                print(com)
                tasks.pop(i-1)
                tasks.insert(i-1, com)
                y+=1
                break
        z = len(tasks)
        if y == z:
            print("\nYour task list is fully completed! Congratulations!")
            view_tasks()
            break
        while True:
            again = input("Would you like to mark more items complete on the to-do list? Yes or no? ")
            if again.lower() == "no":
                break
            elif again.lower() == "yes":
                break
            else:
                print(f"{again.upper()} not recognized. Please try again.")
        if again.lower() == "no":
            break
        
def delete_task(): 
    while True:
        view_tasks()
        if tasks == []:
            break
        delete_item = input("Enter an item to delete from the To-Do List: \n >> ")
        del_comp = delete_item + " (Complete)"
        del_incomp = delete_item + " (Incomplete)"

        if del_comp in tasks:
            tasks.remove(del_comp)
            print(f"'{delete_item}' deleted!")
        elif del_incomp not in tasks: 
            print(f"{delete_item} is not in the to-do list!")  
        elif del_incomp in tasks:
            while True:
                quitter = input(f"{delete_item} is not complete. Are you sure you want to delete this? Yes or no? ")
                if quitter.lower() == "no":
                    break
                elif quitter.lower() == "yes":
                    tasks.remove(del_incomp)
                    print(f"'{delete_item}' deleted!")
                    break
                else:
                    print(f"{quitter.upper()} not recognized. Please try again.")
        while True:
            again = input("Would you like to delete more items on the to-do list? Yes or no? ")
            if again.lower() == "no":
                break
            elif again.lower() == "yes":
                break
            else:
                print(f"{again.upper()} not recognized. Please try again.")
        if again.lower() == "no":
            break    

while True:
    try:
        display = input("\n Welcome to the To-Do List Application! \n Menu: \n 1. Add a task \n 2. View tasks \n 3. Mark a task complete \n 4. Delete a task \n 5. Quit \n Please input from the menu above with a number or action: \n >> ")
    
    except ValueError:
        print("Input not recognized. Please try again.")
   

    if display == "1" or display.lower() == "add" or display.lower() == "add a task":
        add_task()
    elif display == "2" or display.lower() == "view" or display.lower() == "view a task":
        view_tasks()
    elif display == "3" or display.lower() == "complete" or display.lower() == "mark complete" or display.lower() == "mark a task complete":
        mark_complete()
    elif display == "4" or display.lower() == "delete" or display.lower() == "delete a task":
        delete_task()
    elif display == "5" or display.lower() == "quit":
        print("Thank you for using the To-Do Application! Have a great day!")
        if tasks == []:
            break
        else:
            view_tasks()
            break
    else:
        print("Input not recognized. Please try again.")


    
