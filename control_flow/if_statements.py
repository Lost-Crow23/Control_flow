 # if, elif and else

 # movie ratings
age = 15
if age >= 18:
    print("you are the correct age to buy a ticket for this movie")
elif age < 18:
    print("sorry, you are not old enough to by a ticket of this movie")

# elif , else

film_rating = "universal"

if film_rating.lower() == "universal":
    print("All ages can watch this movie")
elif film_rating.lower() == "pg":
    print("Parental guidance recommended")
elif film_rating.lower == "12":
    print("you must be at least 12 years old to watch this movie")
elif film_rating.lower == "15":
    print("you must be at least 15 years old to watch this movie")
elif film_rating.lower == "18":
    print("you must be at least 18 years old to watch this movie")
else:
    print("Not correct rating, please use universal, pg, 12, 15 or 18")

#


