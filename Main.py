from random import randint


def main():
    player_name = player_name_check()
    print("Welcome", player_name + ".\nLets play golf,CP1401 style!")
    par = choose_par()
    distance = distance_choose()
    game_results = []
    game_over = False
    while not game_over:
        get_player_choice = input("\nLet's play golf, CP1401 style!\n(I)nstructions\n(P)lay golf\n(Q)uit\n").upper()
        game_play_options = ["I", "P", "Q"]
        while get_player_choice not in game_play_options:
            get_player_choice = input("Invalid input..\n"
                                      "Let's play golf, CP1401 style!\n"
                                      "(I)nstructions\n(P)lay golf\n(Q)uit\n\n").upper()
        if get_player_choice == "I":
            print("\nThis is a simple golf game in which each hole is {}m game away with par {}. You are able to\n"
                  "choose from 3 clubs, the Driver, Iron, or Putter. The Driver will hit around 100m, The Iron "
                  "around\n30m and the Putter around 10m. The putter is best used very close to the hole.\n"
                  "\nFor each shot, you may use a driver, iron or a putter – each shot will vary in distance.\n"
                  "The average distance each club can hit is:\n"
                  "  Driver = 100m\n  Iron = 30m\n  Putter = 10m".format(distance, par))
            game_over = False
        elif get_player_choice == "P":
            game_score = game_play(par, distance)
            game_results.append(game_score)
            print("Your overall score is {} and you are {} par".format(game_results, par))
            game_over = False
        elif get_player_choice == "Q":
            print("\nThanks for playing {}.".format(player_name))
            for result in (1, len(game_results)):
                print("Round {} : {}shots.  par".format(result, game_results))

            game_over = True


def player_name_check():
    player_name = input("What is your name?\n")
    while len(player_name) < 1:
        player_name = input("\nPlayer name must be atleast 1 character.\nWhat is your name?\n ")
    return player_name


def choose_par():
    par = str(input("\nChoose a par for this course(between 3-5 inclusive).\n"))
    par_length = ["3", "4", "5"]
    while par not in par_length:
        par = str(input("\nI'm sorry, you must choose a number between 3-5 inclusive. Please enter again..\n"))
    par = int(par)
    return par


def distance_choose():
    distance = 0
    input_check = False
    while not input_check:
        try:
            distance = int(input("\nHow many meters to the hole(between 195-250 inclusive)\n"))
            while distance not in range(195, 251):
                distance = int(input("\nDistance must be between 195-250\n"))
                input_check = True
            input_check = True
        except ValueError:
            print("Distance must be numerical")
    return distance


def game_play(par, distance):  # to start the game
    print("\nThe hole is a {}m par {}\n".format(distance, par))
    distance_meter = distance
    shot_count = 0
    while not distance_meter <= 0:
        print("You are {}m away from the hole, after {} shot/s".format(distance_meter, shot_count))
        club = input("Club selection: press D for driver, I for Iron, P for Putter.\nChoose club:").upper()
        if club == "D":
            driver = randint(80, 120)
            distance_meter = distance_meter - driver
            print("\nYour shot went {}m.".format(driver))
        elif club == "I":
            iron = randint(20, 40)
            distance_meter = distance_meter - iron
            print("\nYour shot went {}m.".format(iron))
        elif club == "P":
            putter = randint(1, 10)
            distance_meter = distance_meter - putter
            print("\nYour shot went {}m.".format(putter))
        else:
            print("\nInvalid club selection-air swing:(")
            distance_meter = distance_meter - 0
        shot_count = shot_count + 1
    if shot_count + 1 < par:
        print("Clunk...After {} hits your ball is in the hole!\nCongratulations. You are {} under par for this hole!"
              .format(shot_count, par - shot_count))
    elif shot_count + 1 == par:
        print("Clunk...After {} hits your ball is in the hole!\nAnd that's par.".format(shot_count, par - shot_count))
    elif shot_count + 1 > par:
        print("Clunk...After {} hits your ball is in the hole!\nDisappointing. You are {} over par for this hole."
              .format(shot_count, shot_count - par))
    print("Your overall score is {} and you are {}".format(shot_count, par - shot_count))
    return shot_count - 1


main()


