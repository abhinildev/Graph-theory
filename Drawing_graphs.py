import networkx as nx
import matplotlib.pyplot as plt

edgeList=[{1,2},{2,3},{3,1},{4,6},{5,6},{6,3}]

G=nx.Graph()
G.add_edges_from(edgeList)
print(nx.adjacency_matrix(G))

#nx.draw(G,with_labels=True)
#nx.draw_circular(G,with_labels=True)
#nx.draw_spring(G,with_labels=True)
#nx.draw_spectral(G,with_labels=True)
nx.draw_random(G,with_labels=True)
plt.show()
