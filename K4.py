import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
edgeList=[(1,2),(1,3),(1,4),(2,4),(2,3),(3,4)]
G=nx.Graph()
G.add_edges_from(edgeList)

#nx.draw_spring(G,with_labels=True)
nx.draw_planar(G,with_labels=True)
plt.show()
