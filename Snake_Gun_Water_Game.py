import numpy as np

def game_rules():
    print("Snake - S")
    print("Gun - G")
    print("Water - W")

def winner(user,computer):
    if (user == computer):
        return "It's a Draw!!"
    
    elif (
        (user == "S" and computer == "W") or
        (user == "G" and computer == "S") or
        (user == "W" and computer == "G")
    ):
        return "You Win!!"
    else:
        return "Computer Wins!!"
    
def game():
    options = ["S","G","W"]

    print("Welcome to Snake-Gun-Water Game..")
    game_rules()

    user = input("Enter Your Choice:-").upper()

    if user not in options:
        print("Invalid choice")
        return 
    

    computer = np.random.choice(options)

    print(f"You choose: {user}")
    print(f"computer choose: {computer}")

    result = winner(user, computer)
    print("\nResult:", result)


game()