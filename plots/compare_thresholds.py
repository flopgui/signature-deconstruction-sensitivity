#!/usr/bin/python3

import json
import matplotlib.pyplot as plt
import numpy as np
import sys

with open(sys.argv[1]) as f:
    data = json.load(f)

# tn = [v['true.negatives.th'] for v in data.values()]
# fn = [v['false.negatives.th'] for v in data.values()]

# width = .25
# plt.rc('xtick', labelsize=7) 
# fig, ax = plt.subplots()
# # plt.yscale('log')
# ax.bar(np.arange(len(tn)), [10**((a+b)/2) for a, b in tn], width=width)
# ax.bar(np.arange(len(tn)) + width, [10**((a+b)/2) for a, b in fn], width=width)
# ax.set_xticks(np.arange(len(data)))
# ax.set_xticklabels(data.keys(), rotation='vertical')


plt.rc('xtick', labelsize=7) 
fig, ax = plt.subplots()
plt.yscale('log')
ax.bar(np.arange(len(data)), [10**((a+b)/2) for a, b in data.values()])
ax.set_xticks(np.arange(len(data)))
ax.set_xticklabels(data.keys(), rotation='vertical')

plt.show()
