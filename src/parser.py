from z3 import *
from implic import *

bool_list = []
var_result = {}
all_result = {}
result_graph = {}

def ParseVal(v):
	if(v[0] == 'not'):
		return Not(Bool(str(v[1])))
	elif(v[0] == 'or'):
		return Or([ ParseVal(b) for b in v[1] ])					 
	elif(v[0] == 'and'):
		return And([ ParseVal(b) for b in v[1] ])
	else:
		return Bool(str(v))
	
def compute_bool(*args):		#Time table SAT solver
	s = Solver()
	s.add(*args)
	r = s.check()
    
	if r == unsat:
		return (False, 'No Solution')
	elif r == unknown:
		return (False, 'Failed to solve')
	else:
		return (True, s.model())

for i in graph:						#z3 bool instance clause dict
    for j in graph[i]:
    	bool_list.append(Implies(ParseVal((i, j)), ParseVal(graph[i][j])))

bool_list.append(Implies(True, ParseVal(true_list))) 	#True_list expr

itr = 0

while itr < max_sol:
    time_table = compute_bool(bool_list)
    if time_table[0] == False:
        break;

    not_again = []

    m = time_table[1]
    for x in m.decls():
        var_result[x] = bool(m[x])
        not_again.append(Bool(str(x)) != m[x])

    for x in var_result:
        y = str(x)[2:-1].split('\', ')
        result_graph[y[0]] = {
            True: [],
            False: []
        }

    for x in var_result:
        str(x)[2:-1].split('\', ')
        result_graph[y[0]][var_result[x]].append(tuple(map(int, y[1][1:-1].split(','))))

    print len(result_graph)    
    
    all_result[itr] = result_graph
    bool_list.append(Or(not_again))
    itr = itr + 1