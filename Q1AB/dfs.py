import networkx as nx
import matplotlib.pyplot as plt




graph = {
    "A": ["B"],
    "B": ["C", "D"],
    "C": ["E"],
    "D": ["F"],
    "E": [],
    "F":[]
}

visited = set()


def dfs(node, graph, visited, dNode):
    stack = []

    stack.append(node)

    while stack:
        newNode = stack.pop()

        visited.add(newNode)
        
        print(newNode)

        if newNode == dNode:
            break

        for neighbor in reversed(graph[newNode]):
            stack.append(neighbor)

print("this is Depth-First Search (DFS)")
dfs("A", graph, visited,"E")



















# # --- Build the directed graph ---
# G = nx.DiGraph()
# G.add_edges_from([
#     ("A", "B"),
#     ("B", "C"),
#     ("B", "D"),
#     ("C", "E"),
#     ("D", "F"),
# ])

# # --- Manually place nodes to match the picture layout ---
# pos = {
#     "A": (0.0, 1.0),
#     "B": (1.2, 1.0),
#     "C": (1.0, 0.2),
#     "D": (2.0, 0.2),
#     "E": (1.0, -0.7),
#     "F": (2.0, -0.9),
# }

# # --- Figure + background (dark) ---
# fig, ax = plt.subplots(figsize=(9, 5))
# fig.patch.set_facecolor("black")
# ax.set_facecolor("black")
# ax.set_axis_off()

# # --- Draw nodes (blue circles) ---
# nx.draw_networkx_nodes(
#     G, pos,
#     node_size=1400,
#     node_color="#1da1f2",     # bright blue
#     edgecolors="#0b4f7a",     # darker rim
#     linewidths=2,
#     ax=ax
# )

# # --- Draw labels (white letters) ---
# nx.draw_networkx_labels(
#     G, pos,
#     font_color="white",
#     font_size=14,
#     font_weight="bold",
#     ax=ax
# )

# # --- Draw edges (white arrows) ---
# nx.draw_networkx_edges(
#     G, pos,
#     edge_color="white",
#     width=2.5,
#     arrows=True,
#     arrowstyle="-|>",
#     arrowsize=22,
#     connectionstyle="arc3,rad=0.0",
#     min_source_margin=18,
#     min_target_margin=18,
#     ax=ax
# )

# # Optional title like the screenshot
# ax.text(
#     0.02, 0.95, "Find a path from A to E.",
#     transform=ax.transAxes,
#     color="white",
#     fontsize=16,
#     ha="left",
#     va="top"
# )

# plt.tight_layout()
# plt.show()
