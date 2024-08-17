import math
import numpy as np


def negation(var):
    var_to_modify = list(var)
    if var[0][0] == '~':
        var_to_modify[0] = var[0][1:]
    else:
        var_to_modify[0] = '~' + var[0]
    return tuple(var_to_modify)


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


test = Cardinality([('xtsg', (1, 1, 1)), ('xtsg', (2, 2, 3)),
                    ('xtsg', (1, 2, 1)), ('xtsg', (2, 2, 2)), ('xtsg', (1, 2, 3))], 3)
print((test.form()))

test2 = Cardinality([('xtsg', (1, 1, 1)), ('xtsg', (2, 2, 3)),
                    ('xtsg', (1, 2, 1)), ('xtsg', (2, 2, 2)), ('xtsg', (1, 2, 3))], 3)
print((test2.form()))

print((test2.__dict__))
