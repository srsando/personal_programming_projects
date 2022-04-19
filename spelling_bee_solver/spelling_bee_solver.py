# This is a script that automatically solves a given NYTs "Spelling Bee" puzzle.
# It takes one "central" letter (must be used to form a word) and 6 "optional" letters (may be used to form a word)
# as inputs and then outputs a list of all 4+ letter words that can be made from those letters.

# run this the first time you use the program to download the list of words:
# import nltk
# nltk.download('words')
# print('download complete')

import string
from nltk.corpus import words

# First, determine which letter set (default or user-specified) to use:
central_letter = input('Enter central letter, or "default" for hardcoded letter set:')

# Run the default, hardcoded letter set or enter today's puzzle:
if central_letter == 'default':
    central_letter = 'i'
    optional_letters_block = 'python'

else:
    if len(central_letter) != 1:
        print("Please enter only one central letter!")
        quit()

    optional_letters_block = input('Input optional letters (no spaces):')
    if len(optional_letters_block) != 6:
        print('Please enter 6 optional letters - no more, no less!')
        quit()

optional_letters = list(optional_letters_block)

alphabet = string.ascii_lowercase
word_list_all_words = words.words()

# Remove words less than 4 letters long:
word_list = [x for x in word_list_all_words if len(x) >= 4]

# get a list of all letters NOT in the set and use these to filter the English dictionary first:
disallowed_letters = [x for x in alphabet if x not in central_letter and x not in optional_letters]


# This function lets us succinctly check whether a given word contains any from a set of letters:
def contains_any_letters(word, letter_list):
    return 1 in [c in word for c in letter_list]


# Now exclude every word from the English dictionary that has any letter NOT in the puzzle set:
word_list_disallowed_excluded = [x for x in word_list if not contains_any_letters(x, disallowed_letters)]

# Next, exclude any word that doesn't contain the central letter:
answers_names_included = [x for x in word_list_disallowed_excluded if central_letter in x]

# Remove proper nouns:
answers = [x for x in answers_names_included if x[0].isupper() is False]

# Sort the answers by length
answers_sorted = sorted(answers, key=len)

print(answers_sorted)
