Shoplist={"DOTA 2": 20,
          "fortnite": 15, 
          "PUBG": 50 ,
          "APEXLEGENDS": 25,
          "VELORANT": 16.99}
total=0
cart=[]
print(".........GAME LIST..........")
for key , value in Shoplist.items():
    print(f"{key:12}:${value:.2f}")
print("............................")
while True:
    games=input("select the games you want to purchase: ").upper()
    if games=="QUITE":
        break
    elif Shoplist.get(games) is not None:
        cart.append(games)
print("...........GAMES..............")

for games in cart:
    print(games,end="")
    total= total+Shoplist.get(games)
    print()
print(f"Your total=${total} ")
print("......THANK'S FOR PURCHASING.......")
