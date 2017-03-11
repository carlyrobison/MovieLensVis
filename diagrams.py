# Helper functions to make diagrams

import matplotlib.pyplot as plt
import numpy as np

def plot_movies(movies, title):
    '''Movies is (label, x, y)'''
    labels = []
    x = []
    y = []
    for m in movies:
        labels.append(m[0])
        x.append(m[1])
        y.append(m[2])
    plot_points(labels, np.asarray(x), np.asarray(y), title)

def plot_points(labels, x, y, title):
    '''Plots 2D points with labels'''

    plt.figure()
    plt.title(title)
    # plt.subplots_adjust(bottom = 0.1)
    plt.scatter(x, y, marker='o', c=np.arange(len(labels)), s=50, cmap=plt.get_cmap('Spectral'))

    for label, x, y in zip(labels, x, y):
        plt.annotate(label,
            xy=(x, y), xytext=(-5, 5),
            textcoords='offset points', ha='right', va='bottom')#,
        #bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
        #arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))
    
    plt.axis([-3, 0], [-1, 1])

    plt.grid(True)


def show_plots():
    plt.show()