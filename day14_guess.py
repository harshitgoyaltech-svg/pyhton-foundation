import random
secret = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == secret:
    print("Congratulations! You guessed the number.")
elif guess < secret:
    print("Too low! The secret number was:", secret)
else:
    print("Too high! The secret number was:", secret)