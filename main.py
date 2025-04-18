# Guess game project.

import random
import varibales_prompts

def main() -> None:
    target_number = get_target_number()

    print(varibales_prompts.game_intro)
    guess_number = get_guess_number()
    
    while not check_guess_number(guess_number, target_number):
        guess_number = get_guess_number()


# Create random target number.
def get_target_number() -> int:
    return random.randrange(varibales_prompts.MIN_NUMBER, varibales_prompts.MAX_NUMBER + 1)

# Get the user guess number.
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


# Check if the player had guessed write or if the guess is lower or greater than the target number.
def check_guess_number(guess_number : int, target_number :  int) -> bool:
    if guess_number == target_number:
        print(varibales_prompts.congrats)
        play_again()
    elif guess_number > target_number:
        print(varibales_prompts.high)
        return False
    elif guess_number < target_number:
        print(varibales_prompts.low)
        return False
    
# Prompt to check if the player want to start new game.
def play_again():
    while True:
        try:
            play_again_answer = input(varibales_prompts.play_again)
            if play_again_answer.lower() == 'n':
                quit()
            elif play_again_answer.lower() == 'y':
                main()
            else:
                raise ValueError(varibales_prompts.play_again_error)
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()