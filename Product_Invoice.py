pid=int(input("Enter your pid:"))
name=input("Enter your Name:")
price=float(input("Enter your price:"))
quantity=int(input("Enter your quantity:"))
print(f"PID={pid},NAME={name},PRICE={price}and QUANTITY={quantity}")
total=price*quantity
discount=0.0
if total<5000:
    discount=(total*15)/100
elif total>5000 and total<10000:
    discount=(total*21)/100
elif total>10000 and total<30000:
    discount=(total*31)/100
elif total>=30000:
    discount=(total*35)/100
else:
    print("Invalid data")
gst=(total*18)/100
final_bill=(total-discount)+gst
print(f"TOTAL={total}")
print(f"DISCOUNT={discount}")
print(f"GST={gst} and FINAL_BILL={final_bill}")
