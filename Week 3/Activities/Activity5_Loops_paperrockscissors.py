import random
print("Let's play Rock, paper or scissors")
Game = ["r","p","s"]
Computer_choice = random.choice(Game)
User_choice = input("Choose r for rock, p for paper or s for scissors: ")
if (Computer_choice == "r") and (User_choice == "s"):
    print("The computer choose " + Computer_choice + " so he wins, you choose " + User_choice)
elif(Computer_choice == "p") and (User_choice == "s"):
    print("You win, the computer choose " + Computer_choice)
elif (Computer_choice == "s") and (User_choice == "p"):
    print("The computer choose " + Computer_choice + " so he wins, you choose " + User_choice)
elif (Computer_choice == "s") and (User_choice == "r"):
    print("The computer choose " + Computer_choice + " so he wins, you choose " + User_choice)
elif(Computer_choice == "p") and (User_choice == "r"):
    print("You win, the computer choose " + Computer_choice)
elif (Computer_choice == "r") and (User_choice == "p"):
    print("The computer choose " + Computer_choice + " so he wins, you choose " + User_choice)
else: 
    print("You are tied both choose " + User_choice)