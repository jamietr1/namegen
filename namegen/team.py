import collections
import random
import os

def get_random_team():
    this_dir, this_file = os.path.split(__file__)
    DATA_PATH = os.path.join(this_dir, "data/teams/teams.txt")

    teams = []
    with open(DATA_PATH, 'r') as f:
        for line in f:
            tokens = line.rstrip('\n').split(',')
            teams.append(tokens[0])

    return random.choice(teams)
