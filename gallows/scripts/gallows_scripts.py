#!/usr/bin/env python3

from gallows.game.gallows_game import play
from gallows.game.game_functionality import get_word
from gallows.game.game_functionality import end_game


def main():
    play(get_word())


if __name__ == '__main__':
    main()
