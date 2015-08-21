import collections
import random
import os

def get_random_firstname(year, gender):
    if year < 1880 or year > 2014:
        return ''

    min_val = 0
    if gender == 'M':
        max_val = 108252256
    else:
        max_val = 77608249

    roll = random.randint(1, max_val)

    for record in firstname_list:
        fields = record.split(',')
        if fields[1] == gender:
            max_val = int(fields[2])
            if (roll > min_val) and (roll <= max_val):
                first_name = fields[0]
                break
            min_val = max_val

    # Does the name have a diminutive?
    diminutives = get_random_diminutive(first_name)
    if (diminutives != ''):
        if random.randint(1,100) > 50:
            dim_list = diminutives.split(',')
            diminutive = random.choice(dim_list)
            return first_name + ' (' + diminutive + ')'
        else:
            return first_name
    else:
        return first_name

def get_random_diminutive(name):
    name_dict = {}

    for line in diminutive_list:
        splitLine = line.split(':')
        name_dict[splitLine[0]] = splitLine[1]

    if name in name_dict:
        return name_dict[name].rstrip('\n')
    else:
        return ''

def get_random_surname():
    min_val = 0
    max_val = 60113
    roll = random.randint(1, max_val)


    for line in surname_list:
        splitLine = line.rstrip('\n').split(',')
        max_val = int(splitLine[1])
        if (roll > min_val) and (roll <= max_val):
            surname = splitLine[0]
            break

        min_val = max_val

    return surname.title()

def get_random_fullname(year, gender):
    first_name = get_random_firstname(year, gender)
    last_name = get_random_surname()
    return first_name, last_name

def get_max_population(year, gender, namepart):
    population = []
    if namepart == "firstname":
        for record in firstname_list:
            fields = record.split(',')
            if fields[1] == gender:
                population.append(int(fields[2]))
    else:
        for record in lastname_list:
            fields = record.split(',')
            if fields[1] == gender:
                population.append(int(fields[2]))

    return max(population)

def get_firstnames():
    global firstname_list
    global max_population_m
    global max_population_f
    firstname_list = []
    max_population_m = {}
    max_population_f = {}
    this_dir, this_file = os.path.split(__file__)

    for year in range(1880, 2014):
        DATA_PATH = os.path.join(this_dir, "data/firstnames", 'yob' + str(year) + '.txt')
        with open(DATA_PATH, 'r') as f:
            for line in f:
                line = line.rstrip('\n')
                firstname_list.append(line)

def get_diminutives():
    global diminutive_list
    diminutive_list = []

    this_dir, this_file = os.path.split(__file__)
    DATA_PATH = os.path.join(this_dir, "data/firstnames", 'diminutives.txt')

    with open(DATA_PATH, 'r') as f:
        for line in f:
            line = line.rstrip('\n')
            diminutive_list.append(line)

def get_surnames():
    global surname_list
    surname_list = []

    this_dir, this_file = os.path.split(__file__)
    DATA_PATH = os.path.join(this_dir, "data/surnames", 'surnames.txt')

    with open(DATA_PATH, 'r') as f:
        for line in f:
            line = line.rstrip('\n')
            surname_list.append(line)
