"""
This is a minimal contest submission file. You may also submit the full
hog.py from Project 1 as your contest entry.

Only this file will be submitted. Make sure to include any helper functions
from `hog.py` that you'll need here! For example, if you have a function to
calculate Free Bacon points, you should make sure it's added to this file
as well.
"""

TEAM_NAME = 'BOWLES_HALL_BEST_HALL' # Change this line!

def memo(f):
	#ima decorator
	#ripperoni pepperoni !!!1!!11!!
	#THE SECRET IS OUT RUNNNNnn
    cache = {}
    def memoized(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return memoized

def probablity_of_winning_with_n(score, opponent_score, n):
	return 4
	#FIX THIS LINE ^^^^^

def six_sided(outcome):
	if 1 <= outcome <= 6:
		return 1/6
	else:
		return 0

@memo
def roll_ones(total, n,dice):
	"""Chance of scoring TOTAL in N rolls of DICE when at least one is a one.
	"""
	if total > n:
		return 0
	elif n==0 and total==0:
		return 1
	elif n==0 and total != 0:
		return 0
	else: 
		#this is a recurisve case
		#why this is a recurisve problem: multiple dice rolls, score of dice rolling is FIRST DICE + REST OF DICE
		#one of two things that can happen: 1 or [the rest]
		with_one = dice(1) * roll_ones(total-1, n-1, dice)
			#chance of rolling 1 TIMES rolling n-1 ones in the rest of the dice
		without_one = (1-dice(1)) * roll_ones(total, n-1, dice)
		return with_one + without_one

def roll_dice(total, n, dice=six_sided):
	return roll_ones(total, n, dice) + roll_no_ones(total, n, dice)

@memo
def roll_no_ones(total, n, dice):
	#limited to SIX SIDED DICE
	if n==0 and total==0:
		return 1
	elif n==0 and total != 0:
		return 0
	else:
		chance, outcome = 0,2
		while outcome <= 6:
			chance += dice(outcome) * roll_no_ones(total - outcome,n-1,dice)
			outcome +=1
		return chance

def roll_at_least(k,n,dice=six_sided):
	#theres a more efficent way like roll_no_ones that doesnt iterate, but just one recursive call
	total, chance = k, 0
	while total <= 6*n:
		chance += roll_dice(total,n,dice)
		total += 1
	return chance

def rerolled(outcome):
	if 1 <= outcome <= 6:
		if outcome % 2 == 0:
			return 1/6 + 1/2*1/6
			#roll two or roll odd and then a two
		else:
			return 1/2 * 1/6
	else:
		return 0

def best_dice_to_roll(score, opponent_score):
	magic_num, magic_score = 0,0
	for x in range(0,11):
		score = probablity_of_winning_with_n(score,opponent_score,x)
		if score > magic_score:
			magic_score,magic_num=score,x
	return magic_num

@memo
def final_strategy(score, opponent_score):
    return best_dice_to_roll(score, opponent_score)

#this is nim vim mac vim text editor yay
goal = 23
def constant(k):
	return lambda n: k

@memo
def winner(n, strat, other):
	if n >= goal:
		return 0
	else:
		return 1 - winner(n + strat(n), other, strat)

@memo
def optimal(n , other):
	choice = 1
	future = lambda future_n: optimal(future_n, other)
	while choice <= 3:
		if winner(n+choice, other, future) == 1:
			return choice
		choice = choice + 1
	return 1

def print_perfect():
	n=0
	perfect = lambda n: optimal(n, perfect)
	other = perfect
	while n<goal:
		if winner(n,perfect, other) == 0:
			print('Perfect play from',n,'wins beautifully with',perfect(n))
		else:
			print('Perfect play from',n,'loses miserably')
		n+=1