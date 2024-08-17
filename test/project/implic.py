from cons import *

# initializing vars


for (t, s, g, n) in list(duration.keys()):
    for d in days:
        graph2['xtsgnd'][(t, s, g, n, d)] = []
        for p in periods[d]:
            graph2['x!tsgndp'][(t, s, g, n, d, p)] = []
            graph2['xtsgndp'][(t, s, g, n, d, p)] = []


for t in teachers:
    for d in days:
        graph2['xtd'][(t, d)] = []
        for p in periods[d]:
            graph2['xtdp'][(t, d, p)] = []

for t in teachers:
    for p in range(p_max):
        graph2['xtp'][(t, p)] = []

for g in groups:
    for d in days:
        for p in periods[d]:
            graph2['xgdp'][(g, d, p)] = []


for k in range(
        1,
        p_max +
        1):  # should it not be from 1 to pmax rather than from 0 to pmax - 1
    # Yes it sould be from 1 to p_max - 1. -- SOLVED
    for t in teachers:
        graph2['ikt'][(k, t)] = []
        for d in days:
            if bic9(k, d):
                graph2['iktd'][(k, t, d)] = []
            for p in periods[d]:
                if bic8(k, d, p):
                    graph2['iktdp'][(k, t, d, p)] = []

for k in range(1, p_max + 1):
    for g in groups:
        graph2['ikg'][(k, g)] = []
        for d in days:
            if bic9(k, d):
                graph2['ikgd'][(k, g, d)] = []
            for p in periods[d]:
                if bic8(k, d, p):
                    graph2['ikgdp'][(k, g, d, p)] = []


for t in teachers:
    for d in days:
        for p in periods[d]:
            if bic11(d, p):
                graph2['itdp'][(t, d, p)] = []

for g in groups:
    for d in days:
        for p in periods[d]:
            if bic11(d, p):
                graph2['igdp'][(g, d, p)] = []


# Implications

for (t, s, g, n, d, p1) in list(graph2['x!tsgndp'].keys()):
    for p2 in periods[d]:
        if bic1(t, s, g, n, d, p1, p2):
            graph2['x!tsgndp'][(t, s, g, n, d, p1)].append(
                ('xtsgndp', (t, s, g, n, d, p2))
            )

for (t, s, g, n, d, p2) in list(graph2['xtsgndp'].keys()):
    if bic3(d, p2):  # required ?...
        or_list = []
        for p1 in periods[d]:
            if bic2(t, s, g, n, d, p1, p2):
                or_list.append(('x!tsgndp', (t, s, g, n, d, p1)))
        if len(or_list) > 0:
            graph2['xtsgndp'][(t, s, g, n, d, p2)].append(('or', or_list))


for (t, s, g, n, d, p) in list(graph2['xtsgndp'].keys()):
    graph2['xtsgndp'][(t, s, g, n, d, p)].append(('xtsgnd', (t, s, g, n, d)))
    graph2['xtsgndp'][(t, s, g, n, d, p)].append(('xtdp', (t, d, p)))
    graph2['xtsgndp'][(t, s, g, n, d, p)].append(('xgdp', (g, d, p)))


for (t, s, g, n, d) in list(graph2['xtsgnd'].keys()):
    or_list = []
    for p in periods[d]:
        or_list.append(('xtsgndp', (t, s, g, n, d, p)))
    if len(or_list) > 0:
        graph2['xtsgnd'][(t, s, g, n, d)].append(('or', or_list))


or_list_t = {}

or_list_g = {}

for (t, d, p) in list(graph2['xtdp'].keys()):
    or_list_t[(t, d, p)] = []

for (g, d, p) in list(graph2['xgdp'].keys()):
    or_list_g[(g, d, p)] = []

for (t, s, g, n, d, p) in list(graph2['xtsgndp'].keys()):
    or_list_t[(t, d, p)].append(('xtsgndp', (t, s, g, n, d, p)))
    or_list_g[(g, d, p)].append(('xtsgndp', (t, s, g, n, d, p)))

for (t, d, p) in list(graph2['xtdp'].keys()):
    graph2['xtdp'][(t, d, p)].append(('xtd', (t, d)))
    graph2['xtdp'][(t, d, p)].append(('xtp', (t, p)))
    if len(or_list_t[(t, d, p)]) > 0:
        graph2['xtdp'][(t, d, p)].append(('or', or_list_t[(t, d, p)]))

for (g, d, p) in list(graph2['xgdp'].keys()):
    if len(or_list_g[(g, d, p)]) > 0:
        graph2['xgdp'][(g, d, p)].append(('or', or_list_g[(g, d, p)]))


for (t, d) in list(graph2['xtd'].keys()):
    or_list = []
    for p in periods[d]:
        or_list.append(('xtdp', (t, d, p)))
    if len(or_list) > 0:
        graph2['xtd'][(t, d)].append(('or', or_list))

for (t, p) in list(graph2['xtp'].keys()):
    or_list = []
    for d in days:
        if bic3(d, p):  # if p in periods[d]:
            or_list.append(('xtdp', (t, d, p)))
    if len(or_list) > 0:
        graph2['xtp'][(t, p)].append(('or', or_list))


for (k, t, d, p) in list(graph2['iktdp'].keys()):
    graph2['iktdp'][(k, t, d, p)].append(('xtdp', (t, d, p - 1)))
    for j in range(k):
        graph2['iktdp'][(k, t, d, p)].append(('~xtdp', (t, d, p + j)))
    graph2['iktdp'][(k, t, d, p)].append(('xtdp', (t, d, p + k)))
    true_list.append(
        ('or', [
                    ('~xtdp', (t, d, p - 1)),
                    ('or', or_list),    # ?
                    ('~xtdp', (t, d, p + k)),
                    ('~iktdp', (k, t, d, p))
        ]))

    graph2['iktdp'][(k, t, d, p)].append(('iktd', (k, t, d)))

for (k, t, d) in list(graph2['iktd'].keys()):
    or_list = []
    for p in periods[d]:
        if bic10(k, d, p):
            or_list.append(('iktdp', (k, t, d, p)))
    if len(or_list) > 0:
        graph2['iktd'][(k, t, d)].append(('or', or_list))

    graph2['iktd'][(k, t, d)].append(('ikt', (k, t)))

    graph2['iktd'][(k, t, d)].append(('itdp', (t, d, p)))

for (k, t) in list(graph2['ikt'].keys()):
    or_list = []
    for d in days:
        or_list.append(('iktd', (k, t, d)))
    if len(or_list) > 0:
        graph2['ikt'][(k, t)].append(('or', or_list))

for (t, d, p) in list(graph2['itdp'].keys()):
    or_list = []
    for k in range(p_max):
        if bic12(k, d, p):
            or_list.append(('iktdp', (k, t, d, p)))
    if len(or_list) > 0:
        graph2['itdp'][(t, d, p)].append(('or', or_list))

# ================ EXACTLY SAME FOR GROUPS =================
# Abstract this somehow!


for (k, g, d, p) in list(graph2['ikgdp'].keys()):
    graph2['ikgdp'][(k, g, d, p)].append(('xgdp', (g, d, p - 1)))
    for j in range(k):
        graph2['ikgdp'][(k, g, d, p)].append(('~xgdp', (g, d, p + j)))
    graph2['ikgdp'][(k, g, d, p)].append(('xgdp', (g, d, p + k)))
    true_list.append(
        ('or', [
                    ('~xgdp', (g, d, p - 1)),
            # ? ('or', or_list),
                    ('~xgdp', (g, d, p + k)),
                    ('~ikgdp', (k, g, d, p))
        ]))

    graph2['ikgdp'][(k, g, d, p)].append(('ikgd', (k, g, d)))

for (k, g, d) in list(graph2['ikgd'].keys()):
    or_list = []
    for p in periods[d]:
        if bic10(k, d, p):
            or_list.append(('ikgdp', (k, g, d, p)))
    graph2['ikgd'][(k, g, d)].append(('or', or_list))

    graph2['ikgd'][(k, g, d)].append(('ikg', (k, g)))

    graph2['ikgd'][(k, g, d)].append(('igdp', (g, d, p)))

for (k, g) in list(graph2['ikg'].keys()):
    or_list = []
    for d in days:
        or_list.append(('ikgd', (k, g, d)))
    if len(or_list) > 0:
        graph2['ikg'][(k, g)].append(('or', or_list))

for (g, d, p) in list(graph2['igdp'].keys()):
    or_list = []
    for k in range(p_max):
        if bic12(k, d, p):
            or_list.append(('ikgdp', (k, g, d, p)))
    if len(or_list) > 0:
        graph2['igdp'][(g, d, p)].append(('or', or_list))


# Correctness constraints

for (t, s, g, n) in list(duration.keys()):
    or_list = []
    for d in days:
        or_list.append(('xtsgnd', (t, s, g, n, d)))
    if len(or_list) > 0:
        true_list.append(('or', or_list))


multi_dict = {}
for (t, s, g, n, d) in list(graph2['xtsgnd'].keys()):
    multi_dict[(t, s, g, n)] = []
for (t, s, g, n, d) in list(graph2['xtsgnd'].keys()):
    multi_dict[(t, s, g, n)].append(('xtsgnd', (t, s, g, n, d)))
for (t, s, g, n) in list(multi_dict.keys()):
    true_list.append(single(multi_dict[(t, s, g, n)]))


multi_dict = {}
for (t, s, g, n, d, p) in list(graph2['x!tsgndp'].keys()):
    multi_dict[(t, s, g, n, d)] = []
for (t, s, g, n, d, p) in list(graph2['x!tsgndp'].keys()):
    multi_dict[(t, s, g, n, d)].append(('x!tsgndp', (t, s, g, n, d, p)))
for (t, s, g, n, d) in list(multi_dict.keys()):
    true_list.append(single(multi_dict[(t, s, g, n, d)]))


multi_dict = {}
for (t, s, g, n, d, p) in list(graph2['xtsgndp'].keys()):
    multi_dict[(g, d, p)] = []
for (t, s, g, n, d, p) in list(graph2['xtsgndp'].keys()):
    multi_dict[(g, d, p)].append(('xtsgndp', (t, s, g, n, d, p)))
for (g, d, p) in list(multi_dict.keys()):
    true_list.append(single(multi_dict[(g, d, p)]))


'''
Assume all groups can be interleaved
The overlapping can be removied using the comfort conditions.
'''

multi_dict = {}
for (t, s, g, n, d, p) in list(graph2['xtsgndp'].keys()):
    multi_dict[(t, d, p)] = {}
for (t, s, g, n, d, p) in list(graph2['xtsgndp'].keys()):
    multi_dict[(t, d, p)][(s, n)] = []
for (t, s, g, n, d, p) in list(graph2['xtsgndp'].keys()):
    multi_dict[(t, d, p)][(s, n)].append(('xtsgndp', (t, s, g, n, d, p)))
for (t, d, p) in list(multi_dict.keys()):
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
                append_list = multi_dict[(t, d, p)][(
                    s, n)][:i - 1] + multi_dict[(t, d, p)][(s, n)][i + 1:]
            graph2['xtsgndp'][multi_dict[(t, d, p)]
                              [(s, n)][i][1]] += append_list
    true_list.append(single(single_list))


'''
Check the previous 2 implications.
'''


# t = 0
# for x in graph2.keys():
#     t += len(graph2[x])

# for x in graph2.keys():
#     for y in graph2[x].keys():
#         print (x, y, graph2[x][y])

# for x in true_list:
#     print x

# print(len(graph2.keys()))
# for x in graph.keys():
# 	print(x, '=>' ,graph2[x])


'''
graph2[('x', t, s, g, n, d, p)] = [('or', [...])]
'''
