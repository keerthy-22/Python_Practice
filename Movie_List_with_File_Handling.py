with open("Prabhas_Movie.txt","w") as file:
    file.writelines(["Eeshwar\n","Raghavendra\n","Varshan\n","Adavi Ramudu\n","Chakram\n","Chatrapathi\n","Pournami\n","Yogi\n","Munna\n","Buji Gadu\n"])
with open("Prabhas_Movie.txt","r") as file:
   data = file.readlines()
   print(data)
with open("Prabhas_Movie.txt","a") as file:
    file.writelines(["Billa\n","Ek Niranjan\n","Darling\n","Mr.Perfect\n","Rebel\n","Mirchi\n","Bahubali-1\n","Bahubali-2\n","Sahoo\n","Radhe Shyam\n","Salaar\n","Kalki 2898 AD\n"])
