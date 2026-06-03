name = "Todo Application: "
options = """1. Add todo 
2. List all todos 
3. Display single todo 
4. Mark todo as completed
5. Close the application"""

todos = [] # storage which stores all of users todos 

tid = 1

def add_todo(tid,title,description,todos):
    todo = {"id":tid ,"title":title,"description":description,"is_completed":False}
    todos.append(todo)

def list_todos(todos):
    print("Listing Todos: ")
    for todo in todos: 
        print(f"ID: {todo["id"]}")
        print(f"Title: {todo["title"]}")
        print()

def get_todo(tid,todos):
    for todo in todos: 
        if todo["id"] == tid:
            return todo 
    return None 

def display_todo(tid,todos):
    todo = get_todo(tid,todos)
    if todo == None: 
        print("Todo not found")
    else: 
        print("Todo Details: ")
        print(f"ID: {todo["id"]}")
        print(f"Title: {todo["title"]}")
        print(f"Description: {todo["description"]}")
        print(f"is_completed: {todo["is_completed"]}")

def mark_todo(tid,todos):
    todo = get_todo(tid,todos)
    if todo == None: 
        print("Todo not found")
    else: 
        todo["is_completed"] = True 
        
while True: # makes the program run forever until user want to close 
    # printing the title of the application
    print(name)
    # printing the available options 
    print(options)
    # ask user to choose the option 
    choice = int(input("Enter your choice ( 1 - 5 ): "))
    # perform action based on option 
    match choice: 
        case 1: 
            print("Adding Todo: ")
            title = input("Enter the Title: ")
            description = input("Enter the Description: ")
            add_todo(tid,title,description,todos)
            tid += 1 
        case 2:
            list_todos(todos)
        case 3:
            t_id = int(input("Enter the ID of the Todo: "))
            display_todo(t_id,todos)
        case 4: 
            print("Marking Todo as Completed: ")
            t_id = int(input("Enter the ID of the Todo: "))
            mark_todo(t_id,todos)
        case 5:
            print("Closing the application....")
            break
        case _: 
            print("Invalid choice! Try again")
    print("-"*15)
    choice = input("Do you want to continue (y/n)?: ")
    if choice == "y":
        continue
    else:
        break 
