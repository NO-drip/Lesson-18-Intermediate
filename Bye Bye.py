value = False
while not value:
    try:
        user = int(input("Enter a number."))
        while user%2 == 0:
            print("bye bye.")
        value = True
    except ValueError:
        print("Goodbye. SEE YOU LATER!")



