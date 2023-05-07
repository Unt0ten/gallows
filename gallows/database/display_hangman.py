def display_hangman(tries):
    stages = [
        # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |
           |
           |
           -
        ''',
        # готовая виселица
        '''
           --------
           |      |
           |
           |
           |
           |
           -
        ''',
        # стоб
        '''

           |
           |
           |
           |
           |
           -
        ''',
        # начальное состояние
        '''






           -
        '''

    ]
    return stages[tries]