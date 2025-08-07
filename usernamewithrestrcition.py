username=None
while True:
 username=input("Enter your usernamename: ")
 if len(username)>12:
    print("You can't enter more than 12 characters")
 elif  not username.find(" ") == -1:
    print("You can't use space in your name")
 elif not  username.isalpha():
    print("YOu can't enter number in your username") 
 else:
   print(f"Welcome {username}")
   break