import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.DiGraph()

# Add nodes
G.add_nodes_from(["A", "B", "C", "D"])

# Add edges (connections)
G.add_edges_from([
    ("A", "B"),
    ("B", "C"),
    ("B", "D"),
    ("C", "E"),
    ("D", "F"),
])

# Draw the graph
nx.draw(
    G,
    with_labels=True,
    node_size=2000,
    font_size=14
)

plt.show()
