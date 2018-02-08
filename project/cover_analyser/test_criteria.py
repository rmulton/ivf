import networkx as nx

class TA:
    def __init__(self):
        return
    def test(self, test_set, program):
        assign_labels = program.get_assign_labels()
        # Stuff
        if len(assign_labels)==0:
            return True
        else:
            return False

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
            for node_or_edge in path:
                # If it is a node
                if isinstance(node_or_edge, nx.OutEdgeView):
                    edge = node_or_edge
                    # If the edge is in the if_while_edges list, it can be removed
                    if edge in if_while_edges:
                        if_while_edges.remove(edge)
        # If the list of edges is empty, the test pass, otherwise it doesn't.
        if len(if_while_edges)==0:
            return True
        else:
            return False

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
            path = program.get_path(test)
            # If the path is in the paths of length inferior or equal to k, remove it
            if path in k_paths:
                k_paths.remove(path)
        # If k_paths is empty, the test pass, otherwise it doesn't
        if len(k_paths)==0:
            return True
        else:
            return False

class I_TB:
    def __init__(self, i):
        self.i = i
        return
    def test(self, test_set, program):
        return

class TDef:
    def __init__(self):
        return
    def test(self, test_set, program):
        return

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

