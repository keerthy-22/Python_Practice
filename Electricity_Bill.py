ConsumerId = int(input("Enter the ID: "))
ConsumerName = input("Enter the Name: ")
CurrentReading = int(input("Enter the Current Reading: "))
PreviousReading = int(input("Enter the Previous Reading: "))
units = CurrentReading - PreviousReading
if units <= 300:
    rate = 1.75
elif units <= 500:
    rate = 3.25
else:
    rate = 7.25
Total_Bill = units * rate
print("\n----- Electricity Bill -----")
print("Consumer ID :", ConsumerId)
print("Consumer Name :", ConsumerName)
print("Current Reading :", CurrentReading)
print("Previous Reading :", PreviousReading)
print("Units Consumed :", units)
print("Rate :", rate)
print("Total Bill :", Total_Bill)
