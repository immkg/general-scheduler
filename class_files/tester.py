from StaticVariables import *

StaticVariables.duration = {
    (0, 0, 0, 1): 3,
    (0, 0, 1, 2): 3,
    (0, 0, 2, 3): 3,
    (0, 0, 3, 4): 3,
    (1, 1, 0, 1): 2,
    (1, 1, 1, 2): 2,
    (1, 1, 2, 3): 2,
    (1, 1, 3, 4): 2,
    (2, 2, 0, 1): 1,
    (2, 2, 1, 1): 1,
    (2, 2, 2, 1): 1,
    (2, 2, 3, 1): 1,
    (2, 2, 0, 2): 1,
    (2, 2, 1, 2): 1,
    (2, 2, 2, 2): 1,
    (2, 2, 3, 2): 1,
    (2, 2, 0, 3): 1,
    (2, 2, 1, 3): 1,
    (2, 2, 2, 3): 1,
    (2, 2, 3, 3): 1,
    (2, 2, 0, 4): 1,
    (2, 2, 1, 4): 1,
    (2, 2, 2, 4): 1,
    (2, 2, 3, 4): 1,
    (3, 3, 0, 1): 1,
    (3, 3, 1, 1): 1,
    (3, 3, 0, 2): 1,
    (3, 3, 1, 2): 1,
    (3, 3, 0, 3): 1,
    (3, 3, 1, 3): 1,
    (4, 3, 2, 1): 1,
    (4, 3, 3, 1): 1,
    (4, 3, 2, 2): 1,
    (4, 3, 3, 2): 1,
    (4, 3, 2, 3): 1,
    (4, 3, 3, 3): 1, 
    (5, 4, 0, 1): 1,
    (5, 4, 1, 1): 1,
    (5, 4, 1, 2): 1,
    (5, 4, 1, 2): 1,
    (5, 4, 0, 3): 1,
    (5, 4, 1, 3): 1,
    (5, 4, 0, 4): 1,
    (5, 4, 1, 4): 1,
    (6, 4, 2, 1): 1,
    (6, 4, 3, 1): 1,
    (6, 4, 2, 2): 1,
    (6, 4, 3, 2): 1,
    (6, 4, 2, 3): 1,
    (6, 4, 2, 3): 1,
    (6, 4, 2, 4): 1,
    (6, 4, 3, 4): 1,
    (7, 5, 0, 1): 1,
    (7, 5, 1, 1): 1,
    (7, 5, 0, 2): 1,
    (7, 5, 1, 2): 1,
    (7, 5, 0, 3): 1,
    (7, 5, 1, 3): 1,
    (8, 5, 2, 1): 1,
    (8, 5, 3, 1): 1,
    (8, 5, 2, 2): 1,
    (8, 5, 3, 2): 1,
    (8, 5, 2, 3): 1,
    (8, 5, 3, 3): 1,
    (9, 6, 0, 1): 1,
    (9, 6, 1, 1): 1,
    (9, 6, 0, 2): 1,
    (9, 6, 1, 2): 1,
    (9, 6, 0, 3): 1,
    (9, 6, 1, 3): 1,
    (10, 6, 2, 1): 1,
    (10, 6, 3, 1): 1,
    (10, 6, 2, 2): 1,
    (10, 6, 3, 2): 1,
    (10, 6, 2, 3): 1,
    (10, 6, 3, 3): 1,
    (11, 7, 0, 1): 2,
    (11, 7, 1, 1): 2,
    (11, 7, 2, 1): 2,
    (11, 7, 3, 1): 2,
    (12, 8, 0, 1): 3,
    (12, 8, 1, 1): 3,
    (12, 8, 2, 1): 3,
    (12, 8, 3, 1): 3,    
    
    
}

for (t, s, g, n) in StaticVariables.duration.keys():
    StaticVariables.num_t = max([StaticVariables.num_t, t+1])
    StaticVariables.num_s = max([StaticVariables.num_s, s+1])
    StaticVariables.num_g = max([StaticVariables.num_g, g+1])

StaticVariables.teachers = np.array(range(StaticVariables.num_t))
StaticVariables.subjects = np.array(range(StaticVariables.num_s))
StaticVariables.groups = np.array(range(StaticVariables.num_g))  



from range_constraints import *
from utils import *
from ComfortImplications import *
from StandardImplications import *
from Parser import *
from utils import *

from tabulate import tabulate

x = StandardImplications()
x.init_vars()
x.basic_implications()
x.correctness_implications()
x.format_result()
z = Parser([x.graph], [x.true_list])
z.compute_result(1)
print 'x!tsgndp: ', len(z.result_graphs[0]['x!tsgndp'][True]), len(StaticVariables.duration)
print 'xtsgndp: ', len(z.result_graphs[0]['xtsgndp'][True]), np.sum([x for x in StaticVariables.duration.values()])

print simple_ttable(z.result_graphs[0]['xtsgndp'][True])

from tabulate import tabulate

courses = {}

for (t, s, g, n) in StaticVariables.duration.keys():
    courses[(t, s)] = []

bdf = [x for x in courses.keys()]
for x in range(len(courses)):
    courses[bdf[x]] = 'ID ' + str(x)

for sol in z.result_graphs:
    result_graph = z.result_graphs[sol]
    scheduled = result_graph['xtsgndp'][True]
    
    ttable = [[ [] for i in range(StaticVariables.p_max) ] for i in range(len(StaticVariables.days))]
    
    for (t, s, g, n, d, p) in scheduled:
        if courses[(t, s)] not in ttable[d][p]:
            ttable[d][p].append(courses[(t, s)])
        
    for i in range(len(ttable)):
        ttable[i].insert(0, "Day {}".format(str(i)))
    
    print tabulate(ttable, headers=["X"]+range(StaticVariables.p_max), tablefmt='fancy_grid').encode('utf-8')

g = [x for x in z.result_graphs]
A = [[] for x in range(len(g))]

for i in range(len(g)):
    for j in range(len(g)):
        A[i].append((g[i] == g[j]))

for i in A:
    print 
    print i
