import random
import string

while True:
    print("\n--- PASSWORD GENERATOR ---")

    length = int(input("Enter password length: "))

    print("\nChoose password complexity:")
    print("1. Letters only")
    print("2. Letters + Numbers")
    print("3. Letters + Numbers + Special Characters")

    choice = input("Enter your choice: ")

    if choice == "1":
        characters = string.ascii_letters

    elif choice == "2":
        characters = string.ascii_letters + string.digits

    elif choice == "3":
        characters = string.ascii_letters + string.digits + string.punctuation

    else:
        print("Invalid choice!")
        continue

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\nGenerated Password:", password)

    again = input("\nDo you want to generate another password? (yes/no): ")

    if again.lower() != "yes":
        print("Password Generator closed.")
        break