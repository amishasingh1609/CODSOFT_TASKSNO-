import random

user_score = 0
computer_score = 0

while True:
    print("\n--- ROCK PAPER SCISSORS ---")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "4":
        print("\nGame Over!")
        print("Final Score:")
        print("You:", user_score)
        print("Computer:", computer_score)
        break

    choices = ["rock", "paper", "scissors"]

    if choice == "1":
        user = "rock"
    elif choice == "2":
        user = "paper"
    elif choice == "3":
        user = "scissors"
    else:
        print("Invalid choice!")
        continue

    computer = random.choice(choices)

    print("\nYour choice:", user)
    print("Computer choice:", computer)

    if user == computer:
        print("It's a Tie!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        print("You Win!")
        user_score += 1

    else:
        print("You Lose!")
        computer_score += 1

    print("Score -> You:", user_score, "| Computer:", computer_score)

    again = input("\nDo you want to play another round? (yes/no): ")

    if again.lower() != "yes":
        print("\nGame Over!")
        print("Final Score:")
        print("You:", user_score)
        print("Computer:", computer_score)
        break