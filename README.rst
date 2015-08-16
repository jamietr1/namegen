Namegen
-------
This package will generate random names for:

* People
* Cities
* Teams

It was developed as part of my baseball_century simulation for generating a realistic set of names for players, and allow name trends to change over time.

# Installation

# Features

* Will generate names for people using [Social Security Administration data](http://www.ssa.gov/oact/babynames/limits.html) from 1880 - 2014.
* Name generation is weighted by popularity in the given year. That is, if "Michael" was the most popular name in a year, it will be generated more frequently in that year.
* Popularity is based on the SSA data for how many occurences of the name they have on record.
* Surname data is taken from (need reference)
* Gender can be specified when generating names
* For names that contain diminutives (e.g. Mike for Michael), there is a 50/50 chance that a diminutive will be included with the name. If a diminutive is to be included and there is more than one possibility, the diminutive is randomly selected.

# Usage

## Within python code


## From the command-line


# Data Sources
