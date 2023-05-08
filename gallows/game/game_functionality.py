from random import choice
from gallows.database.list_of_used_words import word_list


def get_word():
    word = choice(word_list)
    return word.lower()
