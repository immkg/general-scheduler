from StaticVariables import *
from z3 import *

def negation(var):
    if var[0] == StaticVariables.not_head:
        return var[1]
    else:
        return (StaticVariables.not_head, var)


def single(vars):
    and_list = []
    k = len(vars)
    for j in range(k):
        for i in range(j):
            and_list.append((StaticVariables.or_head, [
                negation(vars[i]),
                negation(vars[j])
            ]))
    return (StaticVariables.and_head, and_list)


class Cardinality:
    '''
    Condition that is satisfied when atmost k variables
    are satisfied in the given variable list (vars).

    The form method return a sat for the cardinality object 

    The encoding used is binary and symmetric breaking
    '''
    group_count = 0
    aux_vars_dict = {}
    vars_dict = {}

    def __init__(self, vars, k):

        self.vars = vars
        self.k = k
        self.n = len(vars)
        self.bin_size = int(math.ceil(math.log(self.n, 2)))

        if k > self.n or k < 0:
            return "Error !"

        Cardinality.group_count += 1
        Cardinality.vars_dict[Cardinality.group_count] = vars
        return

    def form(self):
        '''
        Returns a sat for the given cardinality object
        '''
        if (self.k == 0):
            return (negation((StaticVariables.or_head, [self.vars])))

        # Auxillary variables
        # --------------------
        # Auxillary variables are tagged for each cardinalty
        # group constraint with a non negative number (group_count).

        # T variables
        T_vars = {}
        for g in range(self.k):
            T_vars[g] = {}
            for i in range(self.n):
                T_vars[g][i] = ('Tgi', (g, i, Cardinality.group_count))

        # s variables
        bin_strings = {}
        for i in range(self.n):
            bin_strings[i] = list('{:0{}b}'.format(i, self.bin_size))

        # B variables
        B_vars = {}
        for i in range(self.n):
            B_vars[i] = {}
            for g in range(self.k):
                B_vars[i][g] = {}
                for j in range(self.bin_size):
                    if(bin_strings[i][j] == '1'):
                        B_vars[i][g][j] = ('Bgj', (g, j, Cardinality.group_count))
                    else:
                        B_vars[i][g][j] = negation(
                            ('Bgj', (g, j, Cardinality.group_count)))

        main_and_clause = []
        for i in range(self.n):
            T_or_list = []
            for g in range(max(0, (self.k - self.n + i)), min(i, self.k - 1) + 1):
                T_or_list.append(T_vars[g][i])

            or_clause_1 = (StaticVariables.or_head, negation(self.vars[i]), (StaticVariables.or_head, T_or_list))

            and_list1 = []
            for g in range(max(0, (self.k - self.n + i)), min(i, self.k - 1) + 1):
                and_list2 = []
                for j in range(self.bin_size):
                    and_list2.append((StaticVariables.or_head, negation(
                        T_vars[g][i]), B_vars[i][g][j]))

                and_list1.append((StaticVariables.and_head, and_list2))

            and_clause_1 = (StaticVariables.and_head, and_list1)

            main_and_clause.append((StaticVariables.and_head, or_clause_1, and_clause_1))

        return (StaticVariables.and_head, main_and_clause)


def filter_bool(bool_tuple):
    '''
    Filters the void implications
    '''
    if type(bool_tuple) == type([]):
        bool_tuple = (StaticVariables.and_head, bool_tuple)

    if bool_tuple[0] != StaticVariables.and_head and bool_tuple[0] != StaticVariables.or_head:
        return bool_tuple

    bool_list = bool_tuple[1]
    if len(bool_list) == 0:
        return None

    if len(bool_list) == 1:
        return bool_list[0]

    new_list = []
    for x in bool_list:
        new_x = filter_bool(x)

        if new_x != None:
            new_list.append(new_x)

    return (bool_tuple[0], new_list)


def filter_graph(graph):
    '''
    Filters all void implication
    '''
    for var_type in graph.keys():
        for var_tup in graph[var_type].keys():
            new_bool_list = filter_bool(graph[var_type][var_tup])
            if new_bool_list == None:
                graph[var_type].pop(var_tup)
            else:
                graph[var_type][var_tup] = new_bool_list


def parse_val(v):
    if(v[0] == 'not'):
        return Not(Bool(str(v[1])))
    elif(v[0] == 'or'):
        return Or([ parse_val(b) for b in v[1] ])                     
    elif(v[0] == 'and'):
        return And([ parse_val(b) for b in v[1] ])
    else:
        return Bool(str(v))
    
def compute_bool(*args, **keywords):        #Time table SAT solver
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


def simple_ttable(truth_tsgndp):
    
    ttable = [[[] for i in range(StaticVariables.p_max) ] for i in range(len(StaticVariables.days))]
    
    for (t, s, g, n, d, p) in truth_tsgndp:
        ttable[d][p].append((t, s, g, n))
    
    for i in range(len(ttable)):
        ttable[i].insert(0, "Day {}".format(str(i)))  

    return ttable
