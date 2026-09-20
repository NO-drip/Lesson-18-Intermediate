valid = False
while not valid:
    try:
        bill_amount, discount_percentage, count_people = input("Can you enter how much your bill is, your discount and how much people.").split(",")
        bill_amount = float(bill_amount)
        discount_percentage = float(discount_percentage)
        count_people = int(count_people)
        if bill_amount <= 0 or count_people <= 0 or discount_percentage <= 0:
            raise ValueError
        discount_amount = (bill_amount * discount_percentage)/100
        total_cost = bill_amount - discount_amount

        shared_total_amount = total_cost / count_people
    except ValueError:
        print("Please enter a valid number.")
    except ZeroDivisionError:
        print("Please enter your actual amount greater than 0.")
    else:
        print(f"Your discount amount is {shared_total_amount} dollars")
        valid = True
    finally:
        print("This attempt has been run!")
    


    


            

