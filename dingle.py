import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import operator

G = nx.Graph()
Matrix = np.array(
    [   #1 2 3 4 7 16171821
        [0,1,1,1,1,1,1,1,1],  # 1
        [1,0,1,1,0,1,1,0,0],  # 2
        [1,1,0,1,0,0,0,0,0],  # 3
        [1,1,1,0,0,0,0,0,0],  # 4
        [1,0,0,0,0,0,0,0,1],  # 7
        [1,1,0,0,0,0,1,0,0],  # 16
        [1,1,0,0,0,1,0,0,0],  # 17
        [1,0,0,0,0,0,0,0,1],  # 18
        [1,0,0,0,1,0,1,0,0],  # 21

    ]
)
for i in range(len(Matrix)):
    for j in range(len(Matrix)):
        if Matrix[i,j]==1:
            G.add_edge(i, j)
pos=nx.spring_layout(G)
colors = [1,2,3,4,5,6,7,8,9]
nx.draw_networkx_nodes(G,pos,node_color=colors)
nx.draw_networkx_edges(G,pos)



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