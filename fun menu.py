game_over = False
while not game_over:
    get_player_choice = input("Let's play golf, CP1401 style!\n(I)nstructions\n(P)lay golf\n(Q)uit\n").upper()
    game_play_options = ["I", "P", "Q"]
    while get_player_choice not in game_play_options:
        get_player_choice = input("Invalid input..\n"
                                  "Let's play golf, CP1401 style!\n"
                                  "(I)nstructions\n(P)lay golf\n(Q)uit\n").upper()

    if get_player_choice == "I":
        print("This is a simple golf game in which each hole is 230m game away with par 5. You are able to choose "
              "from 3 clubs, the Driver, Iron, or Putter. The Driver will hit around 100m, The Iron around 30m "
              "and the Putter around 10m. The putter is best used very close to the hole.\n"
              "For each shot, you may use a driver, iron or a putter – each shot will vary in distance.\n"
              "The average distance each club can hit is:\n"
              "Driver = 100m\nIron = 30m\nPutter = 10m")
        game_over = False
    elif get_player_choice == "P":
        print("Game is coming soon")
        game_over = False
    elif get_player_choice == "Q":
        print("Thanks for playing")
        game_over = True

