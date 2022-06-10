import random as r

guesses = 9
letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')


def format_word(guessed_letters, word):
    '''
        This function helps to format our secret word with
        the letters that have been guessed correctly. For
        example, if the secret word is PYTHON and only 'n',
        'o' and 'p' have been guessed correctly, P---ON is
        displayed.
    '''
    formatted_string = ''
    for letter in word:
        if letter in guessed_letters:
            formatted_string += letter
        else:
            formatted_string += '-'
    return formatted_string


def display_info(guessed_letters, word):
    '''
        This function takes in the guessed letters and the
        secret word and generates the required data i.e. the
        number of guesses left, the letters that haven't been
        tried yet etc. from the provided data.
    '''
    available_letters = ' '.join([
        letter for letter in letters if letter not in guessed_letters
    ])
    print(format_word(guessed_letters, word))
    print(f'Guesses left: {guesses}.')
    print(f'Available letters: {available_letters}.')


def check_guess(guess, word, guessed_letters):
    '''
        This function takes in the guessed letters, the
        secret word and the new guess. It checks if the
        guess is valid and prints the appropriate message
        if it's not. The [display_info] function is then
        called.
    '''
    global guesses
    if guess in letters and len(guess) == 1 and guess not in guessed_letters:
        guessed_letters.append(guess)
        if guess in word:
            print('Good guess!')
        else:
            print('Bad guess!')
            guesses -= 1
    else:
        if len(guess) != 1:
            print('You must enter one letter, no more, no less!')
        elif guess.upper() not in letters:
            print('Your guess has to be a letter!')
        elif guess in guessed_letters:
            print('This letter has been tried already!')
    display_info(guessed_letters, word)


def can_be_formed_from(letters, word):
    '''
        This function accepts two strings and returns true
        if the second string can be formed from the letters
        of the first.
    '''
    for letter in word:
        if letter not in letters:
            return False
    return True


def play_game():
    '''
        This is the entry point of our game. This is
        where the user is prompted for their guess. The
        necessary checks are then carried out.
    '''
    word_list = ['programmer', 'python', 'defenestrate']
    secret_word = r.choice(word_list).upper()
    word_length = len(secret_word)
    guessed = []
    print(f'You have chosen a/an {word_length}-letter word.')
    while guesses > 0:
        guess = input('Enter a letter: ')
        guess = guess.upper()
        check_guess(guess, secret_word, guessed)
        if can_be_formed_from(guessed, secret_word):
            return print('YOU WON!')
    print('You ran out of guesses.\nYOU LOST!')


if __name__ == '__main__':
    play_game()