import random


def guess_the_number():
    print("Welcome to 'Guess the Number'!")
    print("I have selected a number between 1 and 100. Can you guess what it is?")

    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(
                    f"Congratulations! You've guessed the correct number {number_to_guess} in {attempts} attempts."
                )
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    guess_the_number()
