with open("Library.txt","w") as file:
    file.writelines(["You can Win\n","He made a Promise\n","The Silent Patient\n","The Midnight Library\n"])
with open("Library.txt","r") as file:
   data = file.readlines()
   print(data)
with open("Library.txt","a") as file:
    file.writelines(["To Kill a Mockingbird\n","The Great Gatsby\n","1984\n","Pride and Prejudice\n"])
