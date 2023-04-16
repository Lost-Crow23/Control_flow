# 10 integers are to be taken from the list and the average value is to be solved
print("we are going to work out the average of this numbers, please enter 10 numbers: ")

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
num_4 = int(input())
num_5 = int(input())
num_6 = int(input())
num_7 = int(input())
num_8 = int(input())
num_9 = int(input())
num_10 = int(input())

num_list = [num_1, num_2, num_3, num_4, num_5, num_6, num_7, num_8, num_9, num_10]
print(num_list)
# Average formula
average = sum(num_list) / len(num_list)
print(f"your average is", {average})

# loop to print the following series
for num in range(1, 300):
    if num % 10 == 0:
        print(num)

