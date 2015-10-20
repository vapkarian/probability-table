from __future__ import print_function

from probability_table import print_table


__all__ = ['red', 'yellow', 'blue', 'green']

red = [None, [3, 1, 0], [2, 2, 0], [1, 3, 0], [1, 3, 1], [0, 4, 1]]
yellow = [None, [3, 1, 0], [3, 1, 1], [2, 2, 0], [1, 3, 0], [4, 0, 1]]
blue = [[1, 1, 0], [0, 2, 0], [1, 2, 0], [0, 3, 0], [0, 2, 0], [0, 3, 0]]
green = [[1, 1, 0], [2, 1, 0], [2, 0, 0], [3, 0, 0], [2, 0, 0], [3, 0, 0]]

if __name__ == '__main__':
    print('Red + yellow + green + green + blue + blue:')  # BFG
    print()
    print_table(['Range', 'Damage', 'Bullets'], red, yellow, green, green, blue, blue)
    print('-' * 19)

    print('Yellow + blue:')  # Imp
    print()
    print_table(['Range', 'Damage', None], yellow, blue)  # Bullets don't matter
    print('-' * 19)

    print('Red + green:')  # Trite
    print()
    print_table([None, 'Damage', None], red, green)  # Range and bullets don't matter
    print('-' * 19)
