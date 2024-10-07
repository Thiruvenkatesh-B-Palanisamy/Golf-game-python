valid_input = True
while valid_input:
    try:
        score = int(input("Please enter score: "))
        while score < 0 or score > 100:
            print("Score must be between 0 and 100")
            score = int(input("Please enter score: "))
        valid_input = False
    except ValueError:
        print("Score must be a number")

print(score)

