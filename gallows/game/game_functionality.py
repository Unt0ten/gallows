from random import choice
from gallows.database.list_of_used_words import word_list


def get_word():
    word = choice(word_list)
    return word.lower()


def end_game(play):
    yes = 'да'
    no = 'нет'
    while True:
        game_replay = input(f'Хотите сыграть еще раз? {yes}/{no}  ')
        if game_replay == yes:
            play(get_word())
        elif game_replay == no:
            exit()
        else:
            print(f'Пожалуйста, введите {yes}/{no}!')
            continue
