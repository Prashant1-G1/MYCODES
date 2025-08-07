principle=0
rate=0
time=0
while principle<=0:
    principle=float(input("Enter the priciple: "))
    if principle<=0:
        print("priciple can't be less or equal to zero!")
while rate<=0:
    rate=float(input("Enter the rate: "))
    if principle<=0:
        print("rate can't be less or equal to zero!")
while time<=0:
    time=float(input("Enter the time in years : "))
    if principle<=0:
        print("time can't be less or equal to zero!")
compound_interest=principle*pow((1+rate/100),time)
print(f"The compound interest of your priciple  after {time} will be : {compound_interest:,.2f}")



