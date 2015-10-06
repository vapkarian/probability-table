# Probability table
Script allows to estimate outcomes of dice rolls. It is useful for board games with complex dices, for example
[Descent](https://en.wikipedia.org/wiki/Descent:_Journeys_in_the_Dark) or [Doom](https://en.wikipedia.org/wiki/Doom:_The_Boardgame).
The game features many different dice, while they are all six-sided, they contain a number of symbols (sometimes three on a single face).
You may want to know probability of all outcomes for many possible cases:

1. Choosing between two pairs/triples of dices.
2. Probability of X+ damage/range/defense.
3. Comparing between sets of dices for further usage.

Each dice must to be filled as a list of lists, where nested list is one side of the dice, and its elements must be the values at this side.
You can review example of dices in two ready pack: [descent.py](descent.py) and [doom.py](doom.py).
Blue, red and yellow dices for Descent are six-side dices, each side may contains numeric value (range), some count of hearts (damage) and some count of surges (additional amplifications).
If at least one side of dice contains some parameter, each nested list must contain it even if appropriate side doesn't contain it (you can use 0 in this case).
If dice have miss value (X), nested list must be replaced by single None value.
For example, blue dice from Descent has 6 sides. It must be like:
blue = [
    None,  # single value for 'X'
    [2, 2, 1],  # '2' numeric value, two hearts, one surge
    [3, 2, 0],  # '3' numeric value, two hearts, no surges
    [4, 2, 0],  # '4' numeric value, two hearts, no surges
    [5, 1, 0],  # '5' numeric value, one heart, no surges
    [6, 1, 1],  # '6' numeric value, one heart, one surge
]

Rules of printing probability table depend on the rules:

1. First argument is a list of interested parameters. Length of this list should no more than smallest nested list of dice.
Order of parameters is related to order of parameters on appropriate side. Unnecessary parameters must be replaces by None values.
2. Positional arguments are any number of dices, filled by rules above.
3. Keyword arguments are used for special option: set at_least=False if you want to know probability of "no more than" instead of "at least / no less than".

Example of usages you can see in [descent.py](descent.py) and [doom.py](doom.py) files.

Examples for Descent contains outcomes:

1. Yellow and blue dices for ranged attack (probability of missing, ranges, damages and surges)
2. Red and blue dices for melee attack (probability of missing, damages and surges; ranges don't matter)
3. Brown dice for defense of zombie (probability of defense)
4. Black and grey dices for test willpower (probability of "no more than" value)

Example for Doom contains outcomes:

1. Red, yellow, two green and two blue dices for BFG (probability of missing, ranges, damages and bullets)
2. Yellow and blue dices for ranged attack of Imp (probability of missing, ranges and damage; bullets don't matter)
3. Red and green dices for melee attack of Trite (probability of missing and damage; bullets and ranges don't matter)

Example of probability table for yellow and blue dices for Descent:

Miss: 6/36 (16.67%)

Range:
2+: 30/36 (83.33%)
3+: 27/36 (75.00%)
4+: 22/36 (61.11%)
5+: 16/36 (44.44%)
6+: 10/36 (27.78%)
7+: 4/36 (11.11%)
8+: 1/36 (2.78%)

Damage:
1+: 30/36 (83.33%)
2+: 28/36 (77.78%)
3+: 19/36 (52.78%)
4+: 6/36 (16.67%)

Surges:
1+: 21/36 (58.33%)
2+: 6/36 (16.67%)
