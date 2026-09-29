while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    while True:
        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Result =", num1 + num2)

        elif choice == "2":
            print("Result =", num1 - num2)

        elif choice == "3":
            print("Result =", num1 * num2)

        elif choice == "4":
            if num2 != 0:
                print("Result =", num1 / num2)
            else:
                print("Cannot divide by zero.")

        else:
            print("Invalid choice.")

        again = input("\nDo you want to perform another calculation on these numbers? (yes/no): ")

        if again.lower() != "yes":
            break

    new_numbers = input("\nDo you want to enter new numbers? (yes/no): ")

    if new_numbers.lower() != "yes":
        print("Calculator closed.")
        break