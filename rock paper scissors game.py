roimport random

user_score = 0
computer_score = 0

while True:
    print("\n--- ROCK PAPER SCISSORS ---")
    user = input("Choose rock, paper, or scissors: ").lower()

    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)

    print("Your choice:", user)
    print("Computer choice:", computer)

    if user not in choices:
        print("Invalid choice!")
    elif user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        print("You win!")
        user_score += 1
    else:
        print("You lose!")
        computer_score += 1

    print("Score - You:", user_score, "Computer:", computer_score)

    play = input("Play again? (yes/no): ").lower()

    if play != "yes":
        print("Game Over!")
        break