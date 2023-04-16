# # using the range method to print out 10 times, items is variable
# # Hello, is printed out 10 times, to test if the loops are functional.
for item in range(10):
    print("hello")
#
# # Create another loop with a range that asks for names and appends to list_names
# initialise a list
list_data = []

# asks user input (names) , adds all names and type "finished" to end the process
names = ""
while names.strip().lower() != "finished":
    list_data.append(names.strip())
    names = (input("Enter a name or type finished: "))
print("the names you entered are: ", list_data)
#
# '''
# # This loop iterates over each name in list_data and
# # formats it into lowercase in a new variable called list_names_lower
# '''
counter = 0
list_names_lower = []
for name in list_data:
    list_names_lower.append(list_data[counter].lower())
    counter += 1
print(list_names_lower)
# lastly, amount of names in the list is thus counted, and tells the user, if it's either odd or even
if counter % 2 == 0:
    print("There are an even amount of numbers in the list data")
else:
    print("There are an odd amount of names in the list data")



