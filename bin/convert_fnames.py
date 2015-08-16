#!/usr/bin/python

import os

def convert_file(file):
    output = ()
    gender = 'F'
    running_total = 0

    new_file = file + '.bak'
    if os.path.isfile(new_file):
        os.remove(new_file)

    with open(file, 'r') as f:
        for line in f:
            splitLine = line.rstrip('\n').split(',')
            if gender != splitLine[1]:
                running_total = 0
                if gender == 'F':
                    gender = 'M'
                else:
                    gender = 'F'
            running_total += int(splitLine[2])
            new_line = splitLine[0] + ',' + splitLine[1] + ',' + str(running_total)

            # write the line to a temp file
            tf = open(new_file, 'a')
            tf.write(new_line + '\n')
            tf.close

    # remove the original and rename the new file
    os.remove(file)
    os.rename(new_file, file)

# This is the main routine

this_dir, this_file = os.path.split(__file__)
DATA_PATH = os.path.join(this_dir, "../namegen/data/firstnames/")

for file in os.listdir(DATA_PATH):
    if (file == "diminutives.txt") or (file == "source.txt") or (file == "yob1972.txt"):
        print "Skipping " + file
    else:
        print "Converting " + file
        convert_file(DATA_PATH + file)
