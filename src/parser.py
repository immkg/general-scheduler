from z3 import *
from implic import *

bool_list = []
truth_dict = {}
all_result = {}

def ParseVal(v):
	if(v[0] == 'not'):
		return Not(Bool(str(v[1])))
	elif(v[0] == 'or'):
		return Or([ ParseVal(b) for b in v[1] ])					 
	elif(v[0] == 'and'):
		return And([ ParseVal(b) for b in v[1] ])
	else:
		return Bool(str(v))
	
def compute_bool(*args, **keywords):		#Time table SAT solver
	s = Solver()
	s.set(**keywords)
	s.add(*args)
	if keywords.get('show', False):
		print s
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

for itr in range(1):
    print "Finding Solution " + str(itr+1)
    time_table = compute_bool(bool_list)

    if time_table[0] == False:
        break

    m = time_table[1]
    not_again = []
    var_result = {}
    
    for x in m.decls():
        var_result[x] = bool(m[x])
        not_again.append(Bool(str(x)) != m[x])

    result_graph = {}

    for x in var_result:
        y = str(x)[2:-1].split('\', ')
        result_graph[y[0]] = {
                True: [],
                False: []
                }
	
    for x in var_result:
        y = str(x)[2:-1].split('\', ')
        result_graph[y[0]][var_result[x]].append(tuple(map(int, y[1][1:-1].split(','))))
    
    bool_list.append(Or(not_again))
    all_result[itr] = result_graph
