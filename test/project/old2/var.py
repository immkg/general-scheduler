import numpy as np

graph = {}
true_list = []

graph2 = {}
graph2['x!tsgndp'] = {}
graph2['xtsgndp'] = {}
graph2['xtsgnd'] = {}
graph2['xtdp'] = {}
graph2['xgdp'] = {}
graph2['xtd'] = {}
graph2['xtp'] = {}
graph2['iktdp'] = {}
graph2['iktd'] = {}
graph2['ikt'] = {}
graph2['ikgdp'] = {}
graph2['ikgd'] = {}
graph2['ikg'] = {}
graph2['itdp'] = {}
graph2['igdp'] = {}

num_t = 10
num_s = 10
num_g = 10
n_max = 4
p_max = 6

teachers = np.array(list(range(num_t)))
subjects = np.array(list(range(num_s)))
groups = np.array(list(range(num_g)))

days = list(range(6))
periods = []
for _ in days:
    periods.append([0, 1, 2, 3, 4, 5])
periods[0] = [0, 1, 2, 3]


_duration = np.ones([num_t, num_s, num_g, n_max])

'''
duration = {
    (t, s, g, n): 3
}
'''
duration = {
    (0, 0, 0, 0): 2,
    (0, 1, 0, 0): 3,
    (1, 1, 0, 0): 3,
    (1, 1, 1, 1): 3
}

'''
lessons of t
lessons_t[t] = [(t, s, g, n)]
'''


def compute_lessons():
    lessons_t = [[] for _ in range(num_t)]
    lessons_g = [[] for _ in range(num_g)]
    for x in list(duration.keys()):
        lessons_t[x[0]].append(x)
        lessons_g[x[2]].append(x)
    return (lessons_t, lessons_g)


(lessons_t, lessons_g) = compute_lessons()
