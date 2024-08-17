from parser import *
from tabulate import tabulate

scheduled = truth_dict2['xtsgndp']

ttable = [[[] for i in range(len(periods))] for i in range(len(days))]

for x in scheduled:
    cl = list(map(int, x.replace('(', '').replace(')', '').split(',')))
    ttable[cl[4]][cl[5]].append(cl[:-2])

for i in range(len(ttable)):
    ttable[i].insert(0, "Day" + str(i))

print(tabulate(ttable, headers=["X"] + periods[0], tablefmt='fancy_grid'))
