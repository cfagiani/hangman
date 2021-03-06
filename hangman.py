from graphics import *

WIN_HEIGHT = 900
WIN_WIDTH = 900
BLANK_WIDTH = 20
PADDING = 10

NUM_GUESSES = 8


# TODO 0: Here are some terms that may help you understand:
# - character = a single letter or number (for instance 'a' or '9')

# - string = a series of characters. You represent this by enclosing it in quotes (for instance "this is a string")

# - boolean = a value that is either True or False

# - variable = a variable is just a name you give a value (like a number or a string). You can do a bunch of things with
# a variable like read it, assign to it (give it a value), and pass it to a function.

# - assignment = setting a variable equal to something

# - array = a list of multiple values of the same type. When you have a list, you can access individual members of the
# list using the "membership operator" which is written with square brackets []. For example, to access the first entry
# in a list called my_list, you'd write my_list[0].  The number inside the brackets is called the "index" of the array.
# in Python (and many other programming languages) list indexes start at 0, not 1.

# - function = a re-usable piece of code that can take inputs and may produce outputs. Functions have names and can be
# called by using its name followed by parenthesis. For instance this_is_a_function_call()
# To pass values to a function, include them inside the parenthesis. If a function returns values, you can use that
# to assign a variable. For instance: my_var = my_func(my_arg) will pass a variable called my_arg to a function called
# my_func and set the my_var variable to the value that is returned by the function.

def main():
    """
    This runs the main logic of the program. It should display the game window and then ask the user to make a guess.

    :return:
    """
    win = GraphWin("Hangman", WIN_HEIGHT, WIN_WIDTH)
    win.setBackground("white")
    # this array is used for keeping track of the letters that have already been guessed
    used_letters = []
    # secret_word is the word the user is going to have to guess
    secret_word = get_secret_word()

    # current_word is used to show blanks for any letters that have not been guessed yet.
    # a the beginning of the game, it is all blanks. By the end, it'll match secret_word (if the user won)
    current_word = "_" * len(secret_word)

    # incorrect_count is used to keep track of how many wrong answers the user has given.
    incorrect_count = 0
    while not is_winner(current_word) and not is_dead(incorrect_count):
        draw_hangman(incorrect_count, win)
        draw_word(current_word, win)
        draw_used(used_letters, win)

        # TODO 1: define a "variable" to hold the user's guess. Use the get_guess function to ask the user to guess a letter
        # call this variable "guess"

        # TODO 2: update the "used_letters" array with the guess so the user knows not to guess it again

        # TODO 3: use the "get_indexes" function to get a list of the positions within the secret_word that match the guess
        # store this in a new variable called "matching_positions"

        # TODO 4: check if the user was right or not. To do this, check how many entries are in the "matching_positions"
        # array. If there are none, then we know they were wrong. To do this, you can use the "len" function.
        # that function returns the "length" of the array. If the user is wrong, add 1 to incorrect_count

        # TODO 5: update the current_word variable by calling the update_current_word function and assigning the result
        # back to the current_word array. This will replace any blanks with the guess if it is correct.
        # look a the documentation for the update_current_word function and make sure you pass it the right parameters

        time.sleep(.05)
    draw_word(current_word, win)
    draw_used(used_letters, win)
    show_result(is_winner(current_word), win)
    win.getKey()  # wait for key
    win.close()  # Close window when done


def get_secret_word():
    """
    This method returns the secret word that will be used for the game. It takes no inputs and returns a single word.
    :return:
    """
    # TODO 6: replace this code with code that can return a secret word to use for this game. To make the game more fun,
    # you probably want to make it 'random' so that each time you play the game, a different word is used.
    # to do this, you can use random.choice(XXXX) where XXXX is an array of words that can be used.
    return "test"


def is_dead(incorrect_count):
    """
    This method returns True if the play has lost (too many wrong guesses). Otherwise, it returns False.
    :param incorrect_count:
    :return:
    """
    # TODO 7: replace the body of this function with code that can determine if the player is dead or not
    return False


def is_winner(current_word):
    """
    This method returns True if the user won (found all letters in the secret word), otherwise it returns False.
    :param current_word:
    :return:
    """
    # TODO 8: replace the body of this function with code that can determine if the player has won or not
    return False


def get_guess(window, used_letters):
    """
    Displays a prompt asking for a guess and waits for input from the user. If they press the escape key, the program
    will exit. This method blocks until the user presses escape or a valid guess (letter not already guessed).
    :param window:
    :param used_letters:
    :return:
    """
    guess = prompt_for_guess(window)
    while not is_valid_guess(guess, used_letters):
        guess = prompt_for_guess(window)
    return guess.strip().lower()


def show_result(did_win, window):
    """
    This method displays the game result text based on whether the user won or not.
    :param did_win: a boolean value indicating if the user won (True) or not (False)
    :param window: window that should be updated
    :return:
    """
    text = "YOU WIN"
    if not did_win:
        text = "YOU LOSE"
    t = Text(Point(WIN_WIDTH / 2, WIN_HEIGHT / 2), text)
    t.setSize(36)
    t.setStyle("bold")
    t.setTextColor("red")
    t.draw(window)


def update_current_word(current_word, positions, guess):
    """
    This method updates the "current_word" by replacing the blanks at each of the positions indicated in the positions
    array with the guess.
    :param current_word: string representation of the word with blanks for each un-guessed letter
    :param positions: list of indexes within current_word that should be replaced
    :param guess: letter that was guessed by the user
    :return:
    """
    char_list = list(current_word)
    for pos in positions:
        char_list[pos] = guess
    return ''.join(char_list)


def get_indexes(guess, secret_word):
    """
    This method returns an array of indexes within the secret_word that match the guess. For example, if the word was
    'tomato' and guess is 't', the return value would be [0,4]. If the secret word was 'tomato' and the guess was 'z',
    the return value would be [] (an empty list).
    :param guess:
    :param secret_word:
    :return:
    """
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
    """
    This method returns True if the character passed in is a lowercase letter.
    :param character:
    :return:
    """
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
    # draw the man based on how many wrong guesses there are
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
    """
    This method draws the 'current_word' to show the user's progress in guessing it. The word is drawn along the bottom
    of the game window.
    :param current_word:
    :param window:
    :return:
    """
    total_width = len(current_word) * BLANK_WIDTH + (len(current_word) - 1) * PADDING
    cur_x = (WIN_WIDTH - total_width) / 2
    for val in current_word:
        t = Text(Point(cur_x, WIN_HEIGHT - WIN_HEIGHT / 4), val)
        t.setSize(36)
        t.draw(window)
        cur_x += BLANK_WIDTH + PADDING


def prompt_for_guess(window):
    """
    This method draws the prompt asking the user to enter a guess and then waits for the user to press a key. It returns
    a string that represents the key pressed.
    :param window:
    :return:
    """
    guess_y = WIN_HEIGHT - WIN_HEIGHT / 5
    t = Text(Point(PADDING * 7, guess_y), "Enter a guess")
    t.setSize(24)
    t.draw(window)
    return window.getKey()


def draw_used(used_letters, window):
    """
    This method draws the set of letters that the user has guessed. This is drawn under the current word at the bottom
    of the game window.
    :param used_letters: array of letter that have been guessed
    :param window:
    :return:
    """
    t = Text(Point(PADDING * 3, WIN_HEIGHT - WIN_HEIGHT / 7), "Used:")
    t.setSize(24)
    t.draw(window)
    cur_x = PADDING * 2
    for val in used_letters:
        t = Text(Point(cur_x, WIN_HEIGHT - WIN_HEIGHT / 9), val)
        t.setSize(20)
        t.draw(window)
        cur_x += BLANK_WIDTH + PADDING


# Code that is not enclosed in a function is run when this file is run via the command line or when it is imported
# into another module
main()
