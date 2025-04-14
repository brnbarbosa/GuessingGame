# Guess game project.

import random

MIN_NUMBER = 1
MAX_NUMBER = 100

def main() -> None:
    target_number = get_target_number()
    guess_number = get_guess_number()
    
    while not check_guess_number(guess_number, target_number):
        guess_number = get_guess_number()


# Function that returns the random target number.
def get_target_number() -> int:
    return random.randrange(MIN_NUMBER, MAX_NUMBER + 1)

# Function that get the user guess number.
# Guess number should be a positive integer between 1 - 100.
# Repeat until get a possible estimated number.
def get_guess_number() -> int:
    guess_number : int = 0

    prompt = f"Please enter your guess number(Should be a number between {MIN_NUMBER} - {MAX_NUMBER}): "
    integer_error_msg = f"Invalid number, please enter a integer between {MIN_NUMBER} - {MAX_NUMBER}."
    range_error_msg = f"The number is out of range ( {MIN_NUMBER} - {MAX_NUMBER} )."

    while True:
        try:
            guess_number_str = input(prompt)
            guess_number = int(guess_number_str)
                
            if guess_number < MIN_NUMBER or guess_number > MAX_NUMBER:
                raise ValueError(range_error_msg)
            else:
                return guess_number
        except ValueError as e:
            if str(e) == range_error_msg:
                print(str(e))
            else:
                print(integer_error_msg)


# Function that check if the player had guessed write or if the guess is lower or greater than the target number.
def check_guess_number(guess_number : int, target_number :  int) -> bool:
    if guess_number == target_number:
        print(f"Congratulations! You got it! {guess_number} is the target number!")
        return True
    elif guess_number > target_number:
        print('Guess number was too high')
        return False
    elif guess_number < target_number:
        print('Guess number was too low')
        return False

if __name__ == "__main__":
    main()