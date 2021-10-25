#!/usr/bin/python3

import json
import matplotlib.pyplot as plt
import numpy as np
import sys

with open(sys.argv[1]) as f:
    data = json.load(f)

def plot(data, ct):
    fig, axs = plt.subplots((len(data[ct])+2)//3, 3)
    fig.suptitle(f'{ct}: Distribution of calculated exposures')
    for i, d in enumerate(data[ct]):
        ax = axs.flat[i]
        rel = d['estimated.exposure']
        ax.set_title(f"Exposure {d['real.exposure']}")
        ax.hist(rel, bins=np.linspace(0,max(rel),20))
        ax.axvline(sum(rel)/len(rel), color='k', linestyle='dashed', linewidth=1)
    plt.show()

if len(sys.argv) > 2:
    try:
        plot(data, sys.argv[2])
    except KeyError:
        print(data.keys())
else:
    for ct in data:
        plot(data, ct)

# fig, axs = plt.subplots((len(data)+2)//3, 3)
# fig.suptitle('Distribution of p-values')
# for i, d in enumerate(data):
#     ax = axs.flat[i]
#     rel = d['p.values']
#     ax.set_title(f"Exposure {d['real.exposure']}")
#     ax.hist(rel, bins=np.linspace(0,max(rel),20), color='r')
#     ax.axvline(sum(rel)/len(rel), color='k', linestyle='dashed', linewidth=1)
# plt.show()
