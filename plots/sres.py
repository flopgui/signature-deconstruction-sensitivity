#!/usr/bin/python3

import json
import matplotlib.pyplot as plt
import numpy as np
import sys

with open(sys.argv[1]) as f:
    data = json.load(f)

# res = []
# for sample in fn:
#     detected = [1 if a['chisq.p'] < 0.05 else 0 for a in sample]
#     detected = sum(detected) / len(detected)
#     res.append(detected)

t_exp = '0'

# plt.ylim([0, 0.5])
plt.xlim([0, 0.25])
plt.ylim([0, 1.01])

fn = data['Pan']['true.negatives'][t_exp]
res = []
for sample in fn:
    exposure = [a['exp.with']['8_SBS31_0.950675_0.99']/sum(a['exp.with'].values()) for a in sample]
    # res.append(sum(exposure)/len(exposure))
    res.extend(exposure)
hist = np.histogram(res, bins=50, range=[0, 0.25])
cp = [(a+b)/2 for a,b in zip(hist[1][:-1], hist[1][1:])]
vals = [a/sum(hist[0]) for a in hist[0]]
s = 0
cvals = []
for v in vals:
    s += v
    cvals.append(s)
# plt.bar(cp, cvals, width=(cp[1]-cp[0])/2, color='C0', label='True negatives')
plt.plot(cp, cvals, color='C0', label='True negatives')
# plt.fill_between(cp, cvals, color='#aec7e8')
cvalsp = cvals

fn = data['Pan']['false.negatives'][t_exp]
res = []
for sample in fn:
    exposure = [a['exp.with']['8_SBS31_0.950675_0.99']/sum(a['exp.with'].values()) for a in sample]
    # res.append(sum(exposure)/len(exposure))
    res.extend(exposure)
hist = np.histogram(res, bins=50, range=[0, 0.25])
cp = [(a+b)/2 for a,b in zip(hist[1][:-1], hist[1][1:])]
vals = [a/sum(hist[0]) for a in hist[0]]
s = 0
cvals = []
for v in vals:
    s += v
    cvals.append(s)
# plt.bar(cp, cvals, width=(cp[1]-cp[0])/2, color='C1', label='False negatives')
plt.plot(cp, cvals, color='C1', label='False negatives')
# plt.fill_between(cp, cvals, color='#ffbb78')
# plt.fill_between(cp, cvalsp, cvals, color='#ffbb78')
plt.fill_between(cp, cvalsp, cvals, color='#aec7e8')
plt.fill_between(cp, cvals, color='#ffbb78')

plt.legend()
plt.xlabel('Detected exposure')
plt.show()
