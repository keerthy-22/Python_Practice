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
            skin = {"id":sid,"product":product,"time":time,"is_applied":False}
            sid += 1
            skins.append(skin)
        case 2:
            print("Display single product details")
            s_id = int(input("Enter the ID of the product: "))
            target_product = {}
            for skin in skins:
                if skin["id"] == s_id:
                   target_product = skin
                   break
            if target_product == {}:
               print("Product not found")
            else:
                print("Product Details: ")
                print(f"ID: {target_product["id"]}")
                print(f"Product_name: {target_product["product"]}")
                print(f"Application_time: {target_product["time"]}")
                print(f"is_applied: {target_product["is_applied"]}")
        case 3:
            print("Display single product details")
            s_id = int(input("Enter the ID of the product: "))
            target_product = {}
            for skin in skins:
                if skin["id"] == s_id:
                   target_product = skin
                   break
            if target_product == {}:
               print("Product not found")
            else:
                skin["is_applied"] = True
        case 4:
            print("List of the steps which are Done")
            for skin in skins:
                if skin["is_applied"] == True:
                    print(f"ID: {skin["id"]}")
                    print(f"Product_Name: {skin["product"]}")
                    print(f"Time: {skin["time"]}")
                    print()
        case 5:
            print("List of the steps to be Done")
            for skin in skins:
                if skin["is_applied"] == False:
                    print(f"ID: {skin["id"]}")
                    print(f"Product_Name: {skin["product"]}")
                    print(f"Time: {skin["time"]}")
                    print()
                else:
                    print("All done")
        case 6:
            print("Display all the products")
            for skin in skins:
                print(f"ID: {skin["id"]}")
                print(f"Product_name: {skin["product"]}")
                print(f"Application_time: {skin["time"]}")
                print()
        case 7:
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
            
