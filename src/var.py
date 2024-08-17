import numpy as np

max_sol = 3
true_list = []
graph = {}

graph['x!tsgndp'] = {}
graph['xtsgndp'] = {}
graph['xtsgnd'] = {}
graph['xtdp'] = {}
graph['xgdp'] = {}
graph['xtd'] = {}
graph['xtp'] = {}
graph['iktdp'] = {}
graph['iktd'] = {}
graph['ikt'] = {}
graph['ikgdp'] = {}
graph['ikgd'] = {}
graph['ikg'] = {}
graph['itdp'] = {}
graph['igdp'] = {}

num_t = 0
num_s = 0
num_g = 0
p_max = 0
#n_max = 4

days = range(6)

periods = []
for _ in days:
    periods.append([0, 1, 2, 3, 4, 5, 6, 7])
    
#periods[0] = [0, 1, 3]
#periods[2] = [0, 1, 2]
#periods[5] = [0, 1, 4, 5, 6, 7]

for p in periods:
    p_max = max([p_max, max(p)+1])

'''
duration = {
    (t, s, g, n): 3
}
'''
duration = {
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

courses = {}

for (t, s, g, n) in duration.keys():
    courses[(t, s)] = []

bdf = [x for x in courses.keys()]
for x in range(len(courses)):
    courses[bdf[x]] = 'ID ' + str(x)

for (t, s, g, n) in duration.keys():
    num_t = max([num_t, t+1])
    num_s = max([num_s, s+1])
    num_g = max([num_g, g+1])

teachers = np.array(range(num_t))
subjects = np.array(range(num_s))
groups = np.array(range(num_g))   

'''
lessons of t
lessons_t[t] = [(t, s, g, n)]
'''
def compute_lessons():
    lessons_t = [[] for _ in range(num_t)]
    lessons_g = [[] for _ in range(num_g)]
    for x in duration.keys():
        lessons_t[x[0]].append(x)
        lessons_g[x[2]].append(x)
    return (lessons_t, lessons_g)

(lessons_t, lessons_g) = compute_lessons()

comfort_graph = {}
comfort_graph['xtdp'] = {}
comfort_graph['xtsgnd'] = {}
comfort_graph['x!tsgndp'] = {}
comfort_graph['xtd'] = {}
comfort_graph['xtp'] = {}
comfort_graph['xgdp'] = {}
comfort_graph['xgd'] = {}
comfort_graph['xgp'] = {}
comfort_graph['lkgd'] = {}


comfort_true_list = []


'''
Sketch

teacher_forbidden0 = [(t, d, p)]
teacher_forbidden1 = [(t, d)]
teacher_forbidden2 = [(t, p)]

teacher_requested0 = [(t, d, p)]
teacher_requested1 = [(t, d)]
teacher_requested2 = [(t, p)]

group_forbidden0 = [(g, d, p)]
# group_forbidden1 = [(g, d)]
# group_forbidden2 = [(g, p)]

group_requested0 = [(g, d, p)]
# group_requested1 = [(g, d)]
# group_requested2 = [(g, p)]

teacher_no_overlap = [(t1, t2)]
teacher_overlap = [(t1, t2)]
group_no_overlap = [(g1, g2)]

teaching_days = [(t, n)]        # n <= d
no_of_days = len(days)

work_day_duration = [(g, k, d)]

duration_upper_limit = [(g, d, n)]

duration_lower_limit = [(g, d, n)]

teacher_max_idle_length = [(t, k)]
teacher_atmost_one_idle_period = [t]
teacher_atmost_k_idle_period = [(t, k)]

group_max_idle_length = [(g, k)]
group_atmost_one_idle_period = [g]
group_atmost_k_idle_period = [(g, k)]

favoured_hours = {(t,s,g,n, d):[p]}
last_first_hours = [(t,s,g,n)]
'''
