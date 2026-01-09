import random

secret_number = random.randint(1, 50)
attempts = 10

print("""
Welcome to the Number Guessing Game!
Guess a number between 1 and 50.
You have 10 chances.
""")

for attempt in range(1, attempts + 1):
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess == secret_number:
        print(f"Congratulations! You guessed the number in {attempt} attempts.")
        break
    elif guess < secret_number:
        print("Try higher.")
    else:
        print("Try lower.")

    print(f"Chances left: {attempts - attempt}")

else:
    print(f"You lost! The number was {secret_number}.")

