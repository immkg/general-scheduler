from StaticVariables import *
from utils import *
from z3 import * 

class Parser():
    """docstring for Parser"""

    def __init__(self, graphs, true_lists):
        self.graphs = graphs
        self.true_lists = true_lists
        self.result_graphs = {}
    
    def compute_result(self, num_results=3):
        bool_list = []
        for graph in self.graphs:
            for i in graph:
                for j in graph[i]:
                    bool_list.append(Implies(parse_val((i, j)), parse_val(graph[i][j])))

        for true_list in self.true_lists:
            formatted_true_list = parse_val(true_list)
            if formatted_true_list != None:
                bool_list.append(Implies(True, formatted_true_list))

        for i in range(num_results):
            bool_result = compute_bool(bool_list)

            if bool_result[0] == False:
                break

            truth_assignments = bool_result[1]
            not_again = []

            for x in truth_assignments.decls():
                not_again.append(Bool(str(x)) != truth_assignments[x])

            result_graph = {}

            for x in truth_assignments:
                y = str(x)[2:-1].split('\', ')
                result_graph[y[0]] = {
                        True: [],
                        False: []
                        }

            for x in truth_assignments:
                y = str(x)[2:-1].split('\', ')
                result_graph[y[0]][bool(truth_assignments[x])].append(tuple(map(int, y[1][1:-1].split(','))))
            
            bool_list.append(Or(not_again))
            self.result_graphs[i] = result_graph

