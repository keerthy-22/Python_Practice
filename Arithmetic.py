#Arithmetic
n=2
s=n*n
c=n*n*n
print(s+c)
#Adding
bal=5000
amt=3500
bal=bal+amt
print(bal)
#Sum of numbers with 3rd variable
a=5
b=3
c=a+b
print(c)
#Swap
a=5
b=3
a=b
b=a
print(a,b)
#Sum
sum=0
i=1
sum=sum+i
i=i+1
sum=sum+i
i=i+1
sum=sum+i
i=i+1
sum=sum+i
print(sum)
print(i)
#Factorial
fact = 1
i = 1
fact = fact*i
i=i+1
fact=fact*i
i=i+1
fact=fact*i
i=i+1
fact=fact*i
print(fact)
print(i)
#Sum 
n = 2345
sum=0
sum=sum+n%10
n=n/10
sum=sum+n%10
n=n/10
sum=sum+n%10
n=n/10
sum=sum+n%10
n=n/10
print(sum,n)
#Reverse a number
n=2345
rev=0
rev=rev*10+n%10
n=n/10
rev=rev*10+n%10
n=n/10
rev=rev*10+n%10
n=n/10
rev=rev*10+n%10
n=n/10
print(rev,n)

#Adding of two numbers
a = 10
b = 20
c = a + b
print("The sum of two numbers is:", c) 
#Display quotient and remainder after division
divisor = 10
dividend = 20
print("quotient of the division:",dividend/divisor)
print("remainder of the division:",dividend%divisor)
#To find the total and average of 3 numbers
a = 20
b = 22
c = 28
sum = a+b+c
print("Total of 3 numbers:",sum)
print("Average of 3 numbers:",a+b+c/3)
#To find the square of given number
a = 4
square = a**2
print("Square of given number:",square)
#To find the Cube of given number
a = 4
cube = a**3
print("Cube of given number:",cube)
#To find the sum of square and cube of given number
a = 4
square = a**2
cube = a**3
sum = square+cube
print("Square of given number:",square)
print("Cube of given number:",cube)
print("sum of square and cube of give number:",sum)
#To display last digit of given number
a = 224
print("Last digit of given number:", a % 10)
#To remove last digit of given number
a = 125
print("Remove last digit of given number:",a//10)
#Sum of first n numbers
n = int(input("enter n: "))
formula = (n*(n+1))//2
print("Sum of first n numbers:",formula)
#swap 2 numbers
a = 2 
b = 4
temp = a
a = b
b = temp
print("swapping of two numbers:",a,b)
#Program to swap 2 numbers without using 3rd variable
a = 2
b = 4
a,b = b,a
print("Swap of 2 numbers:",a,b)
#Program to calculate the total amount of given quantity of fruits
a = 6
m = 8
p = 10
purchase = a*10+m*20+p*30
print("Amount of fruits purchased:",purchase)
#Calculate the area of circle
r = int(input("enter r: "))
circle = 3.14*r*r
print("Area of the circle:",circle)
#Calculate the area of triangle
b = int(input("enter b: "))
h = int(input("enter h: "))
triangle = (1/2)*b*h
print("Area of the triangle:",triangle)#Calculate the time taken by using speed and distance
speed = 2
distance = 4
time = distance/speed
print(f"Time taken:{time}")
#Calculate the speed by using time and distance
time = 2
distance = 4
speed = distance/time
print(f"Speed:{speed}")
#Calculate the distance by using speed and time
speed = 2
time = 4
distance = speed*time
print(f"Distance covered:{distance}")
