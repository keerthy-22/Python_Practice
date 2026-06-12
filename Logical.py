# sum of two number equal to 10
a=5
b=5
print(a+b==10)

#first two nums mul equals to 3rd num
n1=8
n2=5
print(n1*n2==40)

#ave of 4 nums greater than 60
a=40
b=20
c=100
d=150
print((a+b+c+d)/4>60)

#num is divisible by 7
x=49
print(x%7==0)

#num not divisible by 100
num=5
if num%100!=0:
    print("not divisible")
else:
    print("divisible")
    
#number is Even   
num=7
print(num%2==0)

#Quantity of friuts exactly in dozens
quantity=48
if quantity%12==0:
    print("quantity is exactly in dozens")
else:
    print("quantity is not exactly in dozens")

#sqa of first num equals to cube of second num
a=8
b=4
print(a**2==b**3)

#last digit of num equal to 5
num=15
print(num%10==5)

#last digit of given 2 num are same
num1=80
num2=40
print(num1%10==num2%10)

#sum of last digits of given three nums is equal to 1
num1=11
num4=4
num3=6
print(num1%10+num2%10+num3%10==1)

#condition for person can vote
a=int(input("Enter a number:"))
if a>=18:
    print("Eligible")
else:
    print("Not eligible")
    
#last digit of given number divisible by 3   
x=123
print((x%10)%3==0)

#average of 3 numbers equal to first number
a=6
b=9
c=3
print((a+b+c)/3==a)

#sqare of last digits greater than 10
a=36
last_digit=a%10
print((a**2)>10)

#square of last digit of given num divisible by 7
x=47
last_digit=x%10
print((last_digit**2)%7==0)
