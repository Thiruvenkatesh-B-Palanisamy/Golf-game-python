input_check = False
while not input_check:
    try:
        distance = int(input("How many meters to the hole(between 195-250 inclusive)\n"))
        while distance not in range(195, 251):
            distance = int(input("Distance must be between 195-250\n"))
            input_check = True
    except ValueError:
        print("Distance must be numerical")


print(distance)

