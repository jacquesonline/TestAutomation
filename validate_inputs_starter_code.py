import pyinputplus as pyip

print("\nEXAMPLE 1")

# uncomment the following line of code and fill in
result = pyip.inputInt("Number of bags:", min=0)

# uncomment the following line of code
print("\nYou will use", result, "store bags.")

print("\nEXAMPLE 2")

# uncomment the following line of code and fill in
result = pyip.inputMenu(["Red", "Blue", "Green"],
                        lettered=True, numbered=False)

# uncomment the following line of code
print("\nYou have chosen a", result, "marker.")

print("\nEXAMPLE 3")

# uncomment the following line of code and fill in
result = pyip.inputEmail("Email:")

# uncomment the following line of code
print("\nThe email you entered:", result)
