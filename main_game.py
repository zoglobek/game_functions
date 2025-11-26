from display_and_feedback import display_game_status
from display_and_feedback import show_win_message
from display_and_feedback import show_lose_message
from game_function.game_logic import update_guessed_letters, check_letter_in_word, \
    get_hidden_word_with_visible_guessed_letters, alphabet_display_with_guessed_letters_marked
from game_function.game_setup import initialize_secret_word_display
from game_function.input_and_validations import get_valid_guess
from game_state import is_game_over
from game_state import check_win_condition
from game_state import check_lose_condition
from word_list import full_game_data
MAX_NUMBER_OF_GUESSES = 7


letters_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
def main():
    incorrect_guesses = 0
    attempts_remaining = MAX_NUMBER_OF_GUESSES - incorrect_guesses
    word = full_game_data()
    hidden_word = initialize_secret_word_display(word)
    hidden_letters = set(word)
    guessed_letters = set()
    while not is_game_over(hidden_letters, attempts_remaining):
        letter = get_valid_guess(guessed_letters)
        print(display_game_status(letters_alphabet,
                                  guessed_letters,
                                  hidden_word,
                                  attempts_remaining
                                  ))
        update_guessed_letters(letter, guessed_letters)
        if check_letter_in_word(letter, word):
            print(get_hidden_word_with_visible_guessed_letters(word, guessed_letters), "\n",alphabet_display_with_guessed_letters_marked(letters_alphabet, guessed_letters))

        else:
            incorrect_guesses += 1
            print(alphabet_display_with_guessed_letters_marked(letters_alphabet, guessed_letters),"\n", get_hidden_word_with_visible_guessed_letters(word, guessed_letters))



if __name__ == "__main__":
    main()
