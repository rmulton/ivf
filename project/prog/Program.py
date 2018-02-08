from cover_analyser.instructions import Assign


class Program:
    def __init__(self, program_graph, variables, initial_nodes=[1], final_nodes=["_"]):
        self.program_graph = program_graph
        self.variables = variables
        self.initial_nodes = initial_nodes
        self.final_nodes = final_nodes

    # Initiate the variables
    def _initiate_variables(self, init_values):
        for variable in self.variables:
            variable.value = init_values[variable.name]

    # Used for TA criterium
    def get_assign_labels(self):
        assign_labels = []
        for edge, attr_dic in self.program_graph.edges.items():
            if isinstance(attr_dic['instr'],Assign):
                assign_labels += [edge]
        return assign_labels
    
    # Used for TD
    def get_if_while_edges(self):
        return
    
    # Used for K_TC
    def get_k_paths(self, k):
        return
    
    # Used for I_TB
    def get_i_while_loops(self, i):
        return

    def get_path(self,initial_value):
        


    
    # TODO: TU, TDU, TC