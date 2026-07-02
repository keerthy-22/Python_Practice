products = []
bill = """
                  Dmart Invoice
            Patamata Lanka,Vijayawada
--------------------------------------------------------------
    Name                Quantity            Price           Cost
"""
while True: 
    name = input("Name: ")
    quantity = int(input("Quantity: "))
    price = int(input("Price Per Unit: "))
    cost = quantity * price
    product = {"name":name,"quantity":quantity,"price":price,"cost":cost}
    products.append(product)
    choice = input("Do you want to generate the bill? (y/n) : ")
    if choice == 'y':
        break 
total = 0
for product in products:
    line = f"\n\t{product["name"]} \t\t\t\t{product["quantity"]} \t\t\t{product["price"]} \t\t\t{product["cost"]}"
    bill += line 
    total += product["cost"]
bill += f"\n\n\t\t\t\t\tTotal: {total}"
with open("Bill.txt","w") as file:
    file.write(bill)

    
    
    
    
