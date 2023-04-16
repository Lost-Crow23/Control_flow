# loops

# for loops and foreach loops
# In python just for loops, that you can then specify how you want the loop

# list_data = [1, 2, 3, 4, 5]
# embedded_lists = [[1, 2, 3], [4, 5, 6]]
# dict_data = {
#     1: {"name": "Bronson",}
# for loops and foreach loops
# In python just for loops, that you can then specify how you want the loop

list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1, 2, 3], [4, 5, 6]]
dict_data = {
    1: {"name": "Bronson",
       "money": "$0.05"},
    2: {"name": "Masha",
        "money": "$3.66"},
    3: {"name": "Roscoe",
        "money": "$1.14"},
}
# basic loop
# number is a variable, anything you want to name
for number in list_data:
    print(number * 2)

# nested loop
# prints the first element of data then the
for data in embedded_lists:
    print(data)
    for number in data:
        print(number)

# looping through the dictionaries
for value in dict_data:
    print(value)
for item in dict_data.values():
    print(item)

for item in dict_data.values():
    for embed_value in item.values():
        print(embed_value)

for items in dict_data.values():
    print(items["money"])

for number in list_data:
    if number == 3:
        print("i found three! ")
    elif number > 3:
        print("i have gone to far")
    else:
        print("too soon")

# while loops
# while loops = monitors a condition
x = 0

while x < 10:
    print(f"it's working -> {x}")
    if x == 4:
        break
    x += 1

# call particular services (API)

# using while loops to verify user input

age = input("what is you age")
print(f"your age is {age} ")

user_prompt = True

while user_prompt:
    age = input("what is your age?: ")
    if age.isdigit() and int(age) < 117:
        user_prompt = False
    else:
        print("please provide age in digits")
print(f"your age is {age} ")

dict_data = {
    1: {"name": "Bronson",
        "money": "$0.05"},
    2: {"name": "Masha" ,
        "money": "$3.66"},
    3: {"name": "Roscoe",
        "money": "$1.14"},
}
# basic loop
# number is a variable, anything you want to name
for number in list_data:
    print(number * 2)

# nested loop
# prints the first element of data then the
for data in embedded_lists:
    print(data)
    for number in data:
        print(number)

# looping through the dictionaries
for value in dict_data:
    print(value)
for item in dict_data.values():
    print(item)

for item in dict_data.values():
    for embed_value in item.values():
        print(embed_value)

for items in dict_data.values():
    print(items["money"])

for number in list_data:
    if number == 3:
        print("i found three! ")
    elif number > 3:
        print("i have gone to far")
    else:
        print("too soon")

# while loops
# while loops = monitors a condition
x = 0

while x < 10:
    print(f"it's working -> {x}")
    if x == 4:
        break
    x += 1

# call particular services (API)

# using while loops to verify user input

age = input("what is you age")
print(f"your age is {age} ")

user_prompt = True

while user_prompt:
    age = input("what is your age?: ")
    if age.isdigit() and int(age) < 117:
        user_prompt = False
    else:
        print("please provide age in digits")
print(f"your age is {age} ")

num = 0
while num < 300:
    print(num)
    num += 10

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])




