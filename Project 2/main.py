from random import randint

n = randint(1, 100)
a = -1
guesses = 0

while a != n:
    guesses += 1
    a = int(input("Guess a number between 1 - 100: "))

    if a > n:
        print("Lower number please...")
    elif a < n:
        print("Higher number please...")

print(f"You have guessed the correct number {n} in {guesses} attempts 🎉")