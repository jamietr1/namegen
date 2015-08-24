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
from .team import get_random_team
<<<<<<< HEAD

# Cache the files on load one time to speed things up
state_list = city_list = {}
firstname_list = diminutive_list = surname_list = []

#get_states()

get_firstnames()
get_diminutives()
get_surnames()
=======
>>>>>>> parent of b9a4f63... Cached city, state, firstname, and surname data on inital load
