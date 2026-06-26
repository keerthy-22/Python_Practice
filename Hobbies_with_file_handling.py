with open("Hobbies.txt","w") as file:
    file.writelines(["Watching Movies\n","Cooking\n","Drawing\n"])
with open("Hobbies.txt","r") as file:
   data = file.readlines()
   print(data)
with open("Hobbies.txt","a") as file:
    file.writelines(["Traveling\n","Photography\n","Crafting\n"])
