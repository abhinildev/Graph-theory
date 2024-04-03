import networkx as nx
import matplotlib.pyplot as plt

def create_bipartite_graph(nodes1, nodes2, edges):
    G = nx.Graph()
    G.add_nodes_from(nodes1, bipartite=0)
    G.add_nodes_from(nodes2, bipartite=1)
    G.add_edges_from(edges)
    return G

def draw_bipartite_graph(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='red', node_size=1000, font_size=10)
    plt.show()

nodes1 = [1, 2, 3]
nodes2 = ['A', 'B', 'C']
edges = [(1, 'A'), (1, 'B'), (2, 'B'), (2, 'C'), (3, 'C')]
G = create_bipartite_graph(nodes1, nodes2, edges)
draw_bipartite_graph(G)
