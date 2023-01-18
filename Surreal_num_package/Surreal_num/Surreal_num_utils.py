from matplotlib import pyplot as plt
import networkx as nx


def plot_graph(edges=[("[SN(0)]", "a"), ("a", "b"), ("a", "e"), ("b", "c"), ("b", "d"), ("d", "e")]):
    g1 = nx.DiGraph()
    g1.add_edges_from(edges)
    plt.tight_layout()
    nx.draw_networkx(g1, arrows=True)
    plt.show()
    plt.clf()
