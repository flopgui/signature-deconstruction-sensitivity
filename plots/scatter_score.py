#!/usr/bin/python3

import json
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import sys


def get_scores(fname):
    with open(fname) as f:
        data = json.load(f)

    scores = {}
    for ct in data:
        d = data[ct]
        diff = [abs(a-b) for a, b in zip(d['real.exposure'], d['estimated.exposure'])]
        score = sum(diff) / len(diff)
        scores[ct] = score
    return scores

scores1 = get_scores(sys.argv[1])
del(scores1['Eso-AdenoCA'])
scores2 = get_scores(sys.argv[2])
del(scores2['Eso-AdenoCA'])

plt.bar(np.arange(0, len(scores1)+1), list(scores1.values())+[sum(scores1.values())/len(scores1)], width=.4, label='mSigAct')
plt.bar(np.arange(0.4, len(scores1)+0.4+1), list(scores2.values())+[sum(scores2.values())/len(scores2)], width=.4, label='deconstructSigs')
plt.gca().set_xticks(np.arange(0.2, len(scores1)+0.2+1))
labels = list(scores1.keys())+["AVERAGE"]
labels = [x[:10]+'...' if len(x) > 12 else x for x in labels]
plt.gca().set_xticklabels(labels, rotation='vertical', size=6)
plt.title('SBS31')
plt.xlabel('Cancer type')
plt.ylabel('Mean absolute error')
plt.gcf().set_size_inches(8, 7)
plt.legend()
plt.show()

# for ct, score in scores1.items():
    # print(f'{ct:<20} {score:.3e}')
print(f'AVERAGE  {sum(scores1.values())/len(scores1):.4e}')
print(f'AVERAGE  {sum(scores2.values())/len(scores2):.4e}')

