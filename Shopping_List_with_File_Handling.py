with open("Shopping.txt","w") as file:
    file.writelines(["Shopping Chudidhar\n","Formals\n","Tops and Bottoms\n","Western\n"])
with open("Shopping.txt","r") as file:
   data = file.readlines()
   print(data)
with open("Shopping.txt","a") as file:
    file.writelines(["Ethnic\n","Frocks\n","Nightwear\n","Jeans\n"])
