# Import
import networkx as nx

# Local imports
import cover_analyser.expressions.boolean as boolean
import cover_analyser.expressions.arithmetic as arithmetic
import cover_analyser.instructions as instructions
from cover_analyser.Var import Var

import prog.node as node

pgm = nx.DiGraph()
x = Var("x")

# Programme exemple du sujet
pgm.add_node(1, attr_dict={"operation":node.If()})

pgm.add_node(2, attr_dict={"operation":node.Always()})
pgm.add_edge(1, 2, attr_dict={"expr": boolean.InfOrEqual(x, 0), "instr": instructions.Skip()})

pgm.add_node(3, attr_dict={"operation":node.Always()})
pgm.add_edge(1, 3, attr_dict={"expr": boolean.InfOrEqual(x, 0, no=True), "instr": instructions.Skip()})

pgm.add_node(4, attr_dict={"operation":node.If()})
pgm.add_edge(2, 4, attr_dict={"expr": boolean.Always(), "instr": instructions.Assign(x, arithmetic.Min(0, x))})
pgm.add_edge(3, 4, attr_dict={"expr": boolean.Always(), "instr": instructions.Assign(x, arithmetic.Min(1, x))})

pgm.add_node(5, attr_dict={"operation":node.Always()})
pgm.add_edge(4, 5, attr_dict={"expr": boolean.Equal(x, 1), "instr": instructions.Skip()})

pgm.add_node(6, attr_dict={"operation":node.Always()})
pgm.add_edge(4, 6, attr_dict={"expr": boolean.Equal(x, 1, no=True), "instr": instructions.Skip()})

pgm.add_node("_", attr_dict={"operation":node.End()})
pgm.add_edge(5, "_", attr_dict={"expr": boolean.Always(), "instr": instructions.Assign(x, 1)})
pgm.add_edge(6, "_", attr_dict={"expr": boolean.Always(), "instr": instructions.Assign(x, arithmetic.Add(x, 1))})

print(pgm.edges, pgm.nodes)
