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
        for edge, data in self.program_graph.edges.items():
            attr_dict = data["attr_dict"]
            if isinstance(attr_dict['instr'],Assign):
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
        return


    def get_1_while_loops(self):
        l = [[1,(1,2),2,(2,4),4,(4,5),5,(5,"_"),"_"],[1,(1,2),2,(2,4),4,(4,6),6,(6,4),4,(4,5),5,(5,"_"),"_"],
             [1,(1,3),3,(3,4),4,(4,5),5,(5,"_"),"_"]]
        return l

    # Used for I_TB
    # def get_i_while_loops(self, i):
    #     #Extracting while_loops
    #     while_loops = []
    #     for edge in self.program_graph.edges:
    #         for edge2 in self.program_graph.edges:
    #             if edge[0] == edge2[1] and edge[1] == edge2[0] and (edge[1],edge[0]) not in while_loops:
    #                 while_loops.append(edge)
    #     for edge in while_loops:
    #         edges = self.program_graph.out_edges(edge[0])
    #         for edg_out in edges:
    #             if edg_out[1] == edge[1]:
    #                 pass
    #             else:
    #                 data = self.program_graph.get_edge_data(edge[0], edge[1])
    #                 attr_dict = data['attr_dict']




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