i = int(input("Please enter i"))
while i is ValueError:
    try:
        i = int(input("Please enter i"))
    except ValueError:
        i = int(input("please enter numbers"))

print("well done")

