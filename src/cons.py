from var import *
import numpy as np


def bic0(t, s, g, n):
    truth = [
        (duration[(t, s, g, n)] > 0)
    ]
    return np.prod(truth)


def bic1(t, s, g, n, d, p1, p2):
    truth = [
        (p1 >= np.min(periods[d])),
        (p1 <= np.max(periods[d]) - duration[(t, s, g, n)] + 1),
        (p2 >= p1),
        (p2 <= p1 + duration[(t, s, g, n)] - 1)
    ]
    return np.prod(truth)


def bic2(t, s, g, n, d, p1, p2):
    truth = [
        (p1 <= p2),
        (p1 >= p2 - duration[(t, s, g, n)] + 1),
        (p1 >= np.min(periods[d])),
        (p1 <= np.max(periods[d]) - duration[(t, s, g, n)] + 1)
    ]
    return np.prod(truth)


def bic3(d, p):
    truth = [
        (p <= np.max(periods[d])),
        (p >= np.min(periods[d]))
    ]
    return np.prod(truth)


def bic4(d, p):
    truth = [
        (p in periods[d])
    ]
    return np.prod(truth)


def bic5(t, s, g, n, d, p):
    truth = [
        (p1 >= np.min(periods[d])),
        (p1 <= np.max(periods[d]) - duration[(t, s, g, n)] + 1)
    ]
    return np.prod(truth)


def bic6(t, s, g, n):
    # this means tsgn belongs to lessons[t] and to lessons[g]
    truth = [
        (duration[(t, s, g, n)] > 0)
    ]
    return np.prod(truth)


def bic7(d):
    truth = [
        (d in days)
    ]
    return np.prod(truth)


def bic8(k, d, p):
    truth = [
        (k >= 1),
        (k <= len(periods[d]) - 2),
        (p >= np.min(periods[d]) + 1),
        (p <= np.max(periods[d]) - k)
    ]
    return np.prod(truth)


def bic9(k, d):
    truth = [
        (k >= 1),
        (k <= len(periods[d]) - 2)
    ]
    return np.prod(truth)


def bic10(k, d, p):
    truth = [
        (p >= np.min(periods[d]) + 1),
        (p <= np.max(periods[d]) - k)
    ]
    return np.prod(truth)


def bic11(d, p):
    truth = [
        (p >= np.min(periods[d]) + 1),
        (p <= np.max(periods[d]) - 1)
    ]
    return np.prod(truth)


def bic12(k, d, p):
    truth = [
        (k >= 1),
        (k <= np.max(periods[d]) - p)
    ]
    return np.prod(truth)


def bic13(d, p):
    truth = [
        (p >= np.min(periods[d])),
        (p <= np.max(periods[d]))
    ]
    return np.prod(truth)


def negation(var):
    if var[0] == 'not':
        return var[1]
    else:
        return ('not', var)


def single(vars):
    and_list = []
    k = len(vars)
    for j in range(k):
        for i in range(j):
            and_list.append(('or', [
                negation(vars[i]),
                negation(vars[j])
            ]))
    return ('and', and_list)


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
            return (negation(('or', [self.vars])))

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
                        B_vars[i][g][j] = (
                            'Bgj', (g, j, Cardinality.group_count))
                    else:
                        B_vars[i][g][j] = negation(
                            ('Bgj', (g, j, Cardinality.group_count)))

        main_and_clause = []
        for i in range(self.n):
            T_or_list = []
            for g in range(max(0, (self.k - self.n + i)),
                           min(i, self.k - 1) + 1):
                T_or_list.append(T_vars[g][i])

            or_clause_1 = ('or', negation(self.vars[i]), ('or', T_or_list))

            and_list1 = []
            for g in range(max(0, (self.k - self.n + i)),
                           min(i, self.k - 1) + 1):
                and_list2 = []
                for j in range(self.bin_size):
                    and_list2.append(('or', negation(
                        T_vars[g][i]), B_vars[i][g][j]))

                and_list1.append(('and', and_list2))

            and_clause_1 = ('and', and_list1)

            main_and_clause.append(('and', or_clause_1, and_clause_1))

        return ('and', main_and_clause)


def filter_bool(bool_tuple):
    '''
    Filters the void implications
    '''
    if isinstance(bool_tuple, type([])):
        bool_tuple = ('and', bool_tuple)

    if bool_tuple[0] != 'and' and bool_tuple[0] != 'or':
        return bool_tuple

    bool_list = bool_tuple[1]
    if len(bool_list) == 0:
        return None

    if len(bool_list) == 1:
        return bool_list[0]

    new_list = []
    for x in bool_list:
        new_x = filter_bool(x)

        if new_x is not None:
            new_list.append(new_x)

    return (bool_tuple[0], new_list)


def filter_graph(graph):
    '''
    Filters all void implication
    '''
    for var_type in list(graph.keys()):
        for var_tup in list(graph[var_type].keys()):
            new_bool_list = filter_bool(graph[var_type][var_tup])
            if new_bool_list is None:
                graph[var_type].pop(var_tup)
            else:
                graph[var_type][var_tup] = new_bool_list
