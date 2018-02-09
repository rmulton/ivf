from cover_analyser.instructions import Assign, If, While

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
        if_while_edges = list()
        for edge, data in self.program_graph.edges.items():
            attr_dict = data["attr_dict"]
            if isinstance(attr_dict["instr"], If) or isinstance(attr_dict["instr"], While):
                if_while_edges.append(edge)
        return if_while_edges
    
    # Used for K_TC
    def get_k_paths(self, k):
        finished_paths = list()
        unfinished_paths = list()
        initial_edges = self.program_graph.out_edges(self.initial_node)
        for initial_edge in initial_edges:
            unfinished_paths.append([initial_edge])
        # k-1 because we already added the initial edges
        for _ in range(0, k-1):
            finished_paths, unfinished_paths = self.increment_paths(finished_paths, unfinished_paths)
        k_paths = finished_paths + unfinished_paths
        return k_paths
    
    def increment_paths(self, finished_paths, unfinished_paths):
        """
        Takes a list of finished paths and a list of unfinished paths through n nodes. Find the paths
        through n+1 nodes. Add them to the finished paths if the new node is a final node of the graph,
        add them to unfinished_paths otherwise.
        """
        for unfinished_path in unfinished_paths:
            last_node = unfinished_path[-1]
            cur_paths = list(unfinished_path)
            new_paths = list()
            for edge in self.program_graph.out_edges(last_node):
                path_increment = list(cur_paths)
                new_node = edge[1]
                path_increment += [new_node]
                if new_node in self.final_nodes:
                    finished_paths.append(path_increment)
                else:
                    new_paths.append(path_increment)
        return finished_paths, new_paths

        
        return finished_paths, unfinished_paths
    
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
                    path += [edge]
                    node = edge[1]
                    break
        return path

        


    
    # TODO: TU, TDU, TC