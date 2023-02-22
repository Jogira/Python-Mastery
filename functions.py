# def greet():
#     print("Hi there")
#     print("Welcome aboard.")

# def greet_with_name(first_name, last_name):
#     print(f"Hi there {first_name} {last_name}")
#     print("Welcome aboard.")

# def return_greeting(name):
#     return f"Hi {name}"

# greet_with_name("Jacko-o", "Valentine")
# greet()
# message = return_greeting("Sin")
# print(f"HEAVEN OR HELL: {message}")
# file = open("content.txt", "w")
# file.write(message)

# def increment(number, by = 1 ): #Defautl value of by is 1.
#     return number + by

# print(increment(number = 2)) #Example of keyword args.
# print(increment(number = 2, by = 20)) #Example of keyword args.


# # Can pass in multiple args using xargs by prepending * to a parameter.
# def multiply(*numbers):
#     print(numbers)
#     total = 1
#     for number in numbers:
#         total *= number
#     return total
#     # return x * y

# print(multiply(2, 3, 4, 5))

# # Can pass in multiple args using xxargs by prepending ** to a parameter. Automatically packs the invoke params into a dictionary.
# def save_user(**user):
#     print(user)
#     print(user["name"])

# save_user(id=1, name="Ky", age=22)


#Global variables by the same name in a method typically default to a local variable. But you can refer to the global variable by using the global keyword.
message ="a"
non_global = "ZZZ"
def greet(name):
    global message
    message = "b"
    non_global = "ho"


greet("Ontan")
print(message)
print(non_global)