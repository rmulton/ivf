from cover_analyser.instructions import Assign


class Program:
    def __init__(self, program_graph, variables, initial_node=1, final_nodes=["_"]):
        self.program_graph = program_graph
        self.variables = variables
        self.initial_node = initial_node
        self.final_nodes = final_nodes

    # Initiate the variables
    def _initiate_variables(self, init_values):
        for variable_name, variable in self.variables.items():
            variable.value = init_values[variable_name]

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

    def get_path(self, initial_value):
        # Initiate variables
        self._initiate_variables(initial_value)
        # Initialize browsing
        node = self.initial_node
        path = []
        while node not in self.final_nodes:
            # Edges coming out from actual node
            edges = self.program_graph.out_edges(node)
            for edge in edges:
                data = self.program_graph.get_edge_data(edge[0], edge[1])
                attr_dict = data["attr_dict"]
                if attr_dict['expr'].result():
                    attr_dict['instr'].run()
                    path += [node,edge]
                    node = edge[1]
                    break
        path.append(node)
        return path

        


    
    # TODO: TU, TDU, TC