Questions=["what is my name?",
          "what is my age?",
          "what do i like?",
          "what am i?"]
options=(("A.PRASHANT","B.RAM","C.SHYAM","D.HARI"),
         ("A.18","B.19","C.23","D.34"),
         ("A.CARROT","B.MANGO","C.STRAWBERRY","D.PINEAPPLE"),
         ("A.ANIMAL","B.GOD","C.ALIEN","D.HUMAN"),)
answers=["A","A","B","D"]
score=0
percentage=0
guesses=[]
question_num=0
for question in Questions:
    print("..............................")
    print(question)
    for option in options[question_num]:
      print(option)
    guess=input("Enter the answer: ").upper()
    guesses.append(guess)
    if guess==answers[question_num]:
      print("YOU ARE CORRECT")
      score+=1
    else:
      print(f"YOU ARE INCORRECT THE ANSWER WAS {answers[question_num]}")
    question_num=question_num+1
print("...................................")
print("............RESULT.................")

print("answers=",end="")
for answer in answers:
   print(answer,end=" ")
print()
print("guesses=",end="")
for guess in guesses:
   print(guess,end=" ")
print()

print(f"YOUR TOTAL SCORE={score}")
percentage=int(score/len(Questions)*100)
print(f"PERCENTAGE={percentage}%")