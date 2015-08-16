# A module for generating play names based on a relative year, and weighted by
# popularity in that year. I think this gives the naming a more realistic
# feel when a simulation is run over 100 seasons.
import collections
import random
import os

def firstname(year, gender):
    if year < 1880 or year > 2014:
        return ''

    # 1. Find the right file
    this_dir, this_file = os.path.split(__file__)
    DATA_PATH = os.path.join(this_dir, "data/firstnames", 'yob' + str(year) + '.txt')

    # 2. Build a mapping
    min_val = 0
    max_val = get_max_population(year, gender)
    roll = random.randint(1, max_val)

    with open(DATA_PATH, 'r') as f:
        for line in f:
            splitLine = line.rstrip('\n').split(',')
            if splitLine[1] == gender:
                max_val = int(splitLine[2])
                if (roll > min_val) and (roll <= max_val):
                    first_name = splitLine[0]
                    break

                min_val = max_val

    # 3. Does the name have a diminutive?
    diminutives = has_diminutive(first_name)
    if (diminutives != ''):
        if random.randint(1,100) > 50:
            dim_list = diminutives.split(',')
            diminutive = random.choice(dim_list)
            return first_name + ' (' + diminutive + ')'
        else:
            return first_name
    else:
        return first_name

def surname():
    this_dir, this_file = os.path.split(__file__)
    DATA_PATH = os.path.join(this_dir, "data/surnames", 'surnames.txt')

    min_val = 0
    max_val = 60113
    roll = random.randint(1, max_val)

    with open(DATA_PATH, 'r') as f:
        for line in f:
            splitLine = line.rstrip('\n').split(',')
            max_val = int(splitLine[1])
            if (roll > min_val) and (roll <= max_val):
                surname = splitLine[0]

            min_val = max_val
    return surname.title()

def fullname(year, gender):
    first_name = firstname(year, gender)
    last_name = surname()
    return first_name, last_name

def has_diminutive(name):
    name_dict = {}
    this_dir, this_file = os.path.split(__file__)
    DATA_PATH = os.path.join(this_dir, "data/firstnames", 'diminutives.txt')

    with open(DATA_PATH, 'r') as f:
        for line in f:
            line.rstrip('\n')
            splitLine = line.split(':')
            name_dict[splitLine[0]] = splitLine[1]

    if name in name_dict:
        return name_dict[name].rstrip('\n')
    else:
        return ''

def get_max_population(year, gender):
    # 1. Find the right file
    this_dir, this_file = os.path.split(__file__)
    DATA_PATH = os.path.join(this_dir, "data/firstnames", 'yob' + str(year) + '.txt')

    population = []
    with open(DATA_PATH, 'r') as f:
        for line in f:
            splitLine = line.rstrip('\n').split(',')
            if splitLine[1] == gender:
                population.append(int(splitLine[2]))

    return max(population)
