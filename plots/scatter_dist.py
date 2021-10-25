#!/usr/bin/python3

import json
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import sys
from scipy.interpolate import make_interp_spline, BSpline

with open(sys.argv[1]) as f:
    data = json.load(f)

def plot(data, ct):
    d = data[ct]
    sel = [e for i, e in enumerate(d['real.exposure']) if abs(d['estimated.exposure'][i] - 0.08) < 0.005]
    mean = sum(sel) / len(sel)
    hist = np.histogram(sel)
    hist = (list(map(lambda x: x/sum(hist[0]), hist[0])), hist[1])
    points = [(a+b)/2 for a, b in zip(hist[1][:-1], hist[1][1:])]
    cumul = []
    s = 0
    for h in hist[0]:
        s += h
        cumul.append(s)
    xnew = np.linspace(min(points), max(points), 300) 
    spl = make_interp_spline(points, hist[0], k=2)  # type: BSpline
    sm = spl(xnew)
    plt.plot(xnew, sm)
    minx = np.where(np.array(cumul) > 0.05)[0][0]
    maxx = np.where(np.array(cumul) < 0.95)[0][-1] + 1
    minv = hist[1][minx]
    maxv = hist[1][maxx]
    wh = (minv < xnew) & (xnew < maxv)
    plt.fill_between(xnew[wh], sm[wh], alpha=0.5, label='95% confidence')
    plt.axvline(mean, color='r', linestyle='dashed', linewidth=2, label='Mean')
    plt.axvline(0.08, color='k', linewidth=1, label='Inferred exposure')
    plt.xlim([.03, .13])
    plt.ylim([0, .35])
    plt.xlabel('Real exposure')
    plt.ylabel('Probability density')
    plt.legend()
    # plt.plot(points, hist[0])

if len(sys.argv) > 2:
    try:
        plot(data, sys.argv[2])
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
