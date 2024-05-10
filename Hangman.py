from os import system, name
import time
def clear():
    """This function clear the Console"""
    time.sleep(1.5)
    # for windows the name is 'nt'
    if name == 'nt':
        _ = system('cls')
    # and for mac and linux, the os.name is 'posix'
    else:
        _ = system('clear')

def check_win(secret_word, old_letters_guessed):  # Unit 7 - Q7.3.2
    """This function checks whether the player was able to guess the secret word and thus won the game.
    :param secret_word: A string represents the secret word the player has to guess.
    :type secret_word: Str
    :param old_letters_guessed: A list contains the letters the player has guessed so far.
    :type old_letters_guessed: List
    :return: Return true if all the letters that make up the secret word are included in the list of letters the user guessed. Otherwise, the function returns False.
    :rtype: Bool
    """
    for Letter in secret_word:
        if old_letters_guessed.count(Letter) != 1:
            return False
    return True

def show_hidden_word(secret_word, old_letters_guessed):  # Unit 7 - Q7.3.1
    """This function returns a string which consists of letters and lower hopes.
	The string displays the letters from the old_letters_guessed list that are in the secret_word string in their appropriate position, and the rest of the letters in the string (which the player has not yet guessed) as underlines.
	:param secret_word: A string represents the secret word the player has to guess
	:type secret_word: Str
	:param old_letters_guessed: A list contains the letters the player has guessed so far
	:type old_letters_guessed: List
	:return: Return a string which consists of letters and lower hopes
	:rtype: Str
	"""
    show_hidden_word_List = []
    for Letter in secret_word:
        show_hidden_word_List += '_'
    i = 0
    for Letter in secret_word:
        for Letter_guessed in old_letters_guessed:
            if Letter == Letter_guessed:
                show_hidden_word_List[i] = Letter_guessed
                break
        i += 1
    return str(' '.join(show_hidden_word_List))


def check_valid_input(letter_guessed, old_letters_guessed):  # Unit 6 - Q6.4.1
    """The function returns a boolean value representing the correctness of the string and whether the user has guessed the character in the past.
	:param letter_guessed: String that represents the character received from the player.
	:type letter_guessed: Str
	:param old_letters_guessed: List that contains the letters the player has guessed so far.
	:type old_letters_guessed: List
	:return: Return a Boolean value representing the correctness of the string and whether the user has guessed the character in the past.
	:rtype: Bool
	"""
    return (len(letter_guessed) == 1) and (letter_guessed.isalpha()) and (
        not (letter_guessed.lower() in old_letters_guessed))


def try_update_letter_guessed(letter_guessed, old_letters_guessed):  # Unit 6 - Q6.4.2
    """If the character is valid (i.e. one English letter) and not previously guessed, the function will add the letter_guessed character to the old_letters_guessed list.
	You will then return a True value indicating that the insertion was successful.
	If the character is invalid (ie not a single English letter) or is already in the guess list, the function will print the character X (capital letter X) and below it the old_letters_guessed list as a string of lowercase letters sorted from uppercase to uppercase and separated by arrows (see sample output).
	The organ print is designed to remind the player which characters he has already guessed.
	At the end, the function returns a false value which means that it is not possible to add the character to the list of characters already guessed.
	:param letter_guessed: String that represents the character received from the player.
	:type letter_guessed: Str
	:param old_letters_guessed: List that contains the letters the player has guessed so far.
	:type old_letters_guessed: List
	:return: Return whether the guess can be added to the guess list
	:rtype: Bool
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    else:
        print('X')
        print_old_letters_guessed = " -> ".join(old_letters_guessed)
        print(print_old_letters_guessed)
        return False


def choose_word(file_path, index):  # Unit 9 - Q9.4.1
    """This function selects for the player a word that will be the secret word for guessing, from a text file containing a list of words separated by spaces.
	:param file_path: A string (file_path) that represents a path to the text file.
	:type file_path: Str
	:param index: An integer (index) that represents the location of a particular word in a file.
	:type index: Int
	:return:Return a Tuple consisting of two organs in the following order:
	The number of different words in a file, that is, does not include repetitive words.
	A word in a position obtained as an argument to a function (index), which will be used as the secret word for guessing.
	:rtype: Tuple
	"""
    file = open(file_path, 'r')
    list_of_words = file.read().replace("\n", '').split(' ')
    file.close()
    while index > len(list_of_words):
        index -= len(list_of_words)
    return list_of_words[index - 1]


def print_opening_screen():  # Unit 2 - Q2.5.1
    """This function print the opening screen of the Hangman game"""
    HANGMAN_ASCII_ART = """    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/\n"""
    MAX_TRIES = 6
    print(HANGMAN_ASCII_ART, MAX_TRIES)


def main():
    do_you_want_to_play = input("Do you want to play a game? ")
    print("OK")
    while do_you_want_to_play.lower() == "yes":
        clear()
        # Auxiliary variables:
        secret_word = ""  # A string called secret_word. This is the word the user needs to guess.
        old_letters_guessed = []  # A list called old_letters_guessed. The list holds the letters the player has guessed so far.
        MAX_TRIES = 6  # A number called MAX_TRIES. The variable holds the maximum allowed attempts allowed in the game, which is 6.
        num_of_tries = 0  # A number called num_of_tries. The number represents the number of failed attempts the user has made so far.
        HANGMAN_PHOTOS = {"0": "    x-------x","1": """    x-------x 
    |
    |
    |
    |
    |""","2": """    x-------x
    |       |
    |       0
    |
    |
    |""","3": """    x-------x
    |       |
    |       0
    |       |
    |
    |""","4": """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""","5": """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""","6": """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""}  # A dictionary called HANGMAN_PHOTOS. The variable holds the pictures of the man depending on each of the situations. #Unit 8 - Q8.4.1
        # Game stage number 1:
        print_opening_screen()
        # Game stage number 2:
        secret_word = choose_word(input("Enter file path: "), int(input("Enter index: ")))
        print("Let’s start The game!")
        # The Game Loop (stages 3&4&5):
        while (not(check_win(secret_word, old_letters_guessed))) and (num_of_tries < 6):
            clear()
            # Game stage number 3:
            print(HANGMAN_PHOTOS[str(num_of_tries)])
            print("You have " + str(MAX_TRIES - num_of_tries) + " attempts")
            # Game stage number 4:
            print(show_hidden_word(secret_word, old_letters_guessed))
            # Game stage number 5:
            not_valid_input = True
            letter_guessed = ""
            while not_valid_input:
                letter_guessed = input("Guess a letter: ")
                if try_update_letter_guessed(letter_guessed, old_letters_guessed):
                    not_valid_input = False
            if letter_guessed not in secret_word:
                print(":(")
                num_of_tries += 1
        clear()
        # Game stage number 6:
        print("Game Over!\nThe Hangman:")
        if check_win(secret_word, old_letters_guessed):
            print(HANGMAN_PHOTOS[str(num_of_tries)])
            print("You managed to guess the secret word, " + '"' + secret_word + '"')
            print("You won.")
            print("(:")
        else:
            print(HANGMAN_PHOTOS[str(MAX_TRIES)])
            print("You managed to guess this: " + show_hidden_word(secret_word, old_letters_guessed))
            print("The secret word is: " + secret_word)
            print("You lost.")
            print("):")
        do_you_want_to_play = input("Want to play the game again? ")
        print("OK")
        if do_you_want_to_play.lower() != "yes":
            print("Thank you so much for playing!")
    clear()            
    print("Bye Bye.")

if __name__ == "__main__":
    main()