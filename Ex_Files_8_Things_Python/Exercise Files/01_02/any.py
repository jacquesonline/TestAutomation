# def contains_digit(input_str):
#     for char in input_str:
#         if char.isdigit():
#             return True
#     return False

def contains_digit(input_str):
    return any(
        char.isdigit()
        for char in input_str
    )


# import string

# print(f"Punctuations are any of the following: {string.punctuation}")

# def contains_punctuation(input_str):
#     ''' Return True if the input_str contains punctuations.
#     Return False otherwise'''
#     return any(
#         val in string.punctuation
#         for val in input_str
#     )
#     pass # Replace this line with your solution

assert contains_digit('This sentence does not contain any digits') == False
assert contains_digit('But th15 0ne d0e5') == True
assert contains_digit('123-456-7890') == True
print('Passed all tests ...')
