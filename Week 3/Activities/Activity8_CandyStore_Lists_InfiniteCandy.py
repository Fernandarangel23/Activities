# The list of candies to print to the screen
candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish","Skittles", "Hershey Bar", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
allowance = True

# The list used to store all of the candies selected inside of
candyCart = []

# Print out options
for i in range(len(candyList)):
    print("[" + str(i) + "] " + candyList[i])

#Ask for candies
while allowance:
    userCandy = int(input("Choose your candie or type (9) to end: "))
    if userCandy == 9:
        allowance = False
    elif int(userCandy) > -1 and int(userCandy) <9:
        candyCart.append(userCandy)
    

print("This is the list of candies you chose:")
for i in candyCart:
    print(candyList[i])