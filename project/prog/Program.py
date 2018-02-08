class Program:
    def __init__(self, program_graph, variables, initial_nodes=[1], final_nodes=["_"]):
        self.program_graph = program_graph
        self.variables = variables
        self.initial_nodes = initial_nodes
        self.final_nodes = final_nodes
    
    # Used for TA criterium
    def get_assign_labels(self):
        return
    
    # Used for TD
    def get_if_while_edges(self):
        return
    
    # Used for K_TC
    def get_k_paths(self, k):
        return
    
    # Used for I_TB
    def get_i_while_loops(self, i):
        return
    
    # TODO: TU, TDU, TC