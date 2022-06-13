from xml.etree.ElementInclude import include


def print_upper_words(wordList):
    '''Converts each word in a list to uppercase'''
    for words in wordList:
        print(words.upper())


# def print_upper_words_withE(wordList):
#     '''Converts each word in a list to uppercase that start with the letter E or e'''
#     for words in wordList:
#         if words == 'e' or words == 'E':
#             print(words.upper())


def print_upper_words_withE(wordList):
    '''Converts each word in a list to uppercase that start with the letter E or e'''
    for words in wordList:
        if words.startswith('e') or words.startswith('E'):
            print(words.upper())


def print_upper_words_with_choosen(wordList, must_start_with):
    '''Converts each word in a list to uppercase that start with the letter input in the function must_start_with'''
    for words in wordList:
        for letter in must_start_with:
            if words.startswith(letter) :
                print(words.upper())
                break

# what does break do ?

print_upper_words_with_choosen(["hello", "hey", "goodbye", "yo", "yes", 'eat'], must_start_with='H')