from display_and_feedback import display_game_status
from display_and_feedback import show_win_message
from display_and_feedback import show_lose_message
from game_function.input_and_validations import get_valid_guess
from game_state import is_game_over
from game_state import check_win_condition
from game_state import check_lose_condition
from word_list import randomizer, word_of_game
letters_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
def start ():
    randomizer()
    word = word_of_game()
    return word
def round(hidden_letters:set, attempts_remaining:int,guessed_letters:set ):
    while is_game_over(hidden_letters, attempts_remaining) is False:
        get_valid_guess(guessed_letters)
        display_game_status(letters_alphabet, guessed_letters, hidden_word, attempts_remaining)

if __name__ == "__main__":
    ...