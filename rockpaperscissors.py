import random 
options=("ROCK","PAPER","SCISSORS")
choices=None
round=0
print("Lets play ROCK,PAPER SCISSORS")
while True:
    option=random.choice(options)
    choices=input("WHAT DO YOU WANT TO CHOOSE: ").upper()
    if choices=="ROCK" or choices=="PAPER" or choices=="SCISSORS":
        choices=str(choices)
        round +=1
        print(f"Players choice={choices}")
        print(f"computers choice={option}")
        if option==choices:
         print(f"ITS A TIE. SINCE YOU AND COMPUTER CHOOSE {option}")
        elif option=="ROCK" and choices=="PAPER":
         print(f"CONGRATULATION YOU WIN in {round}round. {choices} wins over {option}")
         break
        elif option=="PAPER" and choices=="SCISSORS":
         print(f"CONGRATULATION YOU WIN in {round}round. {choices} wins over {option}")
         break
        elif option=="SCISSORS" and choices=="ROCK":
         print(f"CONGRATULATION YOU WIN in {round}round. {choices} wins over {option}")
         break
        else:
         print(f" YOU LOSE,TRY AGAIN.SINCE {option} wins over {choices}")
    else:
        print("INCORRECT CHOICE")
        print("Please select from ROCK ,PAPER AND SCISSORS")
    
