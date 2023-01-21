from matplotlib import pyplot as plt
from ..Surreal_num import *
import networkx as nx

def plot_graph():
    g1 = nx.DiGraph()
    g1.add_edges_from([("root", "a"), ("a", "b"), ("a", "e"), ("b", "c"), ("b", "d"), ("d", "e")])
    plt.tight_layout()
    nx.draw_networkx(g1, arrows=True)
    plt.show()
    plt.clf()
    plot_graph()
def Full_generato(num:int):
    lines = [str(Surreal_num.Generator.üsr_day(num)).replace(',','\n')]
    with open('Fullgenerato.txt', 'w') as f:
        for line in lines:
            f.write(line)
            f.write('\n')
def half_generato():
    lines = [str(Surreal_num.Generator.generate_day(num)).replace(',','\n')]
    with open('Halfgenerato.txt', 'w') as f:
        for line in lines:
            f.write(line)
            f.write('\n')
