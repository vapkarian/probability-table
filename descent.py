from __future__ import print_function

from probability_table import print_table


__all__ = ['blue', 'yellow', 'red', 'brown', 'grey', 'black']

blue = [None, [2, 2, 1], [3, 2, 0], [4, 2, 0], [5, 1, 0], [6, 1, 1]]
yellow = [[0, 1, 1], [1, 0, 1], [1, 1, 0], [2, 1, 0], [0, 2, 0], [0, 2, 1]]
red = [[0, 1, 0], [0, 2, 0], [0, 2, 0], [0, 2, 0], [0, 3, 0], [0, 3, 1]]
brown = [[0], [0], [0], [1], [1], [2]]
grey = [[0], [1], [1], [1], [2], [3]]
black = [[0], [2], [2], [2], [3], [4]]

if __name__ == '__main__':
    print('Yellow + blue:')  # Ranged attack
    print()
    print_table(['Range', 'Damage', 'Surges'], yellow, blue)
    print('-' * 19)

    print('Red + blue:')  # Melee attack
    print()
    print_table([None, 'Damage', 'Surges'], red, blue)  # range doesn't matter
    print('-' * 19)

    print('Brown:')  # Zombie's defense
    print()
    print_table(['Defense'], brown)
    print('-' * 19)

    print('Black + grey:')  # Test willpower
    print()
    print_table(['Attribute test'], black, grey, at_least=False)
    print('-' * 19)
