import collections
import random
import os

def get_random_state(region):
    this_dir, this_file = os.path.split(__file__)
    DATA_PATH = os.path.join(this_dir, "data/geo/states.txt")

    states = []
    with open(DATA_PATH, 'r') as f:
        for line in f:
            tokens = line.rstrip('\n').split(',')
            if region == '':
                states.append(tokens[0])
            elif region == tokens[1]:
                states.append(tokens[0])

    if len(states) == 0:
        return ''
    else:
        return random.choice(states)


def get_random_city(statename, population):
    this_dir, this_file = os.path.split(__file__)
    DATA_PATH = os.path.join(this_dir, "data/geo/cities.txt")

    if statename == '':
        statename = state('')

    cities = []
    with open(DATA_PATH, 'r') as f:
        for line in f:
            tokens = line.rstrip('\n').split(',')
            if tokens[1] == statename:
                if population == 0:
                    cities.append(tokens[0])
                elif population > int(tokens[2]):
                    cities.append(tokens[0])

    if len(cities) == 0:
        return ''
    else:
        return random.choice(cities)
