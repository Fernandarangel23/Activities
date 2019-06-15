# Collects the user's and neighbors
myname = input("What is your name? ")
neighbor = input("What is your neighbor's name?")

# Collects the user's input for the prompt "How old are you?" and converts the string to an integer.
months = int(input("How many months you have been coding?"))
nighbormonths = int(input("How many months your neighbor has been coding?"))

totalmonths = months + nighbormonths

# print names and total of age
print(myname + " and " + neighbor + " have been coding for " + str(totalmonths) + " months.")
