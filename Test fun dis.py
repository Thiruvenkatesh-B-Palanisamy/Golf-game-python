distance = str(input("How many meters to the hole(between 195-250 inclusive)\n"))
distance_int = int(distance)
print(distance_int)
print(distance)
dis_calc = range(195, 250)
if distance_int not in range(195, 250):
    distance = str(input("I'm sorry you must choose a number between 195-250 inclusive. Please enter again\n"))
else:
    print("good job")
