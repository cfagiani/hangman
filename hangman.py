import random

from graphics import *

WIN_HEIGHT = 900
WIN_WIDTH = 900
BLANK_WIDTH = 20
PADDING = 10

NUM_GUESSES = 8

SECRET_WORDS = ["spaceship", "bananas", "architect", "hockey", "picture", "literature", "library", "automobile",
                "airplane", "bumblebee", "dictionary", "xylophone", "piano", "potato", "broccoli", "weather"]


def main():
    win = GraphWin("Hangman", WIN_HEIGHT, WIN_WIDTH)
    win.setBackground("white")
    used_letters = []
    secret_word = get_secret_word()
    current_word = "_" * len(secret_word)
    incorrect_count = 0
    while not is_winner(current_word) and not is_dead(incorrect_count):
        draw_hangman(incorrect_count, win)
        draw_word(current_word, win)
        draw_used(used_letters, win)
        guess = prompt_for_guess(win)
        while not is_valid_guess(guess, used_letters):
            guess = prompt_for_guess(win)
        # now we have a valid guess
        guess = guess.lower()
        used_letters += guess
        matching_positions = get_indexes(guess, secret_word)
        if len(matching_positions) == 0:
            incorrect_count += 1
        current_word = update_current_word(current_word, matching_positions, guess)
        time.sleep(.1)
    draw_word(current_word, win)
    draw_used(used_letters, win)
    show_result(is_winner(current_word), win)
    win.getKey()  # wait for key
    win.close()  # Close window when done


def get_secret_word():
    return random.choice(SECRET_WORDS)


def show_result(did_win, window):
    text = "YOU WIN"
    if not did_win:
        text = "YOU LOSE"
    t = Text(Point(WIN_WIDTH / 2, WIN_HEIGHT / 2), text)
    t.setSize(36)
    t.setStyle("bold")
    t.setTextColor("red")
    t.draw(window)


def update_current_word(current_word, positions, guess):
    char_list = list(current_word)
    for pos in positions:
        char_list[pos] = guess
    return ''.join(char_list)


def get_indexes(guess, secret_word):
    indexes = []
    for i in range(len(secret_word)):
        if guess == secret_word[i]:
            indexes.append(i)
    return indexes


def is_valid_guess(guess, used_letters):
    """
    This function takes 2 inputs: guess (a string containing 1 character) and an array of used letters. It returns
    True if the guess is NOT in the used_letter array (ignores upper/lower case) and is a letter a-z.
    :param guess:
    :param used_letters:
    :return:
    """
    lower_letter = guess.strip().lower()
    if lower_letter == 'escape':
        sys.exit(0)
    if len(lower_letter) > 1:
        return False
    return is_letter(lower_letter) and lower_letter not in used_letters


def is_letter(character):
    code = ord(character)
    return 97 <= code <= 122


def draw_hangman(incorrect_guesses, window):
    """
    Draws the hangman and the gallows based on the number of incorrect guesses.
    :param incorrect_guesses:
    :param window:
    :return:
    """
    # first, draw the gallows
    gallows_base_y = WIN_HEIGHT - (WIN_HEIGHT / 3)
    gallows_base_x = WIN_WIDTH - (WIN_WIDTH / 3)
    gallows_top = WIN_HEIGHT / 18
    gallows_base_width = WIN_WIDTH / 4
    head_radius = WIN_HEIGHT / 20
    rope_bottom = gallows_top + 20
    hangman_center_x = gallows_base_x - gallows_base_width
    body_top = rope_bottom + (2 * head_radius)
    body_length = head_radius * 4
    limb_length = body_length / 2
    Line(Point(gallows_base_x - (gallows_base_width / 2), gallows_base_y),
         Point(gallows_base_x + (gallows_base_width / 2), gallows_base_y)).draw(window)
    Line(Point(gallows_base_x - (gallows_base_width / 2), gallows_base_y),
         Point(gallows_base_x + (gallows_base_width / 2), gallows_base_y)).draw(window)
    Line(Point(gallows_base_x, gallows_base_y),
         Point(gallows_base_x, gallows_top)).draw(window)
    Line(Point(gallows_base_x, gallows_top),
         Point(hangman_center_x, gallows_top)).draw(window)
    Line(Point(hangman_center_x, gallows_top),
         Point(hangman_center_x, rope_bottom)).draw(window)
    if incorrect_guesses > 0:
        Circle(Point(hangman_center_x, rope_bottom + head_radius), head_radius).draw(window)
    if incorrect_guesses > 1:
        Line(Point(hangman_center_x, body_top),
             Point(hangman_center_x, body_top + body_length)).draw(window)
    if incorrect_guesses > 2:
        Line(Point(hangman_center_x, body_top + head_radius),
             Point(hangman_center_x - limb_length, body_top - head_radius)).draw(window)
    if incorrect_guesses > 3:
        Line(Point(hangman_center_x, body_top + head_radius),
             Point(hangman_center_x + limb_length, body_top - head_radius)).draw(window)
    if incorrect_guesses > 4:
        Line(Point(hangman_center_x, body_top + body_length),
             Point(hangman_center_x + limb_length, body_top + body_length + limb_length)).draw(window)
    if incorrect_guesses > 5:
        Line(Point(hangman_center_x, body_top + body_length),
             Point(hangman_center_x - limb_length, body_top + body_length + limb_length)).draw(window)
    if incorrect_guesses > 6:
        Circle(Point(hangman_center_x - head_radius / 3, rope_bottom + head_radius / 2), head_radius / 10).draw(window)
        Circle(Point(hangman_center_x + head_radius / 3, rope_bottom + head_radius / 2), head_radius / 10).draw(window)
    if incorrect_guesses > 7:
        Oval(Point(hangman_center_x - head_radius / 3, rope_bottom + head_radius * 1.5),
             Point(hangman_center_x + head_radius / 3, rope_bottom + head_radius * 1.75)).draw(window)


def draw_word(current_word, window):
    total_width = len(current_word) * BLANK_WIDTH + (len(current_word) - 1) * PADDING
    cur_x = (WIN_WIDTH - total_width) / 2
    for val in current_word:
        t = Text(Point(cur_x, WIN_HEIGHT - WIN_HEIGHT / 4), val)
        t.setSize(36)
        t.draw(window)
        cur_x += BLANK_WIDTH + PADDING


def prompt_for_guess(window):
    guess_y = WIN_HEIGHT - WIN_HEIGHT / 5
    t = Text(Point(PADDING * 7, guess_y), "Enter a guess")
    t.setSize(24)
    t.draw(window)
    return window.getKey()


def draw_used(used_letters, window):
    t = Text(Point(PADDING * 3, WIN_HEIGHT - WIN_HEIGHT / 7), "Used:")
    t.setSize(24)
    t.draw(window)
    cur_x = PADDING * 2
    for val in used_letters:
        t = Text(Point(cur_x, WIN_HEIGHT - WIN_HEIGHT / 9), val)
        t.setSize(20)
        t.draw(window)
        cur_x += BLANK_WIDTH + PADDING


def is_dead(incorrect_count):
    return incorrect_count >= NUM_GUESSES


def is_winner(current_word):
    return "_" not in current_word


# Code that is not enclosed in a function is run when this file is run via the command line or when it is imported
# into another module
main()
