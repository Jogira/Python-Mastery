import random
import string

print(random.random())
print(random.randint(1,10))
print(random.choice([1,2,9,84,11,8,8]))
print(random.choices([1,2,9,84,11,8,8], k=2))
print("".join(random.choices(string.ascii_letters + string.digits, k=4)))
print(string.ascii_letters)

numbers = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(numbers)
print(numbers)