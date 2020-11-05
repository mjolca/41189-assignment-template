## Threshold model using underlying libs.
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

from thresholdmodel import ThreshModel

N = 3000
k = 10


initially_infected = np.arange(400)

G = nx.fast_gnp_random_graph(N, k/(N-1.0))
thresholds = np.random.rand(G.number_of_nodes()) 

Thresh = ThreshModel(G,initially_infected,thresholds)
t, a = Thresh.simulate()

plt.plot(t,a)
plt.ylim([0,1])
plt.xlabel('time $[1/\gamma]$')
plt.ylabel('total converted')
plt.gcf().savefig('granov_model.png')
plt.show()
