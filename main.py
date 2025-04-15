# Guess game project.

import random
import varibales_prompts

def main() -> None:
    target_number = get_target_number()

    print(varibales_prompts.game_intro)
    guess_number = get_guess_number()
    
    while not check_guess_number(guess_number, target_number):
        guess_number = get_guess_number()


# Function that returns the random target number.
def get_target_number() -> int:
    return random.randrange(varibales_prompts.MIN_NUMBER, varibales_prompts.MAX_NUMBER + 1)

# Function that get the user guess number.
# Guess number should be a positive integer between 1 - 100.
# Repeat until get a possible estimated number.
def get_guess_number() -> int:
    guess_number : int = 0

    while True:
        try:
            guess_number_str = input(varibales_prompts.prompt)
            guess_number = int(guess_number_str)
                
            if guess_number < varibales_prompts.MIN_NUMBER or guess_number > varibales_prompts.MAX_NUMBER:
                raise ValueError(varibales_prompts.range_error_msg)
            else:
                return guess_number
        except ValueError as e:
            if str(e) == varibales_prompts.range_error_msg:
                print(str(e))
            else:
                print(varibales_prompts.integer_error_msg)


# Function that check if the player had guessed write or if the guess is lower or greater than the target number.
def check_guess_number(guess_number : int, target_number :  int) -> bool:
    if guess_number == target_number:
        print(varibales_prompts.congrats)
        return True
    elif guess_number > target_number:
        print(varibales_prompts.high)
        return False
    elif guess_number < target_number:
        print(varibales_prompts.low)
        return False

if __name__ == "__main__":
    main()