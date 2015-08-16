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
    nameDict = {}
    with open(DATA_PATH, 'r') as f:
        for line in f:
            splitLine = line.split(',')
            if splitLine[1] == gender:
                nameDict[splitLine[0]] = int(splitLine[2])

    # 3. Calcuate the total
    population = sum(nameDict.values())
    census = []
    for name in nameDict:
        for x in range(1, nameDict[name]):
            census.append(name)

    # TODO: Need a diminutive lookup for common names with dims
    #       This would allow for more options

    # 4. Generate the name
    return random.choice(census)

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
