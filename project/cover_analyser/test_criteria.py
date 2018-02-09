import networkx as nx
from cover_analyser.instructions import Assign

def test_ta(test_set, program):
    """
    Wrapper function that instantiates a TA object and runs TA.test(test_set, program)
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

def test_itb(test_set, program,i):
    """
    Wrapper function that instantiates a TB(i) object and runs ITB.test(test_set, program)
    """
    tester = I_TB(i)
    tester.test(test_set, program)
    return

def test_tdef(test_set, program):
    """
    Wrapper function that instantiates a TDef object and runs TDef.test(test_set, program)
    """
    tester = TDef()
    tester.test(test_set, program)
    return

def test_tu(test_set, program):
    """
    Wrapper function that instantiate a TU object and runs TU.test(test_set, program)
    """
    tester = TU()
    tester.test(test_set, program)
    return

def test_tdu(test_set, program):
    """
    Wrapper function for ITB.test(test_set, program)
    """
    tester = TDU()
    tester.test(test_set, program)
    return

def test_tc(test_set, program):
    """
    Wrapper function for ITB.test(test_set, program)
    """
    tester = TC()
    tester.test(test_set, program)
    return

class TA:
    """
    Implements the All Affections criterium
    """
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
    """
    Implements the All Decisions criterium
    """
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
    """
    Implements the All k-paths criterium
    """
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
    """
    Implements the All i-loops criterium
    """
    def __init__(self, i):
        self.i = i

    def test(self, test_set, program):
        #get all paths with a while loop of length i
        while_loops = program.get_i_while_loops(self.i)
        #Browse test_set
        for test in test_set:
            # Get the path for the test
            path = program.get_path(test)
            if path in while_loops:
                while_loops.remove(path)
        if len(while_loops)==0:
            print("Test I_TB for i=1 passed")
        else:
            print("Test I_TB for i=1 didn't pass. Some paths are not visited: {}".format(while_loops))

class TDef:
    """
    Implements the All Definitions criterium
    """
    def __init__(self):
        return
    def test(self, test_set, program):
        # On récupère les arrêtes sur lesquelles il y a une assignation
        assignation_edges = program.get_assignation_edges()

        # Pour chaque test, on vérifie si le chemin permet de valider le critère pour une paire
        # (variable, arrête) des noeuds d'assignation contenus par assignation_edges
        for test in test_set:
            # On récupère le chemin associé au test
            path = program.get_path(test)
            # On filtre les noeuds pour obtenir ceux qui sont contenus dans assignation_edges
            for i, edge in enumerate(path):
                # S'il est dans assignation_edges, on parcours la fin du chemin pour voir si la variable qui
                # a reçu une assignation est utilisée
                if edge in assignation_edges.values() and len(path)>i:
                    for ass_variable, ass_edge in assignation_edges.items():
                        if edge==ass_edge:
                            var = ass_variable
                    end_of_path = path[i+1:]
                    for edge_to_end in end_of_path:
                        edge_data = program.program_graph.get_edge_data(*edge_to_end)["attr_dict"]
                        instr = edge_data["instr"]
                        expr = edge_data["expr"]
                        used_vars = instr.variables() + expr.variables()
                        if var in used_vars:
                            assignation_edges.pop(var, None)
        if len(assignation_edges)==0:
            print("Test TDef passed")
        else:
            print("Test TDef didn't pass. Some variables {} are not used on edges: {}".format(assignation_edges.keys(), assignation_edges))

class TU:
    """
    Implements the All Use criterium
    """
    def __init__(self):
        pass
    def test(self, test_set, program):
        #Retrieve utilisation paths
        tu_paths = program.get_utilisation_paths()
        tu_paths_new = []
        for elt in tu_paths:
            tu_paths_new.append(elt[0])
        #browse test_set
        for test in test_set:
            # Get the path for the test
            path = program.get_path(test)
            if path in tu_paths_new:
                tu_paths_new.remove(path)
        if len(tu_paths_new)==0:
            print("Test TU passed")
        else:
            print("Test TU didn't pass. Some paths are not visited: {}".format(tu_paths_new))


class TDU:
    """
    Implements the All DU-paths criterium
    """
    def __init__(self):
        return
    def test(self, test_set, program):
        # Retrieve DU paths
        tdu_paths = program.get_DU_paths()
        # Browse test_set
        for test in test_set:
            # Get the path for the test
            path = program.get_path(test)
            if path in tdu_paths:
                tdu_paths.remove(path)
        if len(tdu_paths) == 0:
            print("Test TDU passed")
        else:
            print("Test TDU didn't pass. Some paths are not visited: {}".format(tdu_paths))

class TC:
    """
    Implements the All conditions criterium
    """
    def __init__(self):
        return
    def test(self, test_set, program):
        # Get all the conditons in the graph
        conditions = program.get_conditions()
        for test in test_set:
            # Get the path for the test
            path = program.get_path(test)
            for edge in path:
                decision = program.program_graph.get_edge_data(*edge)["attr_dict"]["expr"]
                for edge_cond in decision.conditions():
                    if edge_cond in conditions:
                        conditions.remove(edge_cond)
        if len(conditions) == 0:
            print("Test TC passed")
        else:
            print("Test TC didn't pass. Some conditions are not satisfied by any test provided: {}".format(tdu_paths)) 
