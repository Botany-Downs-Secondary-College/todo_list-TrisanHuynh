import time
import os

def clr():
    os.system('cls')

def menu():
    clr()
    while True:
        try:
            mode = input("""Choose a mode by entering a number:
1: Add a task
2: View task list
3: Exit
Number : """)
            break
        except ValueError:
            print("That is not a valid choice. Please try again.")
    return mode

todo_list = []

def add_tasks():
    while True:
        new_task = input("Enter the task to add or type 'end' to return to the menu: ").capitalize().strip()
        if new_task  == "End":
            break
        else:
            todo_list.append(new_task)
            
def view_list():
    for task in todo_list:
        print("- {}".format(task))
    time.sleep(5)

while True:
    chosen_option = menu()
    
    if chosen_option == "1":
        add_tasks()
    elif chosen_option == "2":
        view_list()
    elif chosen_option == "3":
        print("Thanks for using this tool. Goodbye!")
        time.sleep(2)
        exit()
    else:
        print("That wasn't an option, please try again.")