"""
Going over control flow examples.
"""
# print(ord("Z"))
# print(ord("z"))
# print("Notice they are representing by different numbers.")

# TEMPERATURE = 50
# if TEMPERATURE > 30:
#     print("\nIt's warm!")
#     print("Drink water.")
# elif TEMPERATURE > 20:
#     print("It's mild.")
# else:
#     print("It's samui.")
# print("Dang, I am really wasting my time.")

# ALL OF THIS CAN BE COMPACTED INTO...
# AGE = 12
# if AGE >= 18:
#     MESSAGE = "Valid"

# else:
#     MESSAGE = "Invalid"
# THIS. A ternary operator.
# MESSAGE = "Valid" if AGE >= 18 else "Invalid"
# print(MESSAGE)

# TESTNUM = 25
# if TESTNUM >= 18 and TESTNUM < 65:
#     print("BOTH OF THESE LINES ARE LOGICALLY EQUAL.")

# if 18 <= TESTNUM < 65:
#     print("THIS IS JUST CHAINING COMPARISON OPERATORS.")

# for number in range(3):
#     print("Loop", number + 1, (number + 1) * ".")


# #NESTING LOOPS
# for x in range(5):
#     for y in range(3):
#         print(f"({x}, {y})")

# #ITERABLES
# print(type(5))
# print(type(range(5)))

# for x in "Python":
#     print(x)
# for y in [1,2,3,4,5]:
#     print(y)

# # #WHILE LOOP
# number = 100
# while number > 0:
#     print(number)
#     number //= 2

# command = ""
# while command.lower() != "quit":
#     print(command != "quit" or command != "QUIT")
#     command = input(">")
#     print("ECHO", command)

#Infinite loops
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break
    