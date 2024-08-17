
from cons import *

# initializing vars

for t in teachers:
    for s in subjects:
        for g in groups:
            for n in range(n_max):
                if bic0(t, s, g, n):  # Valid lesson
                    for d in days:
                        graph[('xtsgnd', t, s, g, n, d)] = []
                        for p in periods[d]:
                            graph[('x!tsgndp', t, s, g, n, d, p)] = []
                            graph[('xtsgndp', t, s, g, n, d, p)] = []


for t in teachers:
    for d in days:
        graph[('xtd', t, d)] = []
        for p in periods[d]:
            graph[('xtp', t, p)] = []
            graph[('xtdp', t, d, p)] = []

for g in groups:
    for d in days:
        for p in periods[d]:
            graph[('xgdp', g, d, p)] = []


for t in teachers:
    for d in days:
        for p in periods[p]:
            for k in range(len(periods[p])):
                if bic8(k, d, p):
                    graph[('iktdp', k, t, d, p)] = []
                    graph[('iktd', k, t, d)] = []

for g in groups:
    for d in days:
        for p in periods[p]:
            for k in range(len(periods[p])):
                if bic8(k, d, p):
                    graph[('ikgdp', k, g, d, p)] = []
                    graph[('ikgd', k, g, d)] = []


# Implications

for t in teachers:
    for s in subjects:
        for g in groups:
            for n in range(n_max):
                if bic0(t, s, g, n):  # Valid lesson
                    for d in days:
                        for p1 in periods[d]:
                            for p2 in periods[d]:
                                if bic1(t, s, g, n, d, p1, p2):
                                    graph[('x!tsgndp', t, s, g, n, d, p1)].append(
                                        ('x!tsgndp', t, s, g, n, d, p2))

for t in teachers:
    for s in subjects:
        for g in groups:
            for n in range(n_max):
                if bic0(t, s, g, n):  # Valid lesson
                    for d in days:
                        for p2 in periods[d]:
                            if bic3(d, p2):
                                or_list = []
                                for p1 in periods[d]:
                                    if bic2(t, s, g, n, d, p1, p2):
                                        or_list.append(
                                            ('x!tsgndp', t, s, g, n, d, p1))
                                graph[('xtsgndp', t, s, g, n, d, p2)
                                      ].append(('or', or_list))


for t in teachers:
    for s in subjects:
        for g in groups:
            for n in range(n_max):
                if bic0(t, s, g, n):  # Valid lesson
                    for d in days:
                        or_list = []
                        for p in periods[d]:
                            graph[('xtsgndp', t, s, g, n, d, p)].append(
                                ('xtsgnd', t, s, g, n, d))
                            graph[('xtsgndp', t, s, g, n, d, p)
                                  ].append(('xtdp', t, d, p))
                            graph[('xtsgndp', t, s, g, n, d, p)
                                  ].append(('xgdp', g, d, p))
                            or_list.append(('xtsgndp', t, s, g, n, d, p))
                        graph[('xtsgnd', t, s, g, n, d)].append(
                            ('or', or_list))


for t in teachers:
    for d in days:
        or_list_td = []
        for p in periods[d]:
            graph[('xtdp', t, d, p)].append(('xtd', t, d))
            or_list_td.append(('xtdp', t, d, p))
            or_list = []
            for s in subjects:
                for g in groups:
                    for n in range(n_max):
                        if bic0(t, s, g, n):
                            or_list.append(('xtsgndp', t, s, g, n, d, p))
            graph[('xtdp', t, d, p)].append(('or', or_list))
        graph[('xtd', t, d)].append(('or', or_list_td))


for g in groups:
    for d in days:
        for p in periods[d]:
            or_list = []
            for s in subjects:
                for t in teachers:
                    for n in range(n_max):
                        if bic0(t, s, g, n):
                            or_list.append(('xtsgndp', t, s, g, n, d, p))
            graph[('xgdp', g, d, p)].append(('or', or_list))


print((len(list(graph.keys()))))
print(graph)

'''
graph[('x', t, s, g, n, d, p)] = [('or', [...])]
'''
