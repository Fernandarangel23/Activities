print("Welcome to the House of Pies! Here are our pies")
List=["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun", "Blueberry", "Buko", "Burek", "Tamale", "Steak"]
Cart []
allowance = "Yes"
while allowance == "Yes":
    print("---------------------------------------------------------------------")
    print("(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee,  (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek,  (9) Tamale, (10) Steak")
    selection = int(input("Please entre the number of the pie you want: ") -1)
    Cart.append(List[selection])
    allowance = input("Say Yes if you like more pies and not if you are ok: ")
    
print("You have ordered" + Cart