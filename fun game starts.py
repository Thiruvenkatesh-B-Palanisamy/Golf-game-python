from random import randint
distance = 200
par = 5


def game_play():  # to start the game
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


game_play()
