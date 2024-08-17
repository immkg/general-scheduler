from collections import defaultdict
from StaticVariables import *

class ComfortImplications():
    """docstring for ComfortImplications"""

    def __init__(self):
        self.comfort_graph = {}
        self.comfort_graph['xtdp'] = {}
        self.comfort_graph['xtsgnd'] = {}
        self.comfort_graph['x!tsgndp'] = {}
        self.comfort_graph['xtd'] = {}
        self.comfort_graph['xtp'] = {}
        self.comfort_graph['xgdp'] = {}
        self.comfort_graph['xgd'] = {}
        self.comfort_graph['xgp'] = {}
        self.comfort_graph['lkgd'] = {}
        self.comfort_true_list = []

        StaticVariables.days = days
        StaticVariables.periods = StaticVariables.periods
        StaticVariables.duration = duration

    def reset(self):
        self.comfort_graph = {}
        self.comfort_graph['xtdp'] = {}
        self.comfort_graph['xtsgnd'] = {}
        self.comfort_graph['x!tsgndp'] = {}
        self.comfort_graph['xtd'] = {}
        self.comfort_graph['xtp'] = {}
        self.comfort_graph['xgdp'] = {}
        self.comfort_graph['xgd'] = {}
        self.comfort_graph['xgp'] = {}
        self.comfort_graph['lkgd'] = {}
        self.comfort_true_list = []

    def format_result(self):
        filter_graph(self.comfort_graph)
        self.comfort_true_list = filter_bool(self.comfort_true_list)

    # 1) Forbidden and requested working hours
    def teacher_forbidden(self,
                          teacher_forbidden0 = [],
                          teacher_forbidden1 = [],
                          teacher_forbidden2 = []):

        if not teacher_forbidden0:
            for (t, d, p) in teacher_forbidden0:
                self.comfort_true_list.append(negation(('xtdp', (t, d, p))))
        
        if not teacher_forbidden1:
            for (t, d) in teacher_forbidden1:
                self.comfort_true_list.append(negation(('xtd', (t, d))))
        
        if not teacher_forbidden2:
            for (t, p) in teacher_forbidden2:
                self.comfort_true_list.append(negation(('xtp', (t, p))))

        return 

    def teacher_requested(self,
                          teacher_requested0 = [],
                          teacher_requested1 = [],
                          teacher_requested2 = []):

        if not teacher_requested0:
            for (t, d, p) in teacher_requested0:
                self.comfort_true_list.append(('xtdp', (t, d, p)))
        
        if not teacher_requested1:
            for (t, d) in teacher_requested1:
                self.comfort_true_list.append(('xtd', (t, d)))
        
        if not teacher_requested2:
            for (t, p) in teacher_requested2:
                self.comfort_true_list.append(('xtp', (t, p)))

        return

    def group_forbidden(self,
                        group_forbidden0 = [],
                        group_forbidden1 = [],
                        group_forbidden2 = []):

        if not group_forbidden0:
            for (g, d, p) in group_forbidden0:
                self.comfort_true_list.append(negation(('xgdp', (g, d, p))))
        
        if not group_forbidden1:
            for (g, d) in group_forbidden1:
                self.comfort_true_list.append(negation(('xgd', (g, d))))
        
        if not group_forbidden2:
            for (g, p) in group_forbidden2:
                self.comfort_true_list.append(negation(('xgp', (g, p))))

        return

    def group_requested(self,
                        group_requested0 = [],
                        group_requested1 = [],
                        group_requested2 = []):

        if not group_requested0:
            for (g, d, p) in group_requested0:
                self.comfort_true_list.append(('xgdp', (g, d, p)))
        
        if not group_requested1:
            for (g, d) in group_requested1:
                self.comfort_true_list.append(('xgd', (g, d)))
        
        if not group_requested2:
            for (g, p) in group_requested2:
                self.comfort_true_list.append(('xgp', (g, p)))

        return

    # 2)
    # a) Avoiding groups and teachers overlapping 

    def overlaps(self,
                 teacher_overlap = [],
                 teacher_no_overlap = [],
                 group_no_overlap = []):

        if not teacher_no_overlap:
            for (t1, t2) in teacher_no_overlap:
                for d in StaticVariables.days:
                    for p in StaticVariables.periods[d]:
                        self.comfort_graph['xtdp'][(t1, d, p)].append(
                            negation(('xtdp', (t2, d, p))))
                        self.comfort_graph['xtdp'][(t2, d, p)].append(
                            negation(('xtdp', (t1, d, p))))
        
        if not group_no_overlap:
            for (g1, g2) in group_no_overlap:
                for d in StaticVariables.days:
                    for p in StaticVariables.periods[d]:
                        self.comfort_graph['xgdp'][(g1, d, p)].append(
                            negation(('xgdp', (g2, d, p))))
                        self.comfort_graph['xgdp'][(g2, d, p)].append(
                            negation(('xgdp', (g1, d, p))))
        
        # b)
        # Compulsory teacher overlap
        
        if not teacher_overlap:
            for (t1, t2) in teacher_overlap:
                for d in StaticVariables.days:
                    for p in StaticVariables.periods[d]:
                        self.comfort_graph['xtdp'][(t1, d, p)].append(
                            ('xtdp', (t2, d, p)))
                        self.comfort_graph['xtdp'][(t2, d, p)].append(
                            ('xtdp', (t1, d, p)))

        return

    # 3) Number of teaching days for a teacher

    def teaching_days(self, teaching_days = []):

        if not teaching_self.days:
            for (t, n) in teaching_self.days:
                atmost_var_list = []
                atleast_var_list = []
                for d in StaticVariables.days:
                    atmost_var_list.append(('xtd', (t, d)))
                    atleast_var_list.append(negation(('xtd', (t, d))))
        
                atmost_n = Cardinality(atmost_var_list, n)
                self.comfort_true_list.append(atmost_n.form())
        
                atleast_n = Cardinality(atleast_var_list, (no_of_days - n))
                self.comfort_true_list.append(atleast_n.form())

        return

    # 4) Work day duration

    def duration(self,
                 work_day_duration = [],
                 duration_upper_limit = [],
                 duration_lower_limit = []):

        if not work_day_duration:
            for (g, k, d) in work_day_duration:
                self.comfort_graph['lkgd'][(g, k, d)] = []
        
                or_list = []
                for p in range(min(self.periods[d]), max(self.periods[d]) - k + 2):
                    or_list.append(
                        (StaticVariables.and_head, [('xgdp', (g, d, p)), ('xgdp', (g, d, p + k - 1))]))
                    self.comfort_true_list.append((StaticVariables.or_head, [negation(('xgdp', (g, d, p))), negation(
                        ('xgdp', (g, d, p + k - 1))), ('lkgd', (k, g, d))]))
        
                self.comfort_graph['lkgd'][(g, k, d)].append((StaticVariables.or_head, or_list))
        
        # Atmost n hours on day d for group g
        
        if not duration_upper_limit:
            for (g, d, n) in duration_upper_limit:
                for k in range(n + 1, max(self.periods[d]) + 1):
                    self.comfort_true_list.append(negation(('lkgd', (k, g, d))))
        
        # Atleast n hours on day d for group g
        
        if not duration_lower_limit:
            for (g, d, n) in duration_lower_limit:
                self.comfort_graph['xgd'][(g, d)].append(
                    ('lkgd', (n, g, d)))  # Not convinced

        return

    # 5) Idle duration cardinality('xtgdp')

    # Idle StaticVariables.periods of length k not allowed

    def idle_duration(self,
                      teacher_max_idle_length = [],
                      teacher_atmost_one_idle_period = [],
                      teacher_atmost_k_idle_period = [],
                      group_max_idle_length = [],
                      group_atmost_one_idle_period = [],
                      group_atmost_k_idle_period = []):
        
        if not teacher_max_idle_length:
            for (t, k) in teacher_max_idle_length:
                self.comfort_true_list.append(negation(('ikt', (k, t))))
        
        # Atmost one idle period for a teacher per day
        
        if not teacher_atmost_one_idle_period:
            for t in teacher_atmost_one_idle_period:
                var_list = []
                for d in StaticVariables.days:
                    for p in range(min(self.periods[d]) + 1, max(self.periods[d]) - 1 + 1):
                        var_list.append(('itdp', (t, d, p)))
        
                self.comfort_true_list.append(single(var_list))
        
        # Atmost k idle StaticVariables.periods for a teacher in a week
        
        if not teacher_atmost_k_idle_period:
            for (t, k) in teacher_atmost_k_idle_period:
                var_list = []
                for d in StaticVariables.days:
                    for p in StaticVariables.periods[d]:
                        var_list.append(('itdp', (t, d, p)))
        
                atmost_k = Cardinality(var_list, k)
                self.comfort_true_list.append(atmost_k.form())
        
        # For groups
        # Idle StaticVariables.periods of length k not allowed
        
        if not group_max_idle_length:
            for (g, k) in group_max_idle_length:
                self.comfort_true_list.append(negation(('ikg', (k, g))))
        
        # Atmost one idle period for a group per day
        
        if not group_atmost_one_idle_period:
            for g in group_atmost_one_idle_period:
                var_list = []
                for d in StaticVariables.days:
                    for p in range(min(self.periods[d]) + 1, max(self.periods[d]) - 1 + 1):
                        var_list.append(('igdp', (g, d, p)))
        
                self.comfort_true_list.append(single(var_list))
        
        # Atmost k idle StaticVariables.periods for a teacher in a week
        
        if not group_atmost_k_idle_period:
            for (g, k) in group_atmost_k_idle_period:
                var_list = []
                for d in StaticVariables.days:
                    for p in StaticVariables.periods[d]:
                        var_list.append(('igdp', (g, d, p)))
        
                atmost_k = Cardinality(var_list, k)
                self.comfort_true_list.append(atmost_k.form())

        return

    # 6) Forbidden hours and requested hours:
    # Favoured StaticVariables.periods: 'xtsgnd' => 'x!tsgndp1' or ...

    def hour_specification(self,
                           favoured_hours = {},
                           last_first_hours = []):

        if not favoured_hours:  # dict = {(t,s,g,n):[p]}
            confort_graph['xtsgnd'] = defaultdict(lambda: [])
            for (t, s, g, n) in favoured_hours.keys():
                for d in StaticVariables.days:
                    self.comfort_graph['xtsgnd'][(t, s, g, n, d)] = []
                    or_list = []
                    for p in favoured_hours[(t,s,g,n)]:
                        if bic3(d, p):
                            or_list.append(('x!tsgndp', (t, s, g, n, d, p)))
            
                    self.comfort_graph['xtsgnd'][(t, s, g, n, d)].append((StaticVariables.or_head, or_list))
        
        # first or last last lesson in a day: 'x!tsgndp' => (and, negation('xgdp')) or (StaticVariables.and_head, negation('xgdp'))
        
        if not last_first_hours:
            for (t, s, g, n) in last_first_hours:
                for d in StaticVariables.days:
                    for p in StaticVariables.periods[d]:
                        self.comfort_graph['x!tsgndp'][(t, s, g, n, d, p)] = []
                        and_list1 = []
                        for p2 in range(min(self.periods[d]), p):
                            and_list1.append(negation(('xgdp', (g, d, p2))))
        
                        and_list2 = []
                        for p2 in range(p + duration[(t, s, g, n)], max(self.periods(d) + 1)):
                            and_list2.append(negation(('xgdp', (g, d, p))))
        
                        or_list = [(StaticVariables.and_head, and_list1), (StaticVariables.and_head, and_list2)]
            
                        self.comfort_graph['x!tsgndp'][(t, s, g, n, d, p)].append((StaticVariables.or_head, or_list))

        return

    # 7) lessons on non consecutive StaticVariables.days:
    #   'xtsgnd' => negation('xtsg(n + 1)(d+1))
    #   except for last working day
    def non_consecutive(self, non_consecutive = []):

        if not non_consecutive:
            for (t, s, g, n) in non_consecutive:
                for d in StaticVariables.days[:-1]:
                    self.comfort_graph['xtsgnd'][(t, s, g, n, d)].append(negation(('xtsgnd', (t, s, g, n + 1, d + 1))))

        return