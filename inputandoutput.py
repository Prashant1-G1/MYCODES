total=0
cart=[]
item=None
while True:
    item=input("Enter the item do you want to buy: ").upper()
    if item=="QUITE":
        break
    quantitity=int(input("How many: "))
    price=float(input("Enter the price for the item: "))
    cart.append((item, quantitity))
    total=total+(quantitity*price)
print("THANKS FOR BUYING")
print("YOUR ORDER LIST")
for item,quantitity in cart:
    print(f"{item:10}:x{quantitity}")
print(f"TOTAL=${total:5.2f}")
   
