def number_guessing():
    print("Welcome to the Number Guessing Game!")

    numbers = [1, 3, 6, 9, 18, 7, 8]
    while True:
        target_number = int(input("Specify the number you want to guess: "))

        if target_number in numbers:
            print(f"The number {target_number} is correct.")
            break
        else:
            print(f"Sorry! The number {target_number} is not correct. Try again.")

number_guessing()
