from var import *
from cons import *

# initializing vars


for (t, s, g, n) in duration.keys():
    for d in days:
        graph['xtsgnd'][(t, s, g, n, d)] = []
        for p in periods[d]:
            graph['x!tsgndp'][(t, s, g, n, d, p)] = []
            graph['xtsgndp'][(t, s, g, n, d, p)] = []


for t in teachers:
    for d in days:
        graph['xtd'][(t, d)] = []
        for p in periods[d]:
            graph['xtdp'][(t, d, p)] = []

for t in teachers:
    for p in range(p_max):
        graph['xtp'][(t, p)] = []

for g in groups:
    for d in days:
        for p in periods[d]:
            graph['xgdp'][(g, d, p)] = []



for k in range(1, p_max + 1): #should it not be from 1 to pmax rather than from 0 to pmax - 1
    # Yes it sould be from 1 to p_max - 1. -- SOLVED
    for t in teachers:
        graph['ikt'][(k, t)] = []
        for d in days:
            if bic9(k, d):
                graph['iktd'][(k, t, d)] = []
                for p in periods[d]:
                    if bic8(k, d, p):
                        graph['iktdp'][(k, t, d, p)] = []

for k in range(1, p_max + 1):
    for g in groups:
        graph['ikg'][(k, g)] = []
        for d in days:
            if bic9(k, d):
                graph['ikgd'][(k, g, d)] = []
                for p in periods[d]:
                    if bic8(k, d, p):
                        graph['ikgdp'][(k, g, d, p)] = []


for t in teachers:
    for d in days:
        for p in periods[d]:
            if bic11(d, p):
                graph['itdp'][(t, d, p)] = []

for g in groups:
    for d in days:
        for p in periods[d]:
            if bic11(d, p):
                graph['igdp'][(g, d, p)] = []


# Implications

for (t, s, g, n, d, p1) in graph['x!tsgndp'].keys():
    for p2 in periods[d]:
        if bic1(t, s, g, n, d, p1, p2):
            graph['x!tsgndp'][(t, s, g, n, d, p1)].append(
                ('xtsgndp', (t, s, g, n, d, p2))
            )

for (t, s, g, n, d, p2) in graph['xtsgndp'].keys():
    or_list = []
    for p1 in periods[d]:
        if bic2(t, s, g, n, d, p1, p2):
            or_list.append(('x!tsgndp', (t, s, g, n, d, p1)))
    graph['xtsgndp'][(t, s, g, n, d, p2)].append(('or', or_list))


for (t, s, g, n, d, p) in graph['xtsgndp'].keys():
    graph['xtsgndp'][(t, s, g, n, d, p)].append(('xtsgnd', (t, s, g, n, d)))
    graph['xtsgndp'][(t, s, g, n, d, p)].append(('xtdp', (t, d, p)))
    graph['xtsgndp'][(t, s, g, n, d, p)].append(('xgdp', (g, d, p)))


for (t, s, g, n, d) in graph['xtsgnd'].keys():
    or_list = []
    for p in periods[d]:
        or_list.append(('xtsgndp', (t, s, g, n, d, p)))
    graph['xtsgnd'][(t, s, g, n, d)].append(('or', or_list))


or_list_t = {}

or_list_g = {}

for (t, d, p) in graph['xtdp'].keys():
    or_list_t[(t, d, p)] = []

for (g, d, p) in graph['xgdp'].keys():
    or_list_g[(g, d, p)] = []

for (t, s, g, n, d, p) in graph['xtsgndp'].keys():
    or_list_t[(t, d, p)].append(('xtsgndp', (t, s, g, n, d, p)))
    or_list_g[(g, d, p)].append(('xtsgndp', (t, s, g, n, d, p)))

for (t, d, p) in graph['xtdp'].keys():
    graph['xtdp'][(t, d, p)].append(('xtd', (t, d)))
    graph['xtdp'][(t, d, p)].append(('xtp', (t, p)))
    graph['xtdp'][(t, d, p)].append(('or', or_list_t[(t, d, p)]))

for (g, d, p) in graph['xgdp'].keys():
    graph['xgdp'][(g, d, p)].append(('or', or_list_g[(g, d, p)]))


for (t, d) in graph['xtd'].keys():
    or_list = []
    for p in periods[d]:
        or_list.append(('xtdp',( t, d, p)))
    graph['xtd'][(t, d)].append(('or', or_list))

for (t, p) in graph['xtp'].keys():
    or_list = []
    for d in days:
        if bic3(d, p):
         	or_list.append(('xtdp', (t, d, p)))
    graph['xtp'][(t, p)].append(('or', or_list))


for (k, t, d, p) in graph['iktdp'].keys():
    graph['iktdp'][(k, t, d, p)].append(('xtdp', (t, d, p - 1)))
    or_list = []
    for j in range(k):
        or_list.append(('xtdp', (t, d, p + j)))
        graph['iktdp'][(k, t, d, p)].append(negation(('xtdp', (t, d, p + j))))
    graph['iktdp'][(k, t, d, p)].append(('xtdp', (t, d, p + k)))
    true_list.append(
        ('or', [
                    negation(('xtdp', (t, d, p - 1))),
                    ('or', or_list),
                    negation(('xtdp', (t, d, p + k))),
                    negation(('iktdp', (k, t, d, p)))
        ]))

    graph['iktdp'][(k, t, d, p)].append(('iktd', (k, t, d)))

for (k, t, d) in graph['iktd'].keys():
    or_list = []
    for p in periods[d]:
        if bic10(k, d, p):
            or_list.append(('iktdp', (k, t, d, p)))
    graph['iktd'][(k, t, d)].append(('or', or_list))

    graph['iktd'][(k, t, d)].append(('ikt', (k, t)))

    graph['iktd'][(k, t, d)].append(('itdp', (t, d, p)))

for (k, t) in graph['ikt'].keys():
    or_list = []
    for d in days:
        or_list.append(('iktd', (k, t, d)))
    graph['ikt'][(k, t)].append(('or', or_list))

for (t, d, p) in graph['itdp'].keys():
    or_list = []
    for k in range(p_max):
        if bic12(k, d, p):
            or_list.append(('iktdp', (k, t, d, p)))
    graph['itdp'][(t, d, p)].append(('or', or_list))

# ================ EXACTLY SAME FOR GROUPS =================
# Abstract this somehow!


for (k, g, d, p) in graph['ikgdp'].keys():
    graph['ikgdp'][(k, g, d, p)].append(('xgdp', (g, d, p - 1)))
    or_list = []
    for j in range(k):
        or_list.append(('xgdp', (g, d, p + j)))
        graph['ikgdp'][(k, g, d, p)].append(negation(('xgdp', (g, d, p + j))))
    graph['ikgdp'][(k, g, d, p)].append(('xgdp', (g, d, p + k)))
    true_list.append(
        ('or', [
                    negation(('xgdp', (g, d, p - 1))),
                    ('or', or_list),
                    negation(('xgdp', (g, d, p + k))),
                    negation(('ikgdp', (k, g, d, p)))
        ]))

    graph['ikgdp'][(k, g, d, p)].append(('ikgd', (k, g, d)))

for (k, g, d) in graph['ikgd'].keys():
    or_list = []
    for p in periods[d]:
        if bic10(k, d, p):
            or_list.append(('ikgdp', (k, g, d, p)))
    graph['ikgd'][(k, g, d)].append(('or', or_list))

    graph['ikgd'][(k, g, d)].append(('ikg', (k, g)))

    graph['ikgd'][(k, g, d)].append(('igdp', (g, d, p)))

for (k, g) in graph['ikg'].keys():
    or_list = []
    for d in days:
        or_list.append(('ikgd', (k, g, d)))
    graph['ikg'][(k, g)].append(('or', or_list))

for (g, d, p) in graph['igdp'].keys():
    or_list = []
    for k in range(p_max):
        if bic12(k, d, p):
            or_list.append(('ikgdp', (k, g, d, p)))
    graph['igdp'][(g, d, p)].append(('or', or_list))


# Correctness constraints

for (t, s, g, n) in duration.keys():
    or_list = []
    for d in days:
        or_list.append(('xtsgnd', (t, s, g, n, d)))
    true_list.append(('or', or_list))


multi_dict = {}
for (t, s, g, n, d) in graph['xtsgnd'].keys():
    multi_dict[(t, s, g, n)] = []
for (t, s, g, n, d) in graph['xtsgnd'].keys():
    multi_dict[(t, s, g, n)].append(('xtsgnd', (t, s, g, n, d)))
for (t, s, g, n) in multi_dict.keys():
    true_list.append(single(multi_dict[(t, s, g, n)]))


multi_dict = {}
for (t, s, g, n, d, p) in graph['x!tsgndp'].keys():
    multi_dict[(t, s, g, n, d)] = []
for (t, s, g, n, d, p) in graph['x!tsgndp'].keys():
    multi_dict[(t, s, g, n, d)].append(('x!tsgndp', (t, s, g, n, d, p)))
for (t, s, g, n, d) in multi_dict.keys():
    true_list.append(single(multi_dict[(t, s, g, n, d)]))



multi_dict = {}
for (t, s, g, n, d, p) in graph['xtsgndp'].keys():
    multi_dict[(g, d, p)] = []
for (t, s, g, n, d, p) in graph['xtsgndp'].keys():
    multi_dict[(g, d, p)].append(('xtsgndp', (t, s, g, n, d, p)))
for (g, d, p) in multi_dict.keys():
    true_list.append(single(multi_dict[(g, d, p)]))


'''
Assume all groups can be interleaved
The overlapping can be removied using the comfort conditions.
'''

multi_dict = {}
for (t, s, g, n, d, p) in graph['xtsgndp'].keys():
    multi_dict[(t, d, p)] = {}
for (t, s, g, n, d, p) in graph['xtsgndp'].keys():
    multi_dict[(t, d, p)][(s, n)] = []
for (t, s, g, n, d, p) in graph['xtsgndp'].keys():
    multi_dict[(t, d, p)][(s, n)].append(('xtsgndp', (t, s, g, n, d, p)))
for (t, d, p) in multi_dict.keys():
    single_list = []
    for (s, n) in multi_dict[(t, d, p)]:
        single_list.append(multi_dict[(t, d, p)][(s, n)][0])
        l = len(multi_dict[(t, d, p)][(s, n)])
        for i in range(l):
            if i == 0:
                append_list = multi_dict[(t, d, p)][(s, n)][1:]
            elif i == l - 1:
                append_list = multi_dict[(t, d, p)][(s, n)][:-1]
            else:
                append_list = multi_dict[(t, d, p)][(s, n)][:i-1] + multi_dict[(t, d, p)][(s, n)][i+1:]
            graph['xtsgndp'][multi_dict[(t, d, p)][(s, n)][i][1]] += append_list
    true_list.append(single(single_list))


'''
Check the previous implication.
'''


filter_graph(graph)
true_list = filter_bool(true_list)


# t = 0
# for x in graph.keys():
#     t += len(graph[x])

# for x in graph.keys():
#     for y in graph[x].keys():
#         print (x, y, graph[x][y])

# for x in true_list:
#     print x

# print(len(graph.keys()))
# for x in graph.keys():
# 	print(x, '=>' ,graph[x])


'''
graph[('x', t, s, g, n, d, p)] = [('or', [...])]
'''
