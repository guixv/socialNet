import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import operator

G = nx.Graph()
Matrix = np.array(
    [
        [0,1,0,1,1,0,1,0,0,0,0,0,0,0],  # 101
        [1,0,1,0,0,1,1,1,0,0,0,0,0,0],  # 102
        [0,1,0,1,1,0,0,1,0,0,0,0,0,0],  # 103
        [1,0,1,0,0,1,1,1,0,0,0,0,0,0],  # 104
        [1,0,1,0,0,1,0,1,0,0,0,0,0,0],  # 105
        [0,1,0,1,1,0,1,1,0,0,0,0,0,0],  # 106
        [1,1,0,1,0,1,0,1,0,0,0,0,0,0],  # 110
        [0,1,1,1,1,1,1,0,1,1,1,0,0,1],  # 107
        [0,0,0,0,0,0,0,1,0,1,0,1,0,0],  # 108
        [0,0,0,0,0,0,0,1,1,0,1,1,1,0],  # 109
        [0,0,0,0,0,0,0,1,0,1,0,0,1,0],  # 111
        [0,0,0,0,0,0,0,0,1,1,0,0,0,1],  # 114
        [0,0,0,0,0,0,0,0,0,1,1,0,0,0],  # 116
        [0,0,0,0,0,0,0,1,0,0,0,1,0,0],  # 506
    ]
)
for i in range(len(Matrix)):
    for j in range(len(Matrix)):
        if Matrix[i,j]==1:
            G.add_edge(i, j)

nx.draw(G)


asp = nx.average_shortest_path_length(G)
print("平均最短路径为：")
print('%.4f' % asp)
dc = nx.degree_centrality(G)
print("节点编号及其度中心度值为：")
print(dc)
cc = nx.algorithms.bipartite.centrality.closeness_centrality(G,G.nodes())
print("节点编号及其接近中心度值为：")
print(cc)
bc = nx.algorithms.betweenness_centrality(G,normalized=False)
print("节点编号及其中介中心度值为：")
print(bc)
t = nx.transitivity(G)
print("传递性：")
print('%.4f' % t)
plt.show()
