# Import
import networkx as nx

# Local imports
import cover_analyser.expressions.boolean as boolean
import cover_analyser.expressions.arithmetic as arithmetic
import cover_analyser.instructions as instructions
from cover_analyser.Var import Var
from prog.Program import Program
import cover_analyser.test_criteria as tests

import prog.node as node

def create_test_program():
    # Create the variables
    x = Var()
    variables = {"x":x}

    # Create the program graph
    pgm = nx.DiGraph()

    # Programme exemple du sujet
    pgm.add_node(1, attr_dict={"operation":node.If()})

    pgm.add_node(2, attr_dict={"operation":node.Always()})
    pgm.add_edge(1, 2, attr_dict={"expr": boolean.InfOrEqual(x, Var(value=0)), "instr": instructions.Skip()})

    pgm.add_node(3, attr_dict={"operation":node.Always()})
    pgm.add_edge(1, 3, attr_dict={"expr": boolean.InfOrEqual(x, Var(value=0), no=True), "instr": instructions.Skip()})

    pgm.add_node(4, attr_dict={"operation":node.If()})
    pgm.add_edge(2, 4, attr_dict={"expr": boolean.Always(), "instr": instructions.Assign(x, arithmetic.Min(Var(value=0), x))})
    pgm.add_edge(3, 4, attr_dict={"expr": boolean.Always(), "instr": instructions.Assign(x, arithmetic.Min(Var(value=1), x))})

    pgm.add_node(5, attr_dict={"operation":node.Always()})
    pgm.add_edge(4, 5, attr_dict={"expr": boolean.Equal(x, Var(value=1)), "instr": instructions.Skip()})

    pgm.add_node(6, attr_dict={"operation":node.Always()})
    pgm.add_edge(4, 6, attr_dict={"expr": boolean.Equal(x, Var(value=1), no=True), "instr": instructions.Skip()})

    pgm.add_node("_", attr_dict={"operation":node.End()})
    pgm.add_edge(5, "_", attr_dict={"expr": boolean.Always(), "instr": instructions.Assign(x, Var(value=1))})
    pgm.add_edge(6, "_", attr_dict={"expr": boolean.Always(), "instr": instructions.Assign(x, arithmetic.Add(x, Var(value=1)))})
    # Get the program from the program graph
    pgm = Program(pgm, variables)
    return pgm

pgm = create_test_program()
path = pgm.get_path({"x": 0})
print("0", path)
path = pgm.get_path({"x": 5})
print("5", path)
path = pgm.get_path({"x": -1})
print("-1", path)

# td_test = tests.TD()
# td_test_set = {"x": 0}
# td_test.test(td_test_set, pgm)