
<h1>Movie list</h1>
This code is a ` movie list ` created by various methods.

Using this **While loop** if entered outside the bracket, it prints out invalid input and restarts the cycle.
````
while True:
        customer_age = int(input("Enter your age: "))
        if customer_age < 1 or customer_age > 117:
            print("Invalid age. Please enter a number between 1 and 117.")
        else:
            break
        print("Invalid input. Please enter a number between 1 and 117.")
 ````
if statement is used to achieve, the desired output, if entered less than 12, 15.

    if customer_age <= 12:
        print("You can watch U, PG, and 12 rated movies.")

    elif customer_age <= 15:
        print("You can watch U, PG, 12, and 15 rated movies.")

If above other values, it outputs the print function below.
    
    else:
        print("You can watch all rated movies.")