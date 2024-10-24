import random 
name = input("Type Your Name: ")

print(f"Welcome, {name}")
print("Guess a number between 1-10")

number_to_guess = random.randint(1, 10)
guess = int(input("Enter your guess: "))

if guess == number_to_guess:
    print("Congratulations. You Guessed the Number! ")
elif guess > number_to_guess:
    print(f"Oh too high, the number was {number_to_guess}")
else:
    print(f"Oh too low, the number was {number_to_guess}")
