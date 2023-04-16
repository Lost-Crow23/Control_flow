while True:
        customer_age = int(input("Enter your age: "))
        if customer_age < 1 or customer_age > 117:
            print("Invalid age. Please enter a number between 1 and 117.")
        else:
            break
        print("Invalid input. Please enter a number between 1 and 117.")
if customer_age <= 12:
    print("You can watch U, PG, and 12 rated movies.")
elif customer_age <= 15:
    print("You can watch U, PG, 12, and 15 rated movies.")
else:
    print("You can watch all rated movies.")


