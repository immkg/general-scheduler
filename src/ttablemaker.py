from parser import *
from tabulate import tabulate

for sol in all_result:
    result_graph = all_result[sol]
    scheduled = result_graph['xtsgndp'][True]
    
    ttable = [[ [] for i in range(p_max) ] for i in range(len(days))]
    
    for (t, s, g, n, d, p) in scheduled:
        if courses[(t, s)] not in ttable[d][p]:
            ttable[d][p].append(courses[(t, s)])
        
    for i in range(len(ttable)):
        ttable[i].insert(0, "Day {}".format(str(i)))
    
    print tabulate(ttable, headers=["X"]+range(p_max), tablefmt='fancy_grid').encode('utf-8')

g = [x for x in all_result]
A = [[] for x in range(len(g))]

for i in range(len(g)):
    for j in range(len(g)):
        A[i].append((g[i] == g[j]))

for i in A:
    print 
    print i
