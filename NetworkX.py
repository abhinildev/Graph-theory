import networkx as nx 
import matplotlib.pyplot as plt 
  
  
G= nx.Graph()

G.add_edge(1,2)
G.add_edge("A","B")

nx.draw(G, with_labels=True)
plt.show()
