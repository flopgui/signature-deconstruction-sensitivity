#!/usr/bin/python3

import json
import matplotlib.pyplot as plt
import numpy as np
import sys
from scipy.stats import kstest

with open(sys.argv[1]) as f:
    data = json.load(f)

SIGNATURE = '8_SBS31_0.950675_0.99'
# SIGNATURE = '16_SBS11_0.982108_1.0'
# SIGNATURE = '20_SBS17b_0.960864_1.0'
T_EXP = '0.01'

# plt.ylim([0, 0.5])
plt.xlim([0, 0.25])
plt.ylim([-0.01, 1.01])
plt.title('SBS31')

kk = []
for t_exp in data['Pan']['true.negatives'].keys():
    if t_exp not in ['0', '0.01', '0.1']:
        kk.append(t_exp)
for k in kk:
    del data['Pan']['true.negatives'][k]
    del data['Pan']['false.negatives'][k]


fn = data['Pan']['false.negatives'][T_EXP]
resf = []
for sample in fn:
    exposure = [a['exp.with'][SIGNATURE]/sum(a['exp.with'].values()) for a in sample]
    resf.extend(exposure)

fn = data['Pan']['true.negatives'][T_EXP]
rest = []
for sample in fn:
    exposure = [a['exp.with'][SIGNATURE]/sum(a['exp.with'].values()) for a in sample]
    rest.extend(exposure)

kt = kstest(resf, rest, alternative='less')
print(kt)
