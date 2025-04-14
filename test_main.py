# test_main.py
import unittest
from unittest.mock import patch, call

# Assuming your game code is in 'main.py'
import main

class TestGuessGame(unittest.TestCase):

    # --- Tests for get_target_number ---

    @patch('random.randrange') # Mock the random.randrange function
    def test_get_target_number_mocked(self, mock_randrange):
        """Test if get_target_number calls random.randrange correctly."""
        mock_randrange.return_value = 50 # Set a predictable return value
        target = main.get_target_number()
        # Check if called with the constants and the +1 for inclusive range
        mock_randrange.assert_called_once_with(main.MIN_NUMBER, main.MAX_NUMBER + 1)
        self.assertEqual(target, 50) # Check if it returned the mocked value

    def test_get_target_number_range(self):
        """Test if get_target_number returns a number within the expected range."""
        for _ in range(100): # Run multiple times for better confidence
            target = main.get_target_number()
            self.assertGreaterEqual(target, main.MIN_NUMBER)
            self.assertLessEqual(target, main.MAX_NUMBER) # randrange(min, max+1) is inclusive

    # --- Tests for get_guess_number ---

    @patch('builtins.input', side_effect=['50']) # Mock input to return '50'
    def test_get_guess_number_valid(self, mock_input):
        """Test get_guess_number with valid input."""
        guess = main.get_guess_number()
        self.assertEqual(guess, 50)
        # Check the prompt using constants
        expected_prompt = f"Please enter your guess number(Should be a number between {main.MIN_NUMBER} - {main.MAX_NUMBER}): "
        mock_input.assert_called_once_with(expected_prompt)

    @patch('builtins.input', side_effect=['abc', '75']) # Mock input: invalid then valid
    @patch('builtins.print') # Mock print to check error messages
    def test_get_guess_number_invalid_then_valid(self, mock_print, mock_input):
        """Test get_guess_number with initial invalid (non-integer) input."""
        guess = main.get_guess_number()
        self.assertEqual(guess, 75)
        self.assertEqual(mock_input.call_count, 2)
        # Check the specific integer error message using constants
        expected_msg = f"Invalid number, please enter a integer between {main.MIN_NUMBER} - {main.MAX_NUMBER}."
        mock_print.assert_called_once_with(expected_msg)

    @patch('builtins.input', side_effect=['0', '101', '25']) # Mock input: out of range twice, then valid
    @patch('builtins.print') # Mock print
    def test_get_guess_number_out_of_range_then_valid(self, mock_print, mock_input):
        """Test get_guess_number with out-of-range input."""
        guess = main.get_guess_number()
        self.assertEqual(guess, 25)
        self.assertEqual(mock_input.call_count, 3)
        # Check that the correct range error messages were printed
        expected_msg = f"The number is out of range ( {main.MIN_NUMBER} - {main.MAX_NUMBER} )."
        expected_calls = [
            call(expected_msg), # First out-of-range input '0'
            call(expected_msg)  # Second out-of-range input '101'
        ]
        # Use assert_has_calls to check for specific calls in order (among potentially others)
        # Or check call_args_list directly if you want to be exact about *only* these calls
        self.assertEqual(mock_print.call_count, 2) # Ensure only two prints happened
        mock_print.assert_has_calls(expected_calls)


    # --- Tests for check_guess_number ---

    @patch('builtins.print') # Mock print to check output
    def test_check_guess_number_correct(self, mock_print):
        """Test check_guess_number when the guess is correct."""
        target = 50
        guess = 50
        result = main.check_guess_number(guess_number=guess, target_number=target)
        self.assertTrue(result)
        # Check that the congratulations message is printed
        expected_msg = f"Congratulations! You got it! {guess} is the target number!"
        mock_print.assert_called_once_with(expected_msg)

    @patch('builtins.print')
    def test_check_guess_number_too_high(self, mock_print):
        """Test check_guess_number when the guess is too high."""
        result = main.check_guess_number(guess_number=75, target_number=50)
        self.assertFalse(result)
        mock_print.assert_called_once_with('Guess number was too high')

    @patch('builtins.print')
    def test_check_guess_number_too_low(self, mock_print):
        """Test check_guess_number when the guess is too low."""
        result = main.check_guess_number(guess_number=25, target_number=50)
        self.assertFalse(result)
        mock_print.assert_called_once_with('Guess number was too low')

# --- How to run the tests ---
# Save this code as test_main.py in the same directory as main.py
# Run from your terminal: python -m unittest test_main.py

if __name__ == '__main__':
    unittest.main()
