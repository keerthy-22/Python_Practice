name = "Online_Class"
options = """1. Add class link
2. List all class links 
3. Display single class link 
4. Mark class attended
5. Close the application"""
attends = []
cid = 1
while True:
    print(name)
    print(options)
    choice = int(input("Enter your choice ( 1 - 5 ): "))
    match choice:
        case 1:
            print("Adding Class Link: ")
            title = input("Enter title: ")
            link = input("Enter Link: ")
            description = input("Enter Description: ")
            attend = {"id":cid,"title":title,"link":link,"description":description,"is_attended":False}
            cid = cid + 1
            attends.append(attend)
        case 2:
            print("List all class links: ")
            for attend in attends:
                print(f"ID: {attend["id"]}")
                print(f"Title: {attend["title"]}")
                print(f"Link: {attend["link"]}")
                print()
        case 3:
            c_id = int(input("Enter the ID of class link: "))
            target_class = {}
            for attend in attends:
                if attend["id"] == c_id:
                    target_class = attend
                    break
            if target_class == {}:
                print("Class not found")
            else:
                print("Class Details: ")
                print(f"ID: {target_class["id"]}")
                print(f"Title: {target_class["title"]}")
                print(f"Link: {target_class["link"]}")
                print(f"Description: {target_class["description"]}")
                print(f"is_attended: {target_class["is_attended"]}")
        case 4:
            print("Mark class attended: ")
            c_id = int(input("Enter the ID of class link: "))
            target_class = {}
            for attend in attends: 
                if attend["id"] == c_id: 
                    target_class = attend 
                    break 
            if target_class == {}: 
                print("Class Not found")
            else:
                attend["is_attended"] = True
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
