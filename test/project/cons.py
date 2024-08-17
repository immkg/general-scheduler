from var import *
import math


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
    var_to_modify = list(var)
    if var[0][0] == '~':
        var_to_modify[0] = var[0][1:]
    else:
        var_to_modify[0] = '~' + var[0]
    return tuple(var_to_modify)


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


def together(groups, t, s, n):
    '''
    Condition that is satisfied when all groups specified
    have the lesson tsn at the same time
    '''

    and_list = []
    k = len(groups)
    for j in range(k):
        and_list.append(('or', [
                        ('and', [groups[j],
                                 groups[j + 1]]),
                        ('and', [negation(groups[j]),
                                 negation(groups[j + 1])])
                        ]))
    return

# class cardinality:
#    '''
#    Condition that is satisfied when atmost k variables
#    are satisfied in the given variable list (vars).
#
#    The form method return a sat for the cardinality object
#
#    The encoding used is binary and symmetric breaking
#    '''
#    group_count = 0
#    aux_vars_dict = {}
#    vars_dict = {}
#
#    def __init__(self, vars, k):
#
#        self.vars = vars
#        self.k = k
#
#        n = len(vars)
#        bin_size = math.ceil(math.log(n) / math.log(2))
#
#        group_count += 1
#        vars_dict[group_count] = vars
#
#    def form(self):
#        '''
#        Returns a sat for the given cardinality object
#        '''
#
#        # Auxillary variables
#        # --------------------
#        # Auxillary variables are tagged for each cardinalty
#        # group constraint with a non negative number
#        # (currently incrementally). Such feature would require
#        # the emulation of static variable found in c
#        # Classes will be implemented to
#
#        # T variables
#        T_vars = {}
#        for g in range(k):
#            T_vars[g] = {}
#            for i in range(n):
#                T_vars[g][i].append('Tgi', (g, i, group_count))
#
#        # s variables
#        bin_strings = {}
#        for i in range(n):
#            bin_strings[i] = list('{:0{}b}'.format(i, bin_size))
#
#        # B variables
#        B_vars = {}
#        for i in range(n):
#            B_vars[i] = {}
#            for g in range(k):
#                B_vars[i][g] = {}
#                for j in range(bin_size):
#                    if(bin_strings[i][j] == '1'):
#                        B_vars[i][g][j] = ('Bgj', (g, j, group_count))
#                    else:
#                        B_vars[i][g][j] = negation(
#                            'Bgj', (g, j, group_count))
#
#        main_and_clause = []
#        for i in range(n):
#            T_or_list = []
#            for g in range(max(1, (k - n + i)), min(i, k) + 1):
#                T_or_list.append(T_vars[g][i]) = T_vars[g][i]
#
#            or_clause_1 = ('or', negation(vars[i]), ('or', T_or_list))
#
#            and_list1 = []
#            for g in range(max(1, (k - n + i)), min(i, k) + 1):
#                and_list2 = []
#                for j in range(bin_size):
#                    and_list2.append('or', negation(
#                        T_vars[g][i]), B_vars[i][g][j])
#
#                and_list1.append('and', and_list2)
#
#            and_clause_1 = ('and', and_list1)
#
#            main_and_clause.append('and', or_clause_1, and_clause_1)
#
#        return ('and', main_and_clause)
