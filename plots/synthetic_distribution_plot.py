#!/usr/bin/python3

import json
import matplotlib.pyplot as plt
import numpy as np
import sys
import scipy.stats as stats

np.random.seed(2021)

names = ["SBS1","SBS2","SBS3","SBS4","SBS5","SBS9","SBS13","SBS17a","SBS17b","SBS18","SBS28","SBS40"]
freq = [0.94736842,0.57894737,0.07894737,0.55263158,0.92105263,0.02631579,0.57894737,0.07894737,0.07894737,0.21052632,0.02631579,0.31578947]
means = [5.879354,7.187989,8.908202,10.004273,8.309917,5.973810,7.058655,7.135541,7.877526,7.035528,7.868637,8.884260]
sds = [0.7419105,1.4841934,0.3664694,1.0717298,1.1850669,1.0599888,1.6416088,0.8076794,0.8343613,1.6056898,1.0599888,0.8611788]

# 35, 121

selected = [np.random.random() < 1 for f in freq]

fig, ax = plt.subplots()
fig.suptitle('Probability of signature being present')
plt.ylim([0,1])
bp = ax.bar(np.arange(0, len(freq)), freq)
for i, bar in enumerate(bp):
    if selected[i]:
        bar.set_color(f'C{i}')
    else:
        bar.set_color('#aaaaaa')
ax.set_xticks(np.arange(0, len(freq)))
ax.set_xticklabels(names)
ax.set_xlabel("Signature")
ax.set_ylabel("Probability")
plt.show()


fig, axs = plt.subplots((len(means)+2)//3, 3)
fig.suptitle('Distribution of signature exposures')
fig.tight_layout()
for i in range(len(names)):
    ax = axs.flat[i]
    ax.set_title(names[i])
    x = np.linspace(min(means)-2*max(sds), max(means)+2*max(sds), 100)
    color = f'C{i}' if selected[i] else '#aaaaaa'
    ax.plot(np.exp(x), stats.norm.pdf(x, means[i], sds[i]), color=color)
    ax.fill_between(np.exp(x), stats.norm.pdf(x, means[i], sds[i]), step="pre", alpha=0.4, color=color)
    sel = np.exp(stats.norm.rvs(means[i], sds[i]))
    if selected[i] and False:
        ax.axvline(sel, color='k', linewidth=1)
        ax.text(np.exp(np.log(sel)+0.4), 0.5, int(sel))
    ax.set_xscale("log")
    ax.set_xlabel("Exposure")
    ax.set_ylim([0,0.6])
plt.show()
