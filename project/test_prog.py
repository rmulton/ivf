# Import
import networkx as nx

# Local imports
import cover_analyser.expressions.boolean as boolean
import cover_analyser.expressions.arithmetic as arithmetic
import cover_analyser.instructions as instructions
from cover_analyser.Var import Var
from program.Program import Program
import cover_analyser.test_criteria as tests

import program.node as node

def create_test_program1():
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

def create_test_program2():
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
    pgm.add_edge(4, 5, attr_dict={"expr": boolean.InfOrEqual(x, Var(value=1)), "instr": instructions.Skip()})

    pgm.add_node(6, attr_dict={"operation":node.Always()})
    pgm.add_edge(4, 6, attr_dict={"expr": boolean.InfOrEqual(x, Var(value=1), no=True), "instr": instructions.Skip()})
    pgm.add_edge(6, 4, attr_dict={"expr": boolean.Always(), "instr": instructions.Assign(x,arithmetic.Min(x,Var(value = 1)))})

    pgm.add_node("_", attr_dict={"operation":node.End()})
    pgm.add_edge(5, "_", attr_dict={"expr": boolean.Always(), "instr": instructions.Assign(x, Var(value=1))})

    # Get the program from the program graph
    pgm = Program(pgm, variables)
    return pgm


if __name__=="__main__":
    # Create the program that we are going to test
    pgm = create_test_program1()

    # Test the TA criterion
    ta_test_set = [{"x": 0},{"x": -1},{"x": 1}]
    tests.test_ta(ta_test_set, pgm)

    # Test the TD criterion
    td_test_set = [{"x": 0}]
    tests.test_td(td_test_set, pgm)

    # Test the KTC criterium
    ktc_test_set = [{"x": 0}, {"x": 5}]
    tests.test_ktc(ktc_test_set, pgm, 2)

    # Test the ITB criterium
    pgm_while = create_test_program2()
    itb_tests_set = [{"x": -2},{"x": -1},{"x": 5}]
    tests.test_itb(itb_tests_set,pgm_while,1)

    # Test the TDef criterium
    test_set = [{"x": 0}, {"x": 5}, {"x": -1}]
    tests.test_tdef(test_set, pgm)

    # Test the TU criterium
    tu_test_set = [{"x": -2},{"x": -1},{"x": 5}]
    tests.test_tu(tu_test_set,pgm_while)

    # Test the TDU criterium
    tdu_test_set = [{"x": -2},{"x": -1},{"x": 5}]
    tests.test_tdu(tu_test_set,pgm_while)

    # Test the TC criterium
    tc_test_set = [{"x": 0}, {"x": 5}, {"x": -1}]
    tests.test_tc(tc_test_set, pgm)
