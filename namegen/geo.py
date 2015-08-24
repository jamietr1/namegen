import collections
import random
import os

def get_random_state(region):
    states = []
    for state in state_list:
        if region == '':
            states.append(state)
        elif region == state_list[state]:
            states.append(state)

    if len(states) == 0:
        return ''
    else:
        return random.choice(states)

def get_random_city(statename, population):
    if statename == '':
        statename = state('')

    cities = []
    for city in city_list:
        tokens = city_list[city].split(',')
        city_name = city.split(',')
        if tokens[0] == statename:
            if population == 0:
                cities.append(city_name[0])
            elif population > int(tokens[1]):
                cities.append(city_name[0])
            break

    if len(cities) == 0:
        return ''
    else:
        return random.choice(cities)

def get_states():
    global state_list
    state_list = {}
    this_dir, this_file = os.path.split(__file__)
    DATA_PATH = os.path.join(this_dir, "data/geo/states.txt")

    with open(DATA_PATH, 'r') as f:
        for line in f:
            tokens = line.rstrip('\n').split(',')
            state_list[tokens[0]] = tokens[1]

def get_cities():
    global city_list
    city_list = {}
    this_dir, this_file = os.path.split(__file__)
    DATA_PATH = os.path.join(this_dir, "data/geo/cities.txt")

    with open(DATA_PATH, 'r') as f:
        for line in f:
            tokens = line.rstrip('\n').split(',')
            city_list[tokens[0] +',' + tokens[1]] = tokens[1] + ',' + tokens[2]
