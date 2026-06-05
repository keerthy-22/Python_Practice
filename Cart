name = "Shopping_List"
options = """1.Add item to cart & Add price of the item
2.Add item price
3.Display single item details
4.Mark as  purchased
5.list all items in cart
6 .list items purchased
7.list item to be purchase
8.Close the application"""
carts = []
iid = 1
while True:
    print(name)
    print(options)
    choice = int(input("Enter your choice (1-8): "))
    match choice:
        case 1:
            print("Add item to cart")
            item = input("Enter the item name: ")
            cart = {"id":iid,"item":item,"price":None,"is_purchased":False}
            carts.append(cart)
            iid = iid + 1
        case 2:
            print("Mark item as purchased")
            i_id = int(input("Enter the ID of the item: "))
            price = int(input("Enter the item price: "))
            target_item = {}
            for cart in carts:
                if cart["id"] == i_id:
                   target_item = cart
                   break
            if target_item == {}:
               print("Item not found")
            else:
                cart["price"] = price
            
        case 3:
            print("Display single item details")
            i_id = int(input("Enter the ID of the item: "))
            target_item = {}
            for cart in carts:
                if cart["id"] == i_id:
                   target_item = cart
                   break
            if target_item == {}:
               print("Item not found")
            else:
                print("Item Details: ")
                print(f"ID: {target_item["id"]}")
                print(f"Title: {target_item["item"]}")
                print(f"Description: {target_item["price"]}")
                print(f"is_purchased: {target_item["is_purchased"]}")
        case 4:
            print("Mark item as purchased")
            i_id = int(input("Enter the ID of the item: "))
            target_item = {}
            for cart in carts:
                if cart["id"] == i_id:
                   target_item = cart
                   break
            if target_item == {}:
               print("Item not found")
            else:
                cart["is_purchased"] = True
        case 5:
            print("List all the items in the cart")
            for cart in carts:
                print(f"ID: {cart["id"]}")
                print(f"Item_Name: {cart["item"]}")
                print(f"Price: {cart["price"]}")
                print()
        case 6:
            print("List Item purchased")
            for cart in carts:
                if cart["is_purchased"] == True:
                    print(f"ID: {cart["id"]}")
                    print(f"Item_Name: {cart["item"]}")
                    print(f"Price: {cart["price"]}")
                    print()
        case 7:
            print("List Items to be purchased")
            for cart in carts:
                if cart["is_purchased"] == False:
                    print(f"ID: {cart["id"]}")
                    print(f"Item_Name: {cart["item"]}")
                    print(f"Price: {cart["price"]}")
                    print()
        case 8:
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
                    
                    
                
            
            
             
                
                
            
       
