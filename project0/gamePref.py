games = ["Monopoly","Trivial Pursuit","Chess","Poker"]
print("I like the games: " + str(games))
new_game = input("What game do you like to play? ")
games.append(new_game)
print("Games we like: " + str(games))