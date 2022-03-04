import random  # mport random library to create random number

# Setup variables
runagain = "y"
bestscore = 0
# Start game loop
while runagain == "y":
    # Setup variables after runagain
    num1 = 0
    num2 = 300
    num = random.randint(num1, num2)
    guess = None  # initialise guess as blank variable so line 17 condition will run
    guesses = 0
    # Give instructions to user
    print("Welcome to the Number Guessing Game")
    print(f"I'll think of a number between {num1} and {num2}")
    print("And you try and guess in as few guesses as possible.")
    while guess != num:
        guess = int(input("Enter your guess: "))
        if guess == num:
            guesses += 1
            break
        elif guess < num:
            guesses += 1
            print("Too low")
        elif guess > num:
            guesses += 1
            print("Too high")
    print(f"Congratulations. You took {guesses} guesses to guess the number {num}.")
    if bestscore == 0 or guesses < bestscore:
        bestscore = guesses
    print(f"Your best score is {bestscore}.")
    runagain = input("Would you like to play again? (y/n) ").lower()
print(f"Thanks for playing. Your best score was {bestscore}.")
