import sys
sys.path.append(".")
from display_and_feedback import display_game_status
from display_and_feedback import show_win_message
from display_and_feedback import show_lose_message
from game_logic import update_guessed_letters, check_letter_in_word, \
    get_hidden_word_with_visible_guessed_letters, alphabet_display_with_guessed_letters_marked
from game_setup import initialize_secret_word_display
from input_and_validations import get_valid_guess
from game_state import is_game_over
from game_state import check_win_condition
from game_state import check_lose_condition
from word_list import full_game_data

letters_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y", "z"]


def main():
    word = full_game_data()
    game_word = initialize_secret_word_display(word)
    hidden_letters = set(word)
    guessed_letters = set()
    attempts_remaining = 7
    incorrect_guesses = 0
    while not is_game_over(hidden_letters, attempts_remaining):
        display_game_status(incorrect_guesses, letters_alphabet,
                            guessed_letters,
                            word,
                            attempts_remaining
                            )
        letter = get_valid_guess(guessed_letters)
        update_guessed_letters(letter, guessed_letters)
        if check_letter_in_word(letter, word):
            print(f"{alphabet_display_with_guessed_letters_marked(letters_alphabet, guessed_letters)}\n{get_hidden_word_with_visible_guessed_letters(game_word,guessed_letters)}")


        else:
            attempts_remaining -= 1
            incorrect_guesses += 1
    if check_win_condition(hidden_letters):
        print(show_win_message(word))
    elif check_lose_condition(attempts_remaining):
        print(show_lose_message(word))


if __name__ == "__main__":
    main()
