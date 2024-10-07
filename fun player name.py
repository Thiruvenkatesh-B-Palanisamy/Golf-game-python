def player_name():
    player_name = input("What is your name?")
    while len(player_name) < 1:
        player_name = input("Player name must be atleast 1 character.\nWhat is your name? ")
    return player_name

player_name()

