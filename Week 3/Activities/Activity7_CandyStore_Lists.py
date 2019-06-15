Inventory = ["Snickers", "Tamborines","Pulparindo","Papas","Gudupop","Winnis","Crunch","Hershey's","Milky Way","Ricaleta","Pelón Pelo Rico","Miguelito"]
allowance = 5
Cart = []

# The list used to store all of the candies selected inside of
candyCart = []

# Print out options
for i in range(len(Inventory)):
    print("[" + str(i) + "] " + Inventory[i])


#Ask for candies
while allowance > 0:
    userCandy = int(input("Choose your candie: "))
    if userCandy > -1 and userCandy <9:
        Cart.append(userCandy)
        allowance -= 1

print("This is the list of candies you chose:")
for i in Cart:
    print(Inventory[i])