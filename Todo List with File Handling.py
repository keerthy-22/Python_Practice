with open("Todo.txt","w") as file:
    file.writelines(["Attend Python Class\n","Attend Offline Python\n","Face Skin Care\n","Take Medince\n","Having Lunch\n"])
with open("Todo.txt","r") as file:
   data = file.readlines()
   print(data)
with open("Todo.txt","a") as file:
    file.writelines(["Meet my frnd\n","Go to shopping\n","Dinner at resturant\n","Go to Gym\n","Go to Sleep\n"])
