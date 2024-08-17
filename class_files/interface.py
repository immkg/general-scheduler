from range_constraints import *
from utils import *
from ComfortImplications import *
from StandardImplications import *
from Parser import *
from utils import *
from StaticVariables import *
from tabulate import tabulate

def simple_interface(input_dict):

    StaticVariables.duration = input_dict['duration']

    for (t, s, g, n) in StaticVariables.duration.keys():
        StaticVariables.num_t = max([StaticVariables.num_t, t+1])
        StaticVariables.num_s = max([StaticVariables.num_s, s+1])
        StaticVariables.num_g = max([StaticVariables.num_g, g+1])

    StaticVariables.teachers = np.array(range(StaticVariables.num_t))
    StaticVariables.subjects = np.array(range(StaticVariables.num_s))
    StaticVariables.groups = np.array(range(StaticVariables.num_g))
    StaticVariables.p_max = input_dict['p_max']
    StaticVariables.days = range(input_dict['d_max'])
    StaticVariables.periods = [np.array(range(StaticVariables.p_max)) for _ in range(len(StaticVariables.days))]
 
    for i in StaticVariables.days:
        StaticVariables.periods[i] = [j for j in range(StaticVariables.p_max)]
  
    
    x = StandardImplications()
    x.init_vars()
    x.basic_implications()
    x.correctness_implications()
    x.format_result()
    z = Parser([x.graph], [x.true_list])
    z.compute_result(1)

    return simple_ttable(z.result_graphs[0]['xtsgndp'][True])

def interface(input_dict):

    StaticVariables.duration = input_dict['duration']

    for (t, s, g, n) in StaticVariables.duration.keys():
        StaticVariables.num_t = max([StaticVariables.num_t, t+1])
        StaticVariables.num_s = max([StaticVariables.num_s, s+1])
        StaticVariables.num_g = max([StaticVariables.num_g, g+1])

    StaticVariables.teachers = np.array(range(StaticVariables.num_t))
    StaticVariables.subjects = np.array(range(StaticVariables.num_s))
    StaticVariables.groups = np.array(range(StaticVariables.num_g))
    StaticVariables.p_max = input_dict['p_max']
    StaticVariables.days = range(input_dict['d_max'])
    StaticVariables.periods = [np.array(range(StaticVariables.p_max)) for _ in range(len(StaticVariables.days))]
    for i in StaticVariables.days:
        StaticVariables.periods[i] = [j for j in range(StaticVariables.p_max)]
  
    
    x = StandardImplications()
    x.init_vars()
    x.basic_implications()
    x.correctness_implications()
    x.format_result()
    y = ComfortImplications()
    print input_dict['teacher_forbidden0']
    print (not [])
    y.teacher_forbidden(teacher_forbidden0 = input_dict['teacher_forbidden0'],
                       teacher_forbidden1 = input_dict['teacher_forbidden1'],
                       teacher_forbidden2 = input_dict['teacher_forbidden2'])
    print y.comfort_true_list

    y.teacher_requested(teacher_requested0 = input_dict['teacher_requested0'],
                       teacher_requested1 = input_dict['teacher_requested1'],
                       teacher_requested2 = input_dict['teacher_requested2'])

    y.group_forbidden(group_forbidden0 = input_dict['group_forbidden0'],
                     group_forbidden1 = input_dict['group_forbidden1'],
                     group_forbidden2 = input_dict['group_forbidden2'])

    y.group_requested(group_requested0 = input_dict['group_requested0'],
                     group_requested1 = input_dict['group_requested1'],
                     group_requested2 = input_dict['group_requested2'])

    y.overlaps(teacher_overlap = input_dict['teacher_overlap'],
               teacher_no_overlap = input_dict['teacher_no_overlap'],
               group_no_overlap = input_dict['group_no_overlap'])

    y.teaching_days(teaching_days = input_dict['teaching_days'])

    y.duration(work_day_duration = input_dict['work_day_duration'],
               duration_upper_limit = input_dict['duration_upper_limit'],
               duration_lower_limit = input_dict['duration_lower_limit'])

    y.idle_duration(teacher_max_idle_length = input_dict['teacher_max_idle_length'],
                   teacher_atmost_one_idle_period = input_dict['teacher_atmost_one_idle_period'],
                   teacher_atmost_k_idle_period = input_dict['teacher_atmost_k_idle_period'],
                   group_max_idle_length = input_dict['group_max_idle_length'],
                   group_atmost_one_idle_period = input_dict['group_atmost_one_idle_period'],
                   group_atmost_k_idle_period = input_dict['group_atmost_k_idle_period'])

    y.hour_specification(favoured_hours = input_dict['favoured_hours'],
                        last_first_hours = input_dict['last_first_hours'])

    y.non_consecutive(non_consecutive = input_dict['non_consecutive'])
    print y.comfort_true_list
    y.format_result()
    print y.comfort_true_list
    z = Parser([x.graph, y.comfort_graph], [x.true_list, y.comfort_true_list])
    z.compute_result(1)

    print z.result_graphs.keys()
    
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
