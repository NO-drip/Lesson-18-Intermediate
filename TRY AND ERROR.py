try:
    yeti = int(input("Enter a number."))
except ValueError as ex:
    print("Please a valid number")
    print(ex)