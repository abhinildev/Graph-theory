import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G= nx.from_numpy_array(np.array([[0,1,0],
                                 [1,1,1],
                                 [0,0,0]]))
nx.draw(G,with_labels=True)
plt.show()
