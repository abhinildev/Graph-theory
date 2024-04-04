import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G=nx.complete_graph(5)

nx.draw_spring(G,with_labels=True)
plt.show()