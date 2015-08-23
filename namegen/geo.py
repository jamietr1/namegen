import collections
import random
import os
import MySQLdb as mdb

def get_random_state(region):
    # Randomly selects a state based on the distribution of the poplation of all states
    con = mdb.connect('localhost', 'bc', 'rand5725', 'Baseball')
    #SQL = "select State, MAX(Cumulative) from bs_Geography grou by State order by MAX(Cumulative) DESC limit 1;"

    SQL = "set @csum := 0;"


    with con:
        cur = con.cursor()
        SQL = "set @csum := 0;"
        cur.execute(SQL)
        SQL = "select Pop.s as State, (@csum := @csum + Pop.p) +1 - Pop.p as Min, (@csum := @csum + Pop.p) as Max from (select State as s, SUM(Population) as p from bs_Geography group by s ORDER BY 2) as Pop order by 2 DESC limit 1;"
        cur.execute(SQL)
        row = cur.fetchone()
        max_pop = row[2]

    roll = random.randint(1, max_pop)

    with con:
        cur = con.cursor()
        SQL = "set @csum := 0;"
        cur.execute(SQL)
        SQL = "select Pop.s as State, (@csum := @csum + Pop.p) +1 - Pop.p as Min, (@csum := @csum + Pop.p) as Max from (select State as s, SUM(Population) as p from bs_Geography group by s ORDER BY 2) as Pop where '" + str(roll) + "' between (@csum := @csum + Pop.p) +1 - Pop.p and (@csum := @csum + Pop.p);"
        cur.execute(SQL)
        row = cur.fetchone()
        random_state = row[0]
    if con:
        con.close()

    return random_state

def get_random_city(statename):
    if statename == '':
        statename = get_random_state('')

    con = mdb.connect('localhost', 'bc', 'rand5725', 'Baseball')
    SQL = "set @csum := 0;"

    with con:
        cur = con.cursor()
        SQL = "set @csum := 0;"
        cur.execute(SQL)

        SQL = "select Pop.s as City, (@csum := @csum + Pop.p) +1 - Pop.p as Min, (@csum := @csum + Pop.p) as Max from (select City as s, SUM(Population) as p	from bs_Geography where State = '" + statename + "' group by s ORDER BY 2) as Pop order by 2 desc limit 1;"

        cur.execute(SQL)
        row = cur.fetchone()
        max_pop = row[2]

        roll = random.randint(1, max_pop)

    with con:
        cur = con.cursor()
        SQL = "set @csum := 0;"
        cur.execute(SQL)

        SQL = "select Pop.s as City, (@csum := @csum + Pop.p) +1 - Pop.p as Min, (@csum := @csum + Pop.p) as Max from (select City as s, SUM(Population) as p from bs_Geography where state = '" + statename + "' group by s ORDER BY 2) as Pop where '" + str(roll) + "' between (@csum := @csum + Pop.p) +1 - Pop.p and (@csum := @csum + Pop.p);"

        cur.execute(SQL)
        row = cur.fetchone()
        city_name = row[0]

    if con:
        con.close()

    return city_name
