# Made a change to file
# git revert --no-commit HEAD

# collections
# lists
# array = list

# first list = shopping list
# [] = list
shopping_list = ["milk", "bread", "eggs", "chocolate", "Jam"]
print(shopping_list)
print(type(shopping_list))

# accessing a particular part of the list
print(shopping_list[1])

# change an element in a list
shopping_list[2] = "butter"
print(shopping_list[2])

# List Methods
# add to a list
shopping_list.append("olives")
print(shopping_list)

# remove item
shopping_list.remove("Jam")
print(shopping_list)

# remove last item
shopping_list.pop()
print(shopping_list)

# can i have a list with mixed data types
mixture = [1, 2, 3.5, "six", "five"]
print(mixture)

# slicing
print(mixture[1:3])

# reverse order of slice
print(mixture[-2::])

# step over
print(mixture[::2])

# tuples are IMMUTABLE
tuple_example = ("bread", "eggs", "milk")
print(tuple_example)

# dictionaries
# manage data, more dynamic and complex
# key-value pairs
# key = reference to object
# value = data mechanism to store data in (e.g. string, int, list)

student_1 = {
    "name": "Luke",
    "stream": "DevOps",
    "completed_lesson": 4,
    "completed_lesson_names": ["variables", "data_types", "setup"]
}

print(student_1["stream"])

# access part of the list in the dictionary
print(student_1["completed_lesson_names"][1])

# changing value in a dictionary
student_1["completed_lesson"] = 5
print(student_1["completed_lesson"])

# changing an element of list within a dictionary
student_1["completed_lesson_names"].remove("data_types")
print(student_1["completed_lesson_names"])

# dictionary methods
print(student_1.keys())

print(student_1.values())

# sets and frozen sets
# sets in python list that has no order/indexing
car_parts = {"wheels", "doors", "exhaust"}
print(car_parts)

car_parts.add("windows")
print(car_parts)
car_parts.discard("doors")
print(car_parts)

# frozen sets
x = frozenset([1, 2, 3, 4])
x.add(5)
print(x)
# comment
