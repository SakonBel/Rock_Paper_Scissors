import random
print("Welcome to Rock, Paper, Scissors game!!!\n")

computer_choice = random.choice(["R", "P", "S"])
your_choice = input("Please choose what you want(Rock=R, Paper=P, Scissors=S) : ").upper()

if your_choice == computer_choice:
    print(f"You choose : {your_choice} and computer choose : {computer_choice}")
    print("It's a draw!")
elif your_choice == "R":
    if computer_choice == "S":
        print(f"You choose : {your_choice} and computer choose : {computer_choice}")
        print("You win!!!")
    else:
        print(f"You choose : {your_choice} and computer choose : {computer_choice}")
        print("You lose!!!")
elif your_choice == "S":
    if computer_choice == "P":
        print(f"You choose : {your_choice} and computer choose : {computer_choice}")
        print("You win!!!")
    else:
        print(f"You choose : {your_choice} and computer choose : {computer_choice}")
        print("You lose!!!")
else:
    if computer_choice == "R":
        print(f"You choose : {your_choice} and computer choose : {computer_choice}")
        print("You win!!!")
    else:
        print(f"You choose : {your_choice} and computer choose : {computer_choice}")
        print("You lose!!!")


print("\nGame Over\nThank you for playing!")