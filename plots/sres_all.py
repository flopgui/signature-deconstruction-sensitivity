#!/usr/bin/python3

import json
import matplotlib.pyplot as plt
import numpy as np
import sys

with open(sys.argv[1]) as f:
    data = json.load(f)

# SIGNATURE = '8_SBS31_0.950675_0.99'
# SIGNATURE = '16_SBS11_0.982108_1.0'
SIGNATURE = '20_SBS17b_0.960864_1.0'

# plt.ylim([0, 0.5])
plt.xlim([0, 0.05])
plt.ylim([-0.01, 1.01])
plt.title('SBS17b: Not treated and Not detected')

kk = []
for t_exp in data['Pan']['true.negatives'].keys():
    if t_exp not in ['0', '0.01', '0.1']:
        kk.append(t_exp)
for k in kk:
    del data['Pan']['true.negatives'][k]
    del data['Pan']['false.negatives'][k]

for exp_idx, t_exp in enumerate(data['Pan']['true.negatives']):
    fn = data['Pan']['false.negatives'][t_exp]
    res = []
    for sample in fn:
        exposure = [a['exp.with'][SIGNATURE]/sum(a['exp.with'].values()) for a in sample]
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
    plt.plot(cp, cvals, label=f'Injected exposure {t_exp}', color=f'C{exp_idx}')
    # plt.plot(cp, cvals, color=f'C{exp_idx}')

for exp_idx, t_exp in enumerate(data['Pan']['true.negatives']):
    fn = data['Pan']['true.negatives'][t_exp]
    res = []
    for sample in fn:
        exposure = [a['exp.with'][SIGNATURE]/sum(a['exp.with'].values()) for a in sample]
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
    plt.plot(cp, cvals, color=f'C{exp_idx}', linestyle='--')
    # plt.plot(cp, cvals, label=f'Injected exposure {t_exp}',  color=f'C{exp_idx}', linestyle='--')


plt.plot([], [], color='#7f7f7f', label='Treated & Not detected')
plt.plot([], [], color='#7f7f7f', linestyle='--', label='Not treated & Not detected')


plt.legend()
plt.xlabel('Detected exposure')
plt.ylabel('Cumulative probability')
plt.show()
