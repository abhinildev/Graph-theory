import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G=nx.Graph()
edgeList=[(1,2),(2,3)]
G.add_edges_from(edgeList)
nx.draw(G,with_labels=True)
plt.show()
print(dict(G.degree)[2])
