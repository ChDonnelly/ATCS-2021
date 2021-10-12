games = ["Monopoly","Trivial Pursuit","Chess","Poker"]
print("I like the games: " + str(games))

wantsToAdd = True
while (wantsToAdd):
    new_game = input("Do you want to add a new game? ")
    if (new_game.contains("es")):
        games.append(new_game)
    else:
        wantsToAdd = False

"""
new_game = input("What game do you like to play? ")
games.append(new_game)
print("Games we like: " + str(games))
"""