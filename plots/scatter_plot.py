#!/usr/bin/python3

import json
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import sys

with open(sys.argv[1]) as f:
    data = json.load(f)

def plot(data, ct):
    d = data[ct]
    # colors = ['red' if abs(e - 0.08) < 0.005 else 'C0' for e in d['estimated.exposure']]
    colors = ['C0' for e in d['estimated.exposure']]
    plt.scatter(d['real.exposure'], d['estimated.exposure'], s=1, color=colors)
    maxx = max(max(d['real.exposure']), max(d['estimated.exposure']))
    plt.axline((0,0), (maxx, maxx), color='k', linestyle='dashed', linewidth=1)
    # plt.xlim(0, maxx)
    # plt.ylim(0, maxx)
    plt.xlim(0, 0.2)
    plt.ylim(0, 0.25)
    plt.title(ct+'\nSBS31')
    plt.xlabel('Real relative exposure')
    plt.ylabel('Estimated relative exposure')

if len(sys.argv) > 2:
    try:
        plot(data, sys.argv[2])
        # plt.gca().add_patch(patches.Rectangle((0, 0.075), 1, 0.01, fill=True, alpha=0.5, facecolor='yellow'))
        plt.show()
    except KeyError:
        print(data.keys())
else:
    for ct in data:
        plot(data, ct)
        plt.show()

# negatives = set(i for i, p in enumerate(data['p.values']) if p > 0.05)
# re = [e for i, e in enumerate(data['real.exposure']) if i in negatives]
# plt.hist(re, weights=re)
# plt.show()
