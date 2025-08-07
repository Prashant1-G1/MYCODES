#calculator program
print("which action do you want to perform")
print("1.+")
print("2.-")
print("3.*")
print("4./")
action=input('Enter the action: ')
num1=float(input("enter the first number: "))
num2=float(input("Enter the seconnd number: "))
if action=="1":
 result=num1+num2
 print(f"The sum: {result}")
elif action=="2":
 result=num1-num2
 print(result)
elif action=="3":
 result=num1*num2
 print(round(result,3))
elif action=="4":
 if num2==0:
  print("infinity")
 else:
  result=num1/num2
  print(round(result,3))
else:
 print("Enter the order of the action properly!!")