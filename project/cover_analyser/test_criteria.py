
import networkx as nx
from cover_analyser.instructions import Assign

def test_ta(test_set, program):
    """
    Wrapper function for TA.test(test_set, program)
    """
    tester = TA()
    tester.test(test_set, program)


def test_td(test_set, program):
    """
    Wrapper function that instantiates a TD object and runs TD.test(test_set, program)
    """
    tester = TD()
    tester.test(test_set, program)
    return

def test_ktc(test_set, program, k):
    """
    Wrapper function that instantiates a K_TC(k) object and runs K_TC.test(test_set, program)
    """
    tester = K_TC(k)
    tester.test(test_set, program)
    return

def test_itb(test_set, program):
    """
    Wrapper function for ITB.test(test_set, program)
    """
    tester = I_TB()
    tester.test(test_set, program)
    return

def test_tdef(test_set, program):
    tester = TDef()
    tester.test(test_set, program)
    return

class TA:
    def __init__(self):
        return
    def test(self, test_set, program):
        #Get the assign edges
        assign_labels = program.get_assign_labels()
        # Run the program for all the test set, and remove labels of visited nodes
        for test in test_set:
            # Get the path for the test
            path = program.get_path(test)
            for node_or_edge in path:
                #Test if is an edge
                if isinstance(node_or_edge,tuple):
                    data = program.program_graph.get_edge_data(node_or_edge[0],node_or_edge[1])
                    attr_dict = data['attr_dict']
                    if isinstance(attr_dict['instr'],Assign):
                        if node_or_edge in assign_labels:
                            assign_labels.remove(node_or_edge)

        if len(assign_labels)==0:
            print("Test TA passed.")
        else:
            print("Test TA didn't pass. Some assign edges are not visited: {}".format(assign_labels))

class TD:
    def __init__(self):
        return
    def test(self, test_set, program):
        # Get the nodes with if or while labels
        if_while_edges = set(program.get_if_while_edges())
        # Run the program for all the test set, and remove labels of visited nodes
        for test in test_set:
            # Get the path for the test
            path = program.get_path(test)
            for edge in path:
                # If the edge is in the if_while_edges list, it can be removed
                if edge in if_while_edges:
                    if_while_edges.remove(edge)
        # If the list of edges is empty, the test pass, otherwise it doesn't.
        if len(if_while_edges)==0:
            print("Test TD passed.")
        else:
            print("Test TD didn't pass. Some if or while edges are not visited: {}".format(if_while_edges))

class K_TC:
    def __init__(self, k):
        self.k = k
        return
    def test(self, test_set, program):
        # Get the paths of length inferior or equal to k
        k_paths = program.get_k_paths(self.k)
        # Remove from k_paths the paths that the program follows when using the test set
        for test in test_set:
            # Get the path for the test
            exec_path = program.get_path(test)
            # If the path is in the paths of length inferior or equal to k, remove it
            for i in range(min(self.k+1, len(exec_path))):
                i_exec_path = exec_path[:i]
                if i_exec_path in k_paths:
                    k_paths.remove(i_exec_path)
        # If k_paths is empty, the test pass, otherwise it doesn't
        if len(k_paths)==0:
            print("Test {}-TC passed.".format(self.k))
        else:
            print("Test {}-TC didn't pass. Some {}-paths are not visited: {}".format(self.k, self.k, k_paths))

#Only implemented for i =1
class I_TB:
    def __init__(self, i=1):
        self.i = i

    def test(self, test_set, program):
        while_loops_1 = program.get_1_while_loops()
        for test in test_set:
            # Get the path for the test
            path = program.get_path(test)
            if path in while_loops_1:
                while_loops_1.remove(path)
        if len(while_loops_1)==0:
            print("Test I_TB for i=1 passed")
        else:
            print("Test I_TB for i=1 didn't pass. Some paths are not visited: {}".format(while_loops_1))

class TDef:
    def __init__(self):
        return
    def test(self, test_set, program):
        # NB : is test_set useless ?
        # On récupère les arrêtes sur lesquelles il y a une assignation
        assignation_edges = program.get_assignation_edges()
        for variable, edge in assignation_edges.items():
            # On récupère le bout de l'arrête
            starting_node = edge[1]
            # On vérifie qu'il y a un noeud après starting_node utilisant la variable désignée par variable_name
            descendants = nx.descendants(program.program_graph, starting_node)
            for descendant in descendants:
                for outedge in program.program_graph.outedge(descendant):
                    edge_components = outedge.attr_dict["attr_dict"]
                    instr = edge_components["instr"]
                    expr = edge_components["expr"]
                    if variable in instr.variables() + expr.variables():
                        assignation_edges.remove(variable)
        if len(assignation_edges)==0:
            print("Test Tdef passed")
        else:
            print("Test TDef didn't pass. Some variables {} are not used on edges: {}".format(assignation_edges.keys(), assignation_edges))

class TU:
    def __init__(self):
        return
    def test(self, test_set, program_graph):
        return

class TDU:
    def __init__(self):
        return
    def test(self, test_set, program_graph):
        return

class TC:
    def __init__(self):
        return
    def test(self, test_set, program_graph):
        return

