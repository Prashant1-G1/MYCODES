import time
timee=int(input("Enter the time you want to sleep(in seconds): "))
for x in range(timee,0,-1):
  seconds=x%60
  minute=int(x/60)%60
  hours=int(x/3600)
  print(f"{hours:02}:{minute:02}:{seconds:02}")
  time.sleep(1)
print("WAKE UP!")