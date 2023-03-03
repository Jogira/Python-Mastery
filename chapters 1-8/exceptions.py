# # Handling exceptions.
# try:
#     with open("exceptions.py") as file:
#         print("File opened.")
#         # file.__exit__ #Supports context management protocol.
#     age = int(input("Age: "))
#     xfactor = 10/age
# except (ZeroDivisionError, ValueError) as ex:
#     print("You didn't enter a valid age.")
#     print(ex)
# else:
#     print("No exceptions were thrown.")
#     print("Execution continues.")
# # finally: #This can be replaced with the "with open(x) as file" statement
# #     file.close()

from timeit import timeit
code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
    #print(error)
"""


code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age
xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""

print("first code=", timeit(code1, number=10000))
print("second code=", timeit(code2, number=10000))
# Exceptions are costly. Try to avoid them when you can in applications where time is important.
