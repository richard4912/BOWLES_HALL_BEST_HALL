"""
This is a minimal contest submission file. You may also submit the full
hog.py from Project 1 as your contest entry.

Only this file will be submitted. Make sure to include any helper functions
from `hog.py` that you'll need here! For example, if you have a function to
calculate Free Bacon points, you should make sure it's added to this file
as well.
"""

TEAM_NAME = 'BOWLES_HALL_BEST_HALL'  # Change this line!


def final_strategy(score, opponent_score):
    return 5

def hog_wild(score, opponent_score):
    """ Returns true if the hog wild rule applies (sum of scores is a multiple
    of seven) and the dice need to be swapped.
    >>> hog_wild(7,0)
    True
    >>> hog_wild(29, 70)
    False
    >>> hog_wild(0, 0)
    True
    >>> hog_wild(62, 1)
    True
    """
    return #...


#returns the result of (potentially) running hogtimus prime
def hogtimus_prime(player_score):
    if(not is_prime(player_score)):
        return player_score

    player_score += 1
    while(not is_prime(player_score)):
        player_score += 1

    return player_score


#short method to determine if a number is prime
def is_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True

    assert num % 1 == 0, 'Number must be a natural number greater than 1'

    for n in range(2, num):
        if num % n == 0:
            return False
    return True


#Implements rules for "When Pigs Fly"
def when_pigs_fly(turn_score, num_rolls):
    return min(turn_score, 25 - num_rolls)

def free_bacon(opponent_score):
    """Return the points scored from rolling 0 dice (Free Bacon)."""
    # BEGIN PROBLEM 2
    largest = 0
    while opponent_score > 0:
        if opponent_score % 10 > largest:
            largest = opponent_score % 10
        opponent_score //= 10
    return largest + 1


def should_swap(score1, score0):
    return score0 == 2 * score1 or score1 == 2 * score0
