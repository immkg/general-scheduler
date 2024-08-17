from z3 import *
from implic import *

result = {}  # stores result in Bool instance
sol_list = []
graph = graph2
truth_dict = {}
bool_graph = {}


def DependsOn(pack, deps):  # Adding Implied variables
    return And([Implies(pack, dep) for dep in deps])


def isNeg(v):  # check if ~ is applied
    if(v[0][0] == '~'):
        return True
    else:
        return False


def remTd(v):  # remove ~ form vars
    return str((v[0][1:], v[1]))


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


def ParseVal(v):  # string to bool parser
    if(v[0] == 'or'):
        if len(v[1]) > 1:
            return Or([Not(Bool(remTd(b))) if isNeg(b) else ParseVal(b)
                      for b in v[1] if vc(b)])
        else:
            if isNeg(v[1][0]):
                return Not(Bool(remTd(v[1][0])))
            else:
                return ParseVal(v[1][0])

    elif(v[0] == 'and'):
        if len(v[1]) > 1:
            return And([Not(Bool(remTd(b))) if isNeg(b) else ParseVal(b)
                       for b in v[1] if vc(b)])
        else:
            if isNeg(v[1][0]):
                return Not(Bool(remTd(v[1][0])))
            else:
                return ParseVal(v[1][0])
    else:
        if isNeg(v):
            return Not(Bool(remTd(v)))
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


FLA = 0

for i in graph:  # z3 bool instance clause dict
    for j in graph[i]:
        if len(graph[i][j]) > 0:
            bool_graph[ParseVal((i, j))] = [ParseVal(v)
                                            for v in graph[i][j] if vc(v)]
        else:
            FLA += 1
print(FLA)

for i in bool_graph:  # z3 bool And expr
    sol_list.append(DependsOn(i, bool_graph[i]))

true_bool = [ParseVal(v) for v in true_list if vc(v)]

sol_list.append(DependsOn(True, true_bool))  # True_list expr

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
