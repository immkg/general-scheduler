from StaticVariables import *
from range_constraints import *
from utils import *

class StandardImplications():
    """docstring for StandardImplications"""

    def __init__(self):
        self.true_list = []
        self.graph = {}

        self.graph['x!tsgndp'] = {}
        self.graph['xtsgndp'] = {}
        self.graph['xtsgnd'] = {}
        self.graph['xtdp'] = {}
        self.graph['xgdp'] = {}
        self.graph['xtd'] = {}
        self.graph['xtp'] = {}
        self.graph['iktdp'] = {}
        self.graph['iktd'] = {}
        self.graph['ikt'] = {}
        self.graph['ikgdp'] = {}
        self.graph['ikgd'] = {}
        self.graph['ikg'] = {}
        self.graph['itdp'] = {}
        self.graph['igdp'] = {}


    def init_vars(self):

        for (t, s, g, n) in StaticVariables.duration.keys():
            for d in StaticVariables.days:
                self.graph['xtsgnd'][(t, s, g, n, d)] = []
                for p in StaticVariables.periods[d]:
                    self.graph['x!tsgndp'][(t, s, g, n, d, p)] = []
                    self.graph['xtsgndp'][(t, s, g, n, d, p)] = []


        for t in StaticVariables.teachers:
            for d in StaticVariables.days:
                self.graph['xtd'][(t, d)] = []
                for p in StaticVariables.periods[d]:
                    self.graph['xtdp'][(t, d, p)] = []

        for t in StaticVariables.teachers:
            for p in range(StaticVariables.p_max):
                self.graph['xtp'][(t, p)] = []

        for g in StaticVariables.groups:
            for d in StaticVariables.days:
                for p in StaticVariables.periods[d]:
                    self.graph['xgdp'][(g, d, p)] = []



        for k in range(1, StaticVariables.p_max + 1): #should it not be from 1 to pmax rather than from 0 to pmax - 1
            # Yes it sould be from 1 to p_max - 1. -- SOLVED
            for t in StaticVariables.teachers:
                self.graph['ikt'][(k, t)] = []
                for d in StaticVariables.days:
                    if bic9(k, d):
                        self.graph['iktd'][(k, t, d)] = []
                        for p in StaticVariables.periods[d]:
                            if bic8(k, d, p):
                                self.graph['iktdp'][(k, t, d, p)] = []

        for k in range(1, StaticVariables.p_max + 1):
            for g in StaticVariables.groups:
                self.graph['ikg'][(k, g)] = []
                for d in StaticVariables.days:
                    if bic9(k, d):
                        self.graph['ikgd'][(k, g, d)] = []
                        for p in StaticVariables.periods[d]:
                            if bic8(k, d, p):
                                self.graph['ikgdp'][(k, g, d, p)] = []


        for t in StaticVariables.teachers:
            for d in StaticVariables.days:
                for p in StaticVariables.periods[d]:
                    if bic11(d, p):
                        self.graph['itdp'][(t, d, p)] = []

        for g in StaticVariables.groups:
            for d in StaticVariables.days:
                for p in StaticVariables.periods[d]:
                    if bic11(d, p):
                        self.graph['igdp'][(g, d, p)] = []


    def basic_implications(self):

        for (t, s, g, n, d, p1) in self.graph['x!tsgndp'].keys():
            for p2 in StaticVariables.periods[d]:
                if bic1(t, s, g, n, d, p1, p2):
                    self.graph['x!tsgndp'][(t, s, g, n, d, p1)].append(
                        ('xtsgndp', (t, s, g, n, d, p2))
                    )

        for (t, s, g, n, d, p2) in self.graph['xtsgndp'].keys():
            or_list = []
            for p1 in StaticVariables.periods[d]:
                if bic2(t, s, g, n, d, p1, p2):
                    or_list.append(('x!tsgndp', (t, s, g, n, d, p1)))
            self.graph['xtsgndp'][(t, s, g, n, d, p2)].append((StaticVariables.or_head, or_list))


        for (t, s, g, n, d, p) in self.graph['xtsgndp'].keys():
            self.graph['xtsgndp'][(t, s, g, n, d, p)].append(('xtsgnd', (t, s, g, n, d)))
            self.graph['xtsgndp'][(t, s, g, n, d, p)].append(('xtdp', (t, d, p)))
            self.graph['xtsgndp'][(t, s, g, n, d, p)].append(('xgdp', (g, d, p)))


        for (t, s, g, n, d) in self.graph['xtsgnd'].keys():
            or_list = []
            for p in StaticVariables.periods[d]:
                or_list.append(('xtsgndp', (t, s, g, n, d, p)))
            self.graph['xtsgnd'][(t, s, g, n, d)].append((StaticVariables.or_head, or_list))


        or_list_t = {}

        or_list_g = {}

        for (t, d, p) in self.graph['xtdp'].keys():
            or_list_t[(t, d, p)] = []

        for (g, d, p) in self.graph['xgdp'].keys():
            or_list_g[(g, d, p)] = []

        for (t, s, g, n, d, p) in self.graph['xtsgndp'].keys():
            or_list_t[(t, d, p)].append(('xtsgndp', (t, s, g, n, d, p)))
            or_list_g[(g, d, p)].append(('xtsgndp', (t, s, g, n, d, p)))

        for (t, d, p) in self.graph['xtdp'].keys():
            self.graph['xtdp'][(t, d, p)].append(('xtd', (t, d)))
            self.graph['xtdp'][(t, d, p)].append(('xtp', (t, p)))
            self.graph['xtdp'][(t, d, p)].append((StaticVariables.or_head, or_list_t[(t, d, p)]))

        for (g, d, p) in self.graph['xgdp'].keys():
            self.graph['xgdp'][(g, d, p)].append((StaticVariables.or_head, or_list_g[(g, d, p)]))


        for (t, d) in self.graph['xtd'].keys():
            or_list = []
            for p in StaticVariables.periods[d]:
                or_list.append(('xtdp',( t, d, p)))
            self.graph['xtd'][(t, d)].append((StaticVariables.or_head, or_list))

        for (t, p) in self.graph['xtp'].keys():
            or_list = []
            for d in StaticVariables.days:
                if bic3(d, p):
                    or_list.append(('xtdp', (t, d, p)))
            self.graph['xtp'][(t, p)].append((StaticVariables.or_head, or_list))


        for (k, t, d, p) in self.graph['iktdp'].keys():
            self.graph['iktdp'][(k, t, d, p)].append(('xtdp', (t, d, p - 1)))
            or_list = []
            for j in range(k):
                or_list.append(('xtdp', (t, d, p + j)))
                self.graph['iktdp'][(k, t, d, p)].append(negation(('xtdp', (t, d, p + j))))
            self.graph['iktdp'][(k, t, d, p)].append(('xtdp', (t, d, p + k)))
            self.true_list.append(
                (StaticVariables.or_head, [
                            negation(('xtdp', (t, d, p - 1))),
                            (StaticVariables.or_head, or_list),
                            negation(('xtdp', (t, d, p + k))),
                            negation(('iktdp', (k, t, d, p)))
                ]))

            self.graph['iktdp'][(k, t, d, p)].append(('iktd', (k, t, d)))

        for (k, t, d) in self.graph['iktd'].keys():
            or_list = []
            for p in StaticVariables.periods[d]:
                if bic10(k, d, p):
                    or_list.append(('iktdp', (k, t, d, p)))
            self.graph['iktd'][(k, t, d)].append((StaticVariables.or_head, or_list))

            self.graph['iktd'][(k, t, d)].append(('ikt', (k, t)))

            self.graph['iktd'][(k, t, d)].append(('itdp', (t, d, p)))

        for (k, t) in self.graph['ikt'].keys():
            or_list = []
            for d in StaticVariables.days:
                or_list.append(('iktd', (k, t, d)))
            self.graph['ikt'][(k, t)].append((StaticVariables.or_head, or_list))

        for (t, d, p) in self.graph['itdp'].keys():
            or_list = []
            for k in range(StaticVariables.p_max):
                if bic12(k, d, p):
                    or_list.append(('iktdp', (k, t, d, p)))
            self.graph['itdp'][(t, d, p)].append((StaticVariables.or_head, or_list))

        # ================ EXACTLY SAME FOR GROUPS =================
        # Abstract this somehow!


        for (k, g, d, p) in self.graph['ikgdp'].keys():
            self.graph['ikgdp'][(k, g, d, p)].append(('xgdp', (g, d, p - 1)))
            or_list = []
            for j in range(k):
                or_list.append(('xgdp', (g, d, p + j)))
                self.graph['ikgdp'][(k, g, d, p)].append(negation(('xgdp', (g, d, p + j))))
            self.graph['ikgdp'][(k, g, d, p)].append(('xgdp', (g, d, p + k)))
            self.true_list.append(
                (StaticVariables.or_head, [
                            negation(('xgdp', (g, d, p - 1))),
                            (StaticVariables.or_head, or_list),
                            negation(('xgdp', (g, d, p + k))),
                            negation(('ikgdp', (k, g, d, p)))
                ]))

            self.graph['ikgdp'][(k, g, d, p)].append(('ikgd', (k, g, d)))

        for (k, g, d) in self.graph['ikgd'].keys():
            or_list = []
            for p in StaticVariables.periods[d]:
                if bic10(k, d, p):
                    or_list.append(('ikgdp', (k, g, d, p)))
            self.graph['ikgd'][(k, g, d)].append((StaticVariables.or_head, or_list))

            self.graph['ikgd'][(k, g, d)].append(('ikg', (k, g)))

            self.graph['ikgd'][(k, g, d)].append(('igdp', (g, d, p)))

        for (k, g) in self.graph['ikg'].keys():
            or_list = []
            for d in StaticVariables.days:
                or_list.append(('ikgd', (k, g, d)))
            self.graph['ikg'][(k, g)].append((StaticVariables.or_head, or_list))

        for (g, d, p) in self.graph['igdp'].keys():
            or_list = []
            for k in range(StaticVariables.p_max):
                if bic12(k, d, p):
                    or_list.append(('ikgdp', (k, g, d, p)))
            self.graph['igdp'][(g, d, p)].append((StaticVariables.or_head, or_list))


    def correctness_implications(self):

        for (t, s, g, n) in StaticVariables.duration.keys():
            or_list = []
            for d in StaticVariables.days:
                or_list.append(('xtsgnd', (t, s, g, n, d)))
            self.true_list.append((StaticVariables.or_head, or_list))


        multi_dict = {}
        for (t, s, g, n, d) in self.graph['xtsgnd'].keys():
            multi_dict[(t, s, g, n)] = []
        for (t, s, g, n, d) in self.graph['xtsgnd'].keys():
            multi_dict[(t, s, g, n)].append(('xtsgnd', (t, s, g, n, d)))
        for (t, s, g, n) in multi_dict.keys():
            self.true_list.append(single(multi_dict[(t, s, g, n)]))


        multi_dict = {}
        for (t, s, g, n, d, p) in self.graph['x!tsgndp'].keys():
            multi_dict[(t, s, g, n, d)] = []
        for (t, s, g, n, d, p) in self.graph['x!tsgndp'].keys():
            multi_dict[(t, s, g, n, d)].append(('x!tsgndp', (t, s, g, n, d, p)))
        for (t, s, g, n, d) in multi_dict.keys():
            self.true_list.append(single(multi_dict[(t, s, g, n, d)]))



        multi_dict = {}
        for (t, s, g, n, d, p) in self.graph['xtsgndp'].keys():
            multi_dict[(g, d, p)] = []
        for (t, s, g, n, d, p) in self.graph['xtsgndp'].keys():
            multi_dict[(g, d, p)].append(('xtsgndp', (t, s, g, n, d, p)))
        for (g, d, p) in multi_dict.keys():
            self.true_list.append(single(multi_dict[(g, d, p)]))


        '''
        Assume all groups can be interleaved
        The overlapping can be removied using the comfort conditions.
        '''

        multi_dict = {}
        for (t, s, g, n, d, p) in self.graph['xtsgndp'].keys():
            multi_dict[(t, d, p)] = {}
        for (t, s, g, n, d, p) in self.graph['xtsgndp'].keys():
            multi_dict[(t, d, p)][(s, n)] = []
        for (t, s, g, n, d, p) in self.graph['xtsgndp'].keys():
            multi_dict[(t, d, p)][(s, n)].append(('xtsgndp', (t, s, g, n, d, p)))
        for (t, d, p) in multi_dict.keys():
            single_list = []
            for (s, n) in multi_dict[(t, d, p)]:
                single_list.append(multi_dict[(t, d, p)][(s, n)][0])
                l = len(multi_dict[(t, d, p)][(s, n)])
                for i in range(l):
                    if i == 0:
                        append_list = multi_dict[(t, d, p)][(s, n)][1:]
                    elif i == l - 1:
                        append_list = multi_dict[(t, d, p)][(s, n)][:-1]
                    else:
                        append_list = multi_dict[(t, d, p)][(s, n)][:i-1] + multi_dict[(t, d, p)][(s, n)][i+1:]
                    self.graph['xtsgndp'][multi_dict[(t, d, p)][(s, n)][i][1]] += append_list
            self.true_list.append(single(single_list))

        '''
        Check the previous implication.
        '''

    def format_result(self):
        filter_graph(self.graph)
        self.true_list = filter_bool(self.true_list)