MIN_NUMBER : int = 1
MAX_NUMBER : int = 100

game_intro : str = """Welcome to the Guessing Game!
(Created by Bruno Barbosa)

I'm thinking of a secret number between 1 and 100.
Can you figure it out?

Go ahead, enter your first guess!"""
prompt : str = f"Please enter your guess number(Should be a number between {MIN_NUMBER} - {MAX_NUMBER}): "
integer_error_msg : str = f"Invalid number, please enter a integer between {MIN_NUMBER} - {MAX_NUMBER}."
range_error_msg : str = f"The number is out of range ( {MIN_NUMBER} - {MAX_NUMBER} )."
congrats : str = "Congratulations! You got it!"
high : str = "Guess number was too high"
low : str = "Guess number was too low"
