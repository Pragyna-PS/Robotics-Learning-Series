import random as r

# input by the user.
over = int(input("\nEnter the number of overs you want to play: "))
computer_score = r.randint(1,over*36)
print(f"\nComputer has scored {computer_score} runs. Your target is {computer_score+1} runs.")

# playing with the user.
def find_user_score(over,computer_score):
    user_score = 0
    for i in range(over):
        for j in range(6):
            if user_score <= computer_score:
                print(f"\nOver {i+1} : Ball {j+1}:-")
                bat = int(input("Enter any number to bat: "))
                while bat not in range(1,7):
                    bat = int(input("Enter any number to bat(1-6): "))
                computer_number = r.randint(1,6)
                print(f"Computer’s number: {computer_number}")
                if bat == computer_number:
                    print(f"Total Runs:{user_score}")
                    print("\nOops! you are Out.")
                    break
                else:
                    user_score += bat
                    print(f"Total Runs: {user_score}")
            else:
                break
        if bat == computer_number or user_score > computer_score:
            break
    return user_score

user_score = find_user_score(over,computer_score)

# declaring the winner.
if user_score > computer_score:
    print("\n Congratulations! You Won the game.")
elif user_score < computer_score:
    print("\nComputer Won the game.")
else:
    print("\nThe match is draw.")