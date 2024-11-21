import random

print("Number Guessing Game")

number = random.randint(1, 100)
attempt_count = 0

while True:
    attempt_count += 1
    guess = int(input("Guess the number: "))

    if guess == number:
        print(f"That's correct! You guessed it in {attempt_count} attempts!")
        break
    elif guess > number:
        print("Your guess is too high!")
    else:
        print("Your guess is too low!")