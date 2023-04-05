# # ```
# print("welcome to the restaurant")
# starter_menu = ("corn on cob", "tart", "chicken fingers", "dumplings", "wings", "no starters")
# main_menu = ("salmon fillets", "grilled chicken", "ribs", "pasta", "meatloaf")
# dessert_menu = ("cheesecake", "trifle", "milkshake", "puddings", "waffle", "no desserts")
# # ```
# # ```
# customers_order =[]
# print("starter_menu:")
# for item in starter_menu:
#     print("-" + item)
# print("main_menu")
# for item in main_menu:
#     print("-" + item)
# print("dessert menu")
# print(dessert_menu)
# for item in dessert_menu:
#     print("-" + item)
# # ```
#
# # ```
# for i in range(3):
#     print("Order", i+1)
#     customers_order = input("What would you like to order? ")
#     customers_order.append([starter_menu, main_menu, dessert_menu])
# # ```
# print("Your order:")
# for customers_order in customers_order:
#     print("- " + customers_order)
# # ```
# item = variable / anything / index / starting point
# index
print("Welcome to the restaurant")

starter_menu = ("1- corn on cob", "2- tart", "3- chicken fingers", "4- dumplings", "5- wings", "no starters")
main_menu = ("1- salmon fillets", "2- grilled chicken", "3- ribs", "4- pasta", "5- meatloaf")
dessert_menu = ("1- cheesecake", "2- trifle", "3- milkshake", "4- pudding", "5- waffle", "no desserts")
#
# # item = variable / anything / index / starting point
# # empty list variable  - customer_order
customers_order = []
print("Starter menu:")
for item in starter_menu:
    print("option " + item)
print("Main menu:")
for item in main_menu:
    print("option " + item)
print("Dessert menu:")
for item in dessert_menu:
    print("option " + item)
print("These are you orders: ")
#
# # i = range 0 (index) ,it initially loops over to what you choose, range (3) = function which starts from 0
# # and stops in a specified number which in this case 3(max list of orders that can be placed)
# # then +1 = another time, until the range finishes.
for item in range(3):
    print("Order", item+1)
    starter = input("what starter from the menu do you choose?: ")
    main = input("what main from the menu do you choose?: ")
    dessert = input("what dessert from the menu do you choose?: ")
    customers_order.append((starter, main, dessert))
#
# prints the customers orders back to them, the list of 3 orders they have ordered.
# the f function is used to add the variables with the index's which comes out in order in a row.
print("Your order:")
for item in range(len(customers_order)):
    print(f"Order {item+1}: {customers_order[item][0]}, {customers_order[item][1]}, {customers_order[item][2]}")




