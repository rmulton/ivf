from cover_analyser.instructions import Assign, If
from cover_analyser.expressions.boolean import InfOrEqual, Equal

class Program:
    """
    Represents a program that contains variables, a program graph, an initial node, and one or several final nodes
    Contains methods that are usefull to test the 8 criteria required for this project
    """
    def __init__(self, program_graph, variables, initial_node=1, final_nodes=["_"]):
        self.program_graph = program_graph
        self.variables = variables
        self.initial_node = initial_node
        self.final_nodes = final_nodes

    # Initiate the variables
    def _initiate_variables(self, init_values):
        """
        Initiate the variables to compute the program
        """
        for variable_name, variable in self.variables.items():
            variable.value = init_values[variable_name]

    # Used for TA criterium
    def get_assign_labels(self):
        """
        Get all the edges with assign labels
        """
        assign_labels = []
        for edge, data in self.program_graph.edges.items():
            attr_dict = data["attr_dict"]
            if isinstance(attr_dict['instr'],Assign):
                assign_labels += [edge]
        return set(assign_labels)
    
    # Used for TD
    def get_if_while_edges(self):
        """
        Get all the edges with if and while loops
        """
        if_while_edges = list()
        for edge, data in self.program_graph.edges.items():
            attr_dict = data["attr_dict"]
            if isinstance(attr_dict["instr"], If):
                if_while_edges.append(edge)
        return if_while_edges
    
    # Used for K_TC
    def get_k_paths(self, k):
        """
        Get all the paths in the graph of length <= k
        """
        if k==0:
            return list()
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

    def get_k_paths_finished(self, k):
        finished_paths = list()
        unfinished_paths = list()
        initial_edges = self.program_graph.out_edges(self.initial_node)
        for initial_edge in initial_edges:
            unfinished_paths.append([initial_edge])
        # k-1 because we already added the initial edges
        for _ in range(0, k-1):
            finished_paths, unfinished_paths = self.increment_paths(finished_paths, unfinished_paths)
        return finished_paths

    def increment_paths(self, finished_paths, unfinished_paths):
        """
        Takes a list of finished paths and a list of unfinished paths through n nodes. Find the paths
        through n+1 nodes. Add them to the finished paths if the new node is a final node of the graph,
        add them to unfinished_paths otherwise.
        """
        new_paths = list()
        for unfinished_path in unfinished_paths:
            last_node = unfinished_path[-1][-1]
            cur_path = list(unfinished_path)
            for edge in self.program_graph.out_edges(last_node):
                path_increment = list(cur_path)
                new_node = edge[1]
                path_increment += [edge]
                if new_node in self.final_nodes:
                    finished_paths.append(path_increment)
                else:
                    new_paths.append(path_increment)
        return finished_paths, new_paths

    def get_1_while_loops(self):
        l = [[1,(1,2),2,(2,4),4,(4,5),5,(5,"_"),"_"],[1,(1,2),2,(2,4),4,(4,6),6,(6,4),4,(4,5),5,(5,"_"),"_"],
             [1,(1,3),3,(3,4),4,(4,5),5,(5,"_"),"_"]]
        return l

    def while_loops_in_path(self,path):
        loops = 0
        for i, edge in enumerate(path):
            loop_loc = 0
            i_loc = i
            if i < (len(path)-1) and edge[0] == path[i+1][1] and edge[1] == path[i+1][0]:
                loop_loc += 1
                i_loc += 2
                while path[i_loc][0] == path[i_loc+1][1] and path[i_loc][1] == path[i_loc+1][0] and \
                                path[i_loc-1][0] == path[i_loc][1] and path[i_loc-1][1] == path[i_loc][0]:
                    loop_loc += 1
                    i_loc += 2
                if loop_loc > loops:
                    loops = loop_loc
        return loops



    # Used for I_TB
    def get_i_while_loops(self, i):
        # Return paths with a while loop of length = i
        i_while_loops = []
        for k in range(i*10):
            k_paths = self.get_k_paths_finished(k)
            for path in k_paths:
                if self.while_loops_in_path(path) == i and path not in i_while_loops:
                    i_while_loops += [path]
        return i_while_loops


    def get_path(self, initial_value):
        """
        Get the path the program follows for initial_value as a list of edges
        """
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
    
    def get_assignation_edges(self):
        """
        Get all the edges that assign a value to a variable
        """
        assignation_edges = dict()
        for edge in self.program_graph.edges:
            if edge[1] not in self.final_nodes:
                instr = self.program_graph.get_edge_data(*edge)["attr_dict"]["instr"]
                vars = instr.variables()
                if isinstance(instr, Assign) and len(vars)>0:
                    assignation_edges[vars[0]] = edge
        return assignation_edges


    def get_utilisation_paths(self):
        # returns path where there is a definition of X and a use of X with no redefinition between the two
        # (path,index of edge of definition in path, index of edge of use in path)

        result = []
        # Because of while loops, we have an infinity of paths. We decide to take paths where length < 20
        for k in range(20):
            #Take only paths that finish
            paths = self.get_k_paths_finished(k)
            #Browse those paths
            for path in paths:
                for i, edge in enumerate(path):
                    data = self.program_graph.get_edge_data(edge[0], edge[1])
                    attr_dict = data["attr_dict"]
                    #Definition is an assign or initial state
                    if isinstance(attr_dict['instr'],Assign) or i== 0:
                        #Browsing the end of the path to look for an assign or a use of the variable
                        for j in range(i+1,len(path)):
                            data_temp = self.program_graph.get_edge_data(path[j][0], path[j][1])
                            attr_dict_temp = data_temp["attr_dict"]
                            # There is another assign so we are not interested by this path
                            if isinstance(attr_dict_temp['instr'],Assign):
                                break
                            # There is a use of the variable so we take it
                            elif isinstance(attr_dict_temp['expr'],InfOrEqual) or isinstance(attr_dict_temp['expr'],Equal):
                                if (path,i,j) not in result:
                                    result.append((path,i,j))
                                    break
        return result

    def get_DU_paths(self):
        #get du paths from tu_paths by checking length of while loops
        result = []
        paths = self.get_utilisation_paths()
        for path,i,j in paths:
            path_temp = path[i:j]
            # If there is no while loop longer than 1 between then we consider the path
            if self.while_loops_in_path(path_temp)<=1 and path not in result:
                result += [path]
        return result
    
    # Used for TC test
    def get_conditions(self):
        """
        Get all the conditions in the graph
        """
        conditions = list()
        for edge in self.program_graph.edges:
            edge_decision = self.program_graph.get_edge_data(*edge)["attr_dict"]["expr"]
            edge_conditions = edge_decision.conditions()
            conditions += edge_conditions
        return conditions
                