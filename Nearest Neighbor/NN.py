# coding=utf-8
import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def circle(o, r, xlim, ylim):
    x = np.arange(xlim[0], xlim[1], 0.01)
    y = np.arange(ylim[0], ylim[1], 0.01)
    x, y = np.meshgrid(x, y)
    z = (x - o[0]) ** 2 + (y - o[1]) ** 2 - r**2
    plt.contour(x, y, z, levels=[0], colors='r', linewidths=1)


def line(p, q):
    plt.plot([p[0], q[0]], [p[1], q[1]], lw=1, c='k')


def point(p, m='o', c='k', a=1, s=100):
    plt.scatter(p[0], p[1], s=s, marker=m, c=c, alpha=a)

# select two features
iris = sns.load_dataset('iris')
iris = iris.loc[:, ('sepal_width', 'petal_width', 'species')]

# scatter
g = sns.FacetGrid(iris, hue='species', size=5, hue_kws={'marker': '^os'})
g.map(plt.scatter, 'sepal_width', 'petal_width', s=100, linewidth=.5)
g.add_legend()

# set a test data
test = [3.5, 1.0]
point(test, c='w', a=0.5, s=200)

# calculate distance
train = np.array(iris.loc[:, ('sepal_width', 'petal_width')] - test)
delta = np.array([np.sqrt(train[i].dot(train[i].T))
                  for i in range(train.shape[0])])

# sort and find the kth min
k = 1
ids = sorted(range(len(delta)), lambda x, y: 1 if delta[x] > delta[y] else -1)
i = ids[k - 1]
test_nn = [iris.iloc[i, 0], iris.iloc[i, 1]]

# classify
w = iris.loc[ids[:k], :]['species'].value_counts().argmax()
color = g._legend_data[w].get_facecolor()
point(test, c=color)

# draw line and circle
line(test, test_nn)
circle(test, delta[i], [1.5, 4.5], [0, 3])
plt.show()
