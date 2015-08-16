# A module for generating play names based on a relative year, and weighted by
# popularity in that year. I think this gives the naming a more realistic
# feel when a simulation is run over 100 seasons.
import collections
import random
import os

from .person import get_random_firstname
from .person import get_random_diminutive
from .person import get_random_surname
from .person import get_random_fullname
from .geo import get_random_city
from .geo import get_random_state
