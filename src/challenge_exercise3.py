import random
secret_number = random.randint(1, 100)
count = 0
again = True
while again:
    print("Welcome to Number Guessing Game!")
    guess = int(input("Guess a number between 1 and 100: "))
    while guess < 1 or guess > 100:
        print("Invalid guess. Please enter a number between 1 and 100.")
        guess = int(input("Guess a number between 1 and 100: "))
    while guess != secret_number:
        count += 1
        if guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
        guess = int(input("Guess a number between 1 and 100: "))

    print(f"You won in {count} attempts!")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        secret_number = random.randint(1, 100)
        count = 0
    else:
        again = False
