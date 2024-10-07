def choose_par():
    par = str(input("Choose a par for this course(between 3-5 inclusive)\n"))
    par_length = ["3", "4", "5"]
    while par not in par_length:
        par = str(input("I'm sorry, you must choose a number between 3-5 inclusive. Please enter again\n"))
    else:
        print("good job")


choose_par()
