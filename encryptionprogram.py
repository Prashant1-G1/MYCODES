import random
import string
chars= " "+ string.punctuation+string.ascii_letters+string.digits
chars=list(chars)
encrypted=""
keys=chars.copy()
random.shuffle(keys)
print(f"chars={chars}")
print(f"keys={keys}")
plain_text=input("Enter a text to encrypt:")
for letters in plain_text:
    index=chars.index(letters)
    
    encrypted+=keys[index]
   
print()
print(f"oringinal text: {plain_text}")
print(F"Encrpted text: {encrypted}")