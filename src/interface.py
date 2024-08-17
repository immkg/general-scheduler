from range_constraints import *
from utils import *
from ComfortImplications import *
from StandardImplications import *
from Parser import *
from utils import *
from StaticVariables import *
from tabulate import tabulate

def simple_interface(input_dict):

    StaticVariables.duration = input_dict[duration]

    for (t, s, g, n) in StaticVariables.duration.keys():
        StaticVariables.num_t = max([StaticVariables.num_t, t+1])
        StaticVariables.num_s = max([StaticVariables.num_s, s+1])
        StaticVariables.num_g = max([StaticVariables.num_g, g+1])

    StaticVariables.teachers = np.array(range(StaticVariables.num_t))
    StaticVariables.subjects = np.array(range(StaticVariables.num_s))
    StaticVariables.groups = np.array(range(StaticVariables.num_g))  
    StaticVariables.p_max = input_dict(p_max)
    StaticVariables.days = input_dict(days)
    StaticVariables.periods = [np.array(range(p_max)) for _ in range(len(days))]
    
    x = StandardImplications()
    x.init_vars()
    x.basic_implications()
    x.correctness_implications()
    x.format_result()
    z = Parser([x.graph], [x.true_list])
    z.compute_result(1)

    return simple_ttable(z.result_graphs[0]['xtsgndp'][True])


    #print 'x!tsgndp: ', len(z.result_graphs[0]['x!tsgndp'][True]), len(StaticVariables.duration)
    #print 'xtsgndp: ', len(z.result_graphs[0]['xtsgndp'][True]), np.sum([x for x in StaticVariables.duration.values()])


    # courses = {}

    # for (t, s, g, n) in StaticVariables.duration.keys():
    #     courses[(t, s)] = []

    # bdf = [x for x in courses.keys()]
    # for x in range(len(courses)):
    #     courses[bdf[x]] = 'ID ' + str(x)

    # for sol in z.result_graphs:
    #     result_graph = z.result_graphs[sol]
    #     scheduled = result_graph['xtsgndp'][True]
    
    # ttable = [[ [] for i in range(StaticVariables.p_max) ] for i in range(len(StaticVariables.days))]
    
    # for (t, s, g, n, d, p) in scheduled:
    #     if courses[(t, s)] not in ttable[d][p]:
    #         ttable[d][p].append(courses[(t, s)])
        
    # for i in range(len(ttable)):
    #     ttable[i].insert(0, "Day {}".format(str(i)))
    
    # print tabulate(ttable, headers=["X"]+range(StaticVariables.p_max), tablefmt='fancy_grid').encode('utf-8')

    # g = [x for x in z.result_graphs]
    # A = [[] for x in range(len(g))]
    
    # for i in range(len(g)):
    #     for j in range(len(g)):
    #         A[i].append((g[i] == g[j]))
    
    # for i in A:
    #     print 
    #     print i
