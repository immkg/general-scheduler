from range_constraints import *
from ComfortImplications import *
from StandardImplications import *
from Parser import *
from utils import *

import numpy as np
from tabulate import tabulate

class PSRB:    
    def __init__(self, date, absent_teacher_list, sdata, duration):
        self.absent_teacher_list = absent_teacher_list
        self.sdata = sdata
        self.date = date
        self.duration = duration
        
    def remove_teacher(self):
        for s in self.sdata:
            self.sdata[s] = [i for i in self.sdata[s] if i not in self.absent_teacher_list]
    
    def replace_teacher(self, t, s):       
        for a in np.random.permutation(len(self.sdata[s])):
            try:
                return self.sdata[s][a]
            except:
                return None
    
    def create_graph(self):
        self.remove_teacher()
        
        for (t, s, g, n) in self.duration.keys():
            if t in self.absent_teacher_list:
                st = self.replace_teacher(t, s)
                if st != None:
                    self.duration[(st, s, g, n)] = self.duration[(t, s, g, n)]
                    self.duration.pop((t, s, g, n))
                else:
                    return "no_extra_teacher_found"
        
        for (t, s, g, n) in self.duration.keys():
            StaticVariables.num_t = max([StaticVariables.num_t, t+1])
            StaticVariables.num_s = max([StaticVariables.num_s, s+1])
            StaticVariables.num_g = max([StaticVariables.num_g, g+1])
        
        StaticVariables.teachers = np.array(range(StaticVariables.num_t))
        StaticVariables.subjects = np.array(range(StaticVariables.num_s))
        StaticVariables.groups = np.array(range(StaticVariables.num_g))  
        
        StaticVariables.duration = self.duration
        
        x = StandardImplications()
        x.init_vars()
        x.basic_implications()
        x.correctness_implications()
        x.format_result()
        
        z = Parser([x.graph], [x.true_list])
        z.compute_result(1)
        
        return simple_ttable(z.result_graphs[0]['xtsgndp'][True])        