try:
    value_1, value_2  = eval(input("Enter 2 numbers, seperated by a comma."))
    divide = value_1 / value_2
    print(divide)
except ValueError:
    print("Enter a actual number please.")
except SyntaxError:
    print("Please try again. Seperate your numbers with a comma.")
except ZeroDivisionError:
    print("Number divided by 0 is not possible.")
except:
    ("Something is wrong. Please try again.")
else:
    print("No errors at all.")
finally:
    print("Thanks for trying.")