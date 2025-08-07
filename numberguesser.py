import random
lowest=int(input("enter the lowest number: "))
highest=int(input("enter the highest number: "))
secertnumber=random.randint(lowest,highest)
print(f"Can you guess a  random number between ({lowest} and {highest})?")
tries=0
guess=None
while True:
    guess=(input("enter the number you have guessed: "))
    if guess.isdigit():
        guess=int(guess)
        tries +=1
        if guess<lowest or guess>highest:
         print("The number is out of range!!")
         print(" please enter the number from {lowest} to {highest}")
        elif guess>secertnumber:
         print("Try again")
         print("To high")
        elif guess<secertnumber: 
         print("Try again")
         print("To low")
        else:
         print(f"YOU guesses the correct number in {tries}tires. The number was {secertnumber}")
         break
    else:
        print("INCORRECT INTEGER")
   

