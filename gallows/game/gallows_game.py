from random import choice
from gallows.database.list_of_used_words import word_list
from gallows.database.display_hangman import display_hangman


def get_word():
    word = choice(word_list)
    return word.lower()


def play(word):
    # строка, содержащая символы _ на каждую букву задуманного слова
    word_completion = '_' * len(word)
    list_word = list(word_completion)
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 8  # количество попыток

    print('Давайте играть в угадайку слов!')
    print(f'Колличество попыток - {tries}')
    print(display_hangman(tries))
    print(word[0] + word_completion[1:-1] + word[-1])

    while tries != 0:
        print(word)
        user_input = input('Введите слово или букву  ').lower()
        if not user_input.isalpha():
            print('Вы ошиблись, попробуйте еще раз!')
            continue

        if user_input in guessed_letters or user_input in guessed_words:
            print('Уже было!')
            continue

        if len(user_input) == 1:
            guessed_letters.append(user_input)
            if user_input in word:
                for i in range(len(word)):
                    if user_input == word[i]:
                        list_word.pop(i)
                        list_word.insert(i, word[i])
            else:
                print('Такой буквы нет в слове!')
            tries -= 1
            print(display_hangman(tries))
            print(*(list(word[0]) + list_word[1:-1] + list(word[-1])), sep='')
            print(f'Колличество попыток - {tries}')
            if list(word[0]) + list_word[1:-1] + list(word[-1]) == list(word):
                print('Поздравляем, вы угадали слово! Вы победили!')
                break

        if len(user_input) > 1:
            guessed_letters.append(user_input)
            if user_input != word:
                tries -= 1
                print(display_hangman(tries))
                print('Не правильное слово!')
                print(f'Колличество попыток - {tries}')
            elif user_input == word:
                print('Поздравляем, вы угадали слово! Вы победили!')
                break

        if tries == 0:
            print(display_hangman(tries))
            print(f'Правильное слово {word.upper()}')

    yes = 'да'
    no = 'нет'
    game_replay = input(f'Хотите сыграть еще раз? {yes}/{no}  ')
    if game_replay == yes:
        play(get_word())
    elif game_replay == no:
        exit()
