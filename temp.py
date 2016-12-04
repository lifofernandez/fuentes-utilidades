import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import PatchCollection
from matplotlib.patches import Wedge, Circle
from math import degrees, pi

fig, ax = plt.subplots()
wedges = []
circles = []

# Generar objetos
x = 1.5
y = 1.5
theta, phi = np.random.random(2)  # functions of (x,y) in reality
for v in (0, pi):
    wedges.append(
        Wedge(
           (x, y),
           .15,
           degrees(v - phi - theta/2),
           degrees(v - phi + theta/2),
           edgecolor='none'
        ),
    )

# Dibujar la cosa

colors = np.linspace(0, 1, len(wedges))  # function of (x,y) in reality

wedge_colors = np.array(
	[colors, colors]
).flatten('F') # no itertools

collection = PatchCollection(
	wedges,
	cmap=plt.cm.jet,
	alpha=1
)
collection.set_array(
	np.array(wedge_colors)
)
collection.set_edgecolor('none')

ax.add_collection(
	collection
)


ax.set_xlim(0,3)
ax.set_ylim(0,3)
ax.set_aspect('equal')
plt.show()