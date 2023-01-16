from matplotlib import pyplot as plt
import networkx as nx

def plot_graph():
    g1 = nx.DiGraph()
    g1.add_edges_from([("root", "a"), ("a", "b"), ("a", "e"), ("b", "c"), ("b", "d"), ("d", "e")])
    plt.tight_layout()
    nx.draw_networkx(g1, arrows=True)
    plt.show()
    plt.clf()

plot_graph()