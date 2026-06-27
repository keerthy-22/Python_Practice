with open("Destinations.txt","w") as file:
    file.writelines(["Paris\n","France\n","Korea\n","Japan\n","London\n"])
with open("Destinations.txt","r") as file:
   data = file.readlines()
   print(data)
with open("Destinations.txt","a") as file:
    file.writelines(["America\n","Scotland\n","New York\n","Canada\n","Italy\n"])
