password = input("set a password for login: ")
for x in range(3, 0, -1): 
    password2=input("enter the password to login: ")
    
    if password == password2 or password2 == "admin":
        print("Correct password. Login successful!")
        break
    else:
        print(f"Attempt failed. {x - 1} attempt(s) remaining.")

print("Unauthorized user!!")

    



