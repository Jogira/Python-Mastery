# letters = ["a", "b", "c"]  # List
# matrix = [[0, 1], [2, 3]]  # List made of lists.
# zeros = [0] * 5  # Fast way of repeating value.
# print(zeros)
# # List can be mashed together easily like this.
# combined = zeros + letters
# print(combined)

# numbers = list(range(1, 21))  # Shorthand for list of numbers from 0 to 20.
# print(numbers)
# print(numbers[::-1])  # Returns list reversed.

# numbers_list = [1, 2, 3, 4, 10, 12, 18, 21]
# first, second, third = numbers_list
# LIST PACKING
# first, second, *other = numbers_list #Adding the asertisk relegates the rest of the list to a separate list variable.
# # These are the same.
# first = numbers_list[0]
# second = numbers_list[1]
# third = numbers_list[2]

# print(first)
# print(other)

# letras = ["h","e","j","a"]
# for index, letra in enumerate(letras):
#     # print(letra)
#     # print(letra[0], letra[1])
#     print(index, letra)

# del letras[0:2] #Delete list elements via index.
# print(letras)
# letras.clear() #Clear entire list.
# print(letras)

# items = [
#     ("Prod1", 100),
#     ("Prod2", 12),
#     ("Prod3", 15),
# ]
# items.sort()
# #Python won't know how to sort this list, so we have to define a sort method.
# def sort_item(item):
#     return item[1]

# # items.sort(key=sort_item)
# items.sort(key=lambda item: item[1]) #Lambda expression which is the same as passing in a method such as in the line above.
# print(items)

# prices = []
# for item in items:
#     prices.append(item[1])
# print(prices)
# #THIS CAN BE SHRUNK INTO A MAP STATEMENT
# mapped_prices = map(lambda item: item[1], items)
# for item in mapped_prices:
#     print(item)
# #WE CAN JUST CONVERT IT TO A LIST AND AVOID HAVING TO ITERATE.
# # list_prices = list(map(lambda item: item[1], items))
# list_prices = [item[1] for item in items] #List comprehension.
# print("Converted to lists", list_prices)

# # filtered_list = list(filter(lambda item: item[1] >= 20, items))
# filtered_list = [item for item in items if item[1] >= 20] #List comprehension version of the previous line.
# print(filtered_list)


# #Zip function
# print(list(zip("xyz",list1,list2)))

# from collections import deque
# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.popleft()
# print(queue)

# # Tuples
# point = (1, 2) + (3, 4)
# point = tuple([1, 2])  # Lists can be converted to tuples like this.
# # point = () #Empty tuple
# print(point[0:2])
# x, y = point
# print(x)
# print(y)
# if 10 in point:
#     print("exists")

# # Bad way of swapping variables.
# x = 10
# y = 11
# z = x
# y = z
# print("x", x)
# print("y", y)
# # Good way of swapping vars.
# a = 20
# b = 30
# a, b = b, a
# print("a", a)
# print("b", b)


# #Arrays are faster than lists but must be all the same type.
# #
# from array import array
# numbers = array("i", [1,2,3])
# numbers[0] = 1.0 #Will error out since the array is for ints.

# numbers =[1,1,2,3,4]
# first = set(numbers)
# second = {1,4}
# # second.add(5)
# # second.remove(5)
# # len(second)
# # print(uniques)

# #Sets do not have indices, so they cannot be accessed via a specific slot.
# print(first | second) #Union of both sets.
# print(first & second) #Only number sin both sets.
# print(first - second) #Takes the first set and removes any numbers in it that are duplicate in the second set.
# print(first ^ second) #Elements that are either in the first or second set, but not both.

# if 1 in first:
#     print("Yes, 1 is found")

# DICTIONARY

# point = {"x": 1, "y": 2}
# point = dict(x=1, y=2)
# point["x"] = 10
# point["z"] = 20
# print(point)
# if "a" in point:
#     print(point)
# print(point.get("a", 0))
# del point["x"]
# print(point)


# for key in point:
#     print(key, point[key])
# # These both work the same.
# for key, value in point.items():
#     print(key, value)


# #Dictionary Comprehensions
# values = []
# for x in range(5):
#     values.append(x*2)
# #THESE LINES PERFORM THE SAME FUNCTION.
# values = {x * 2 for x in range(5)} #BUT THIS IS A SET COMPREHENSION.
# dict_values = {x: x * 2 for x in range(5)} #BUT THIS IS A DICTIONARY COMPREHENSION.

# print(values)
# print(dict_values)


# from sys import getsizeof
# values = (x * 2 for x in range(100000)) #Generator object that doesn't store everything in memory,
# # so much more efficient. Generators have no length since it keeps no memory of previously iterated values.
# print(getsizeof(values))
# # for x in values:
# #     print(x)
# values = [x * 2 for x in range(100000)] #Notice how this list comprehension uses a LOT more memory.
# print(getsizeof(values))

# numbers = [1, 2, 3]
# # What if we want to unpack the numbers to get the individual values?
# print(*numbers)

# values = list(range(5))
# values = [*range(5), *"Hello"]  # Here we unpack both numbers 1-5 and hello.
# print(values)


# first = [1, 2]
# second = [3]
# mixed_lists = [*first, "a", *second, *"Hello"]
# print(mixed_lists)

# first = {"x":1}
# second ={"x": 10, "y":2}
# combined = {**first, **second, "z":1}
# print(combined)

#Find out what character is repeated the most.

sentence ="This is a common interview question"
char_dict = {}
for char in sentence:
    if char not in char_dict:
        char_dict[char] = 1
    else:
        char_dict[char] += 1
print(max(char_dict, key=char_dict.get), char_dict[max(char_dict, key=char_dict.get)])