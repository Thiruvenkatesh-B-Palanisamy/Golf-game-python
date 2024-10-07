from random import randint
club = "D"

def game_play(club, distance):
    if club == "D":
        driver = randint(80, 120)
        if driver > distance:
            print("\nYour shot went {}m.".format(distance))
            distance = 0
        else:
            distance = distance - driver
            print("\nYour shot went {}m.".format(driver))
        return distance
    elif club == "I":
        iron = randint(20, 40)
        if iron > distance:
            print("\nYour shot went {}m.".format(distance))
            distance = 0
        else:
            distance = distance - iron
            print("\nYour shot went {}m.".format(iron))
    elif club == "P":
        putter = randint(1, 10)
        if putter > distance:
            print("\nYour shot went {}m.".format(distance))
            distance = 0
        else:
            distance = distance - putter
            print("\nYour shot went {}m.".format(putter))
    else:
        print("\nInvalid club selection-air swing:(")

    return distance


