from z3 import *
from implic import *

result = {}
sol_list = []
graph = graph2
truth_dict = {}
bool_graph = {}


def pf(i, j):  # pretty function
    return '(\'' + str(i) + '\', ' + str(j) + ')'


def DependsOn(pack, deps):  # Adding Implied variables
    return And([Implies(pack, dep) for dep in deps])


def ParseVal(v):  # string to bool parser
    if(v[0] == 'or'):
        return Or([Bool(str(b)) for b in v[1]])
    elif(v[0] == 'and'):
        return And([Bool(str(b)) for b in v[1]])
    else:
        return Bool(str(v))


def vc(v):  # check for voids
    if(len(v) == 0):
        return False
    elif(v[0] == 'or' or v[0] == 'and'):
        if(len(v[1]) > 0):
            return True
        else:
            return False
    else:
        return True


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
        bool_graph[Bool(pf(i, j))] = [ParseVal(v)
                                      for v in graph[i][j] if vc(v)]

for i in bool_graph:  # z3 bool And expr
    sol_list.append(DependsOn(i, bool_graph[i]))

m = makeTT(sol_list)
truth_dict['True'] = []
truth_dict['False'] = []

for x in m.decls():
    result[x] = m[x]
    truth_dict[str(m[x])].append(x)
