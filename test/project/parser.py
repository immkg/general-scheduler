from z3 import *
from popo import *

result = {}  # stores result in Bool instance
sol_list = []
truth_dict = {}
bool_graph = {}


def ParseVal(v):
    if(v[0] == 'not'):
        return Not(Bool(str(v[1])))
    elif(v[0] == 'or'):
        return Or([ParseVal(b) for b in v[1]])
    elif(v[0] == 'and'):
        return And([ParseVal(b) for b in v[1]])
    else:
        return Bool(str(v))


def makeTT(*args, **keywords):  # Time table SAT solver
    s = Solver()
    s.set(**keywords)
    s.add(*args)
    if keywords.get('show', False):
        print(s)
    r = s.check()
    if r == unsat:
        print("no solution")
    elif r == unknown:
        print("failed to solve")
        try:
            print(s.model())
        except Z3Exception:
            return
    else:
        return s.model()


for i in graph:  # z3 bool instance clause dict
    for j in graph[i]:
        bool_graph[ParseVal((i, j))] = ParseVal(graph[i][j])

for i in bool_graph:  # z3 bool And expr
    sol_list.append(Implies(i, bool_graph[i]))

sol_list.append(Implies(True, filter_bool(true_list)))  # True_list expr

m = makeTT(sol_list)
truth_dict['True'] = []
truth_dict['False'] = []

for x in m.decls():
    result[x] = m[x]
    truth_dict[str(m[x])].append(x)

result2 = {}
truth_dict2 = {}

for x in result:
    y = str(x)[2:-1].split('\', ')
    result2[y[0]] = {}
    truth_dict2[y[0]] = []

for x in result:
    y = str(x)[2:-1].split('\', ')
    result2[y[0]][y[1]] = result[x]
    if(result[x]):
        truth_dict2[y[0]].append(y[1])

# result2 : dict has result in init graph form
# truth_dict2 : dict has True states of vars#
