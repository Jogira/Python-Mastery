"""
Using autoformatter.
"""
X = 1
Y = 2
UNIT_PRICE = 3

# Can use triple quotes to do very large strings with line breaks.
BLOB_TEXT = """
I can type so much without
having to use separate lines variables.
And it's a 
lot
cleaner to read.
"""

# print(BLOB_TEXT)
# print(BLOB_TEXT[5:])
# print(BLOB_TEXT[5:10])
# print(BLOB_TEXT[:10])

# ESCAPE_CHARACTER = "Python \"Programming"
# print(ESCAPE_CHARACTER)

FIRST ="Jack-o"
LAST ="Valentine"
FULL = f"{FIRST} {LAST}" #Example of string formatting.
print(FULL)

USER_INPUT  = input("x: ")
RESULT = int(USER_INPUT) + 1
print(RESULT)
