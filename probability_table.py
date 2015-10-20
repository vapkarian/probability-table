from __future__ import print_function

from itertools import product


__all__ = ['print_table']


def print_table(params, *dices, **options):
    """
    Print probability of outcomes for given `params` based on given `dices`. Length of `params` must be no more than
    length of smallest faces of `dices` (it means that `dices` with different length of faces can be calculated).
    Unnecessary element of `params` should be filled by None value: in this case element of `params` will be ignored.

    :param list[str|unicode] params: each element is interesting parameter (or None) in order of faces of `dices`
    :param list[list[int]] dices: several dices where each face must be list of values on it
    :param dict options: keyword parameter `at_lest` means calculating probability ascendingly
    :return: None
    """
    at_least = options.get('at_least', True)
    count = pow(6, len(dices))
    results = [None if None in outcome else [sum(elem) for elem in zip(*outcome)] for outcome in list(product(*dices))]
    if None in results:
        fails_count = len([elem for elem in results if elem is None])
        print('Miss: {}/{} ({:.2f}%)'.format(fails_count, count, fails_count * 100. / count))
        print()
    for index, param in enumerate(params):
        if param is None:
            continue
        print('{}:'.format(param))
        max_param = max(elem[index] for elem in results if elem is not None)
        min_param = min(elem[index] for elem in results if elem is not None)
        if at_least:
            min_param = max(1, min_param)
        for value in range(min_param, max_param + 1):
            if at_least:
                comparison = lambda x, y: x >= y
                sign = '+'
            else:
                comparison = lambda x, y: x <= y
                sign = '-'
            param_count = len([elem for elem in results if elem is not None and comparison(elem[index], value)])
            param_percent = param_count * 100. / count
            print('{value}{sign}: {param_count}/{count} ({param_percent:.2f}%)'.format(**locals()))
        print()
