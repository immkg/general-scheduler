from parser import *
import numpy as np

for sol in all_result:
    result_graph = all_result[sol]
    print 'x!tsgndp: ', len(result_graph['x!tsgndp'][True]), len(duration)
    print 'xtsgndp: ', len(result_graph['xtsgndp'][True]), np.sum([x for x in duration.values()])
    
