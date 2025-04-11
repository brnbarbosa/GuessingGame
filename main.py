# Guess game project.
def main():
    guess_number = get_guess_number()
    print(guess_number)

# Function that returns the random target number.
def getting_target_number(seed):
    pass

# Function that get the user guess number.
# Guess number should be a positive integer between 1 - 100.
# Repeat until get a possible estimated number.
def get_guess_number():
    guess_number : int = 0

    while True:
        try:
            guess_number_str = int(input("Please enter your guess number(Should be a number between 1 - 100): "))
            guess_number = int(guess_number_str)

            if guess_number < 1 or guess_number > 100:
                raise Exception("The number is out of range ( 1 - 100 ).")
            else:
                return guess_number
        except ValueError:
            print("Invalid number, please enter a integer between 1 - 100.")
        except Exception as range:
            print(range)


# Function that check if the player had guessed write or if the guess is lower or greater than the target number.
def check_guess_number(guess_number : int, target_number :  int):
    pass

if __name__ == "__main__":
    main()