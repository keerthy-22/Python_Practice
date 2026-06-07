name = "Skin_Care"
options = """1.Add product name & Add application time
2.Display single Product
3.Mark as applied
4.List of the steps which are Done
5.List of the steps to be Done
6.Display all Products
7.Close the application"""
skins = []
sid = 1
def add_name(sid,product,time,skins):
    skin = {"id":sid,"product":product,"time":time,"is_applied":False}
    skins.append(skin)
def get_info(sid,skins):
    for skin in skins:
        if skin["id"] == sid:
           return skin
    return None
def display_product(sid,skins):
    skin = get_info(sid,skins) 
    if skin == None: 
        print("Product Not found")
    else:
        print("Product Details: ")
        print(f"ID: {skin["id"]}")
        print(f"Product: {skin["product"]}")
        print(f"Time: {skin["time"]}")
        print(f"is_applied: {skin["is_applied"]}")
def mark_product(sid,skins):
    skin = get_info(sid,skins)
    if skin == None: 
        print("Product not found")
    else: 
        skin["is_applied"] = True
def list_done(sid,product,skins):
    skin = get_info(sid,skins)
    for skin in skins:
        if skin["is_applied"] == True:
            print(f"ID: {skin["id"]}")
            print(f"Product: {skin["product"]}")
def list_not_done(sid,product,skins):
    skin = get_info(sid,skins)
    for skin in skins:
        if skin["is_applied"] == False:
            print(f"ID: {skin["id"]}")
            print(f"Product: {skin["product"]}")
def list_all(sid,product,time,skins):
    for skin in skins:
            print(f"ID: {skin["id"]}")
            print(f"Product: {skin["product"]}")
            print(f"Time: {skin["time"]}")
            print()
while True:
    print(name)
    print(options)
    choice = int(input("Enter your choice (1-7): "))
    match choice:
        case 1:
            print("Adding the product name")
            product = input("Enter the product name: ")
            print("Adding the application time")
            time = input("Please enter a time in HH:MM format (e.g., 14:30): ")
            add_name(sid,product,time,skins)
            sid += 1
        case 2:
            print("Display single product details")
            s_id = int(input("Enter the ID of the product: "))
            display_product(s_id,skins)
        case 3:
            print("Mark as applied")
            s_id = int(input("Enter the ID of the product: "))
            mark_product(s_id,skins)
        case 4:
            print("List of the steps which are Done")
            list_done(sid,product,skins)
        case 5:
            print("List of the steps to be Done")
            list_not_done(sid,product,skins)
        case 6:
            print("List all the products")
            list_all(sid,product,time,skins)
        case 7:
            print("Close the application....")
            break
        case _: 
            print("Invalid choice! Try again")
    print("-"*15)
    choice = input("Do you want to continue (y/n)?: ")
    if choice == "y":
        continue
    else:
        break 
            
