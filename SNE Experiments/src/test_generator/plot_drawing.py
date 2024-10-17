import math

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker

name = 'rating-full'
name = 'AmazonFineFoodReviews'
name = 'sx-askubuntu'
name = 'wiki-talk-temporal'
name = 'sx-mathoverflow'
name = 'sx-superuser'
experiment_name = name + ''
ids = ['_id1', '_id2', '_id3', '_id4', '_id5']
len_ids = 5.0
divs = ["logT", '1']

input_file = open('../files/' + name + '-translated.txt', 'r')
t = []
ours_L = []
ours_T = []
for i in divs:
    ours_L.append([])
    ours_T.append([])
ans_L = []
ans_T = []
bcm_L = []
bcm_T = []
# dif_ours_l = []
dif_bcm_l = []
# dif_ours_t = []
dif_bcm_t = []
additive_error_T = []
additive_error_L = []
for i in range(5):
    for d in range(len(divs)):
        ours_L[d].append([])
        ours_T[d].append([])
    ans_L.append([])
    ans_T.append([])
    bcm_L.append([])
    bcm_T.append([])
    # dif_ours_t.append([])
    # dif_ours_l.append([])
    dif_bcm_l.append([])
    dif_bcm_t.append([])
    additive_error_T.append([])
    additive_error_L.append([])

alpha = .5
epsilon = .5
fraction = 1000
for d in range(len(divs)):
    for i in range(fraction):
        if d == 0:
            # t.append(0)
            for j in range(3):
                ans_L[j].append(0)
                ans_T[j].append(0)
                bcm_T[j].append(0)
                bcm_L[j].append(0)
        for j in range(3):
            ours_L[d][j].append(0)
            ours_T[d][j].append(0)

T = int(input_file.readline().split(' ')[0])
for ID in ids:
    results_files = []
    for d in divs:
        results_files.append(
            # open('../files/test/' + experiment_name + '_a0.5' + '_d' + str(d) + ID + '_report.txt', 'r'))
            open('../files/test/' + experiment_name + '_a0.5' + '_d' + d + ID + '_report.txt', 'r'))
    for d in range(len(divs)):
        if d == 0:
            for i in range(fraction):
                if ID == '' or ID == '_id1':
                    t.append(int(results_files[d].readline()))
                else:
                    results_files[d].readline()
                for j in range(6):
                    ln = results_files[d].readline().split(' ')
                    ind = j % 3
                    if ln[0][0] == 'L':
                        ans_L[ind][i] += float(ln[1]) / len_ids
                        ours_L[d][ind][i] += float(ln[2]) / len_ids
                        bcm_L[ind][i] += float(ln[3]) / len_ids
                    else:
                        ans_T[ind][i] += float(ln[1]) / len_ids
                        ours_T[d][ind][i] += float(ln[2]) / len_ids
                        bcm_T[ind][i] += float(ln[3]) / len_ids
        else:
            for i in range(fraction):
                results_files[d].readline()
                for j in range(6):
                    ln = results_files[d].readline().split(' ')
                    ind = j % 3
                    if ln[0][0] == 'L':
                        ours_L[d][ind][i] += float(ln[2]) / len_ids
                    else:
                        ours_T[d][ind][i] += float(ln[2]) / len_ids

figure, axis = plt.subplots(2, 3)
for i in range(3):
    axis[0][i].plot(t, ours_L[0][i], color='green', label='Low-Threshold')
    axis[0][i].plot(t, ours_L[1][i], color='red', label='CSNE')
    axis[0][i].plot(t, ans_L[i], color='black', label='NonPrivate')
    axis[0][i].plot(t, bcm_L[i], color='blue', label='Hist')
    axis[1][i].plot(t, ours_T[0][i], color='green', label='Low-Threshold')
    axis[1][i].plot(t, ours_T[1][i], color='red', label='CSNE')
    axis[1][i].plot(t, ans_T[i], color='black', label='NonPrivate')
    axis[1][i].plot(t, bcm_T[i], color='blue', label='Hist')
    axis[0][i].set_title([r'$\ell_1$',r'$\ell_2$',r'$\ell_3$'][i])
    axis[1][i].set_title('Top-' + ['1', '10', '10%'][i])
    for j in range(2):
        formatter = ticker.ScalarFormatter(useMathText=True)
        formatter.set_powerlimits((0, 0))
        axis[j][i].yaxis.set_major_formatter(formatter)

for i in range(3):
    print(ours_L[1][i][len(ours_L[1][i])-1])
    print(ours_T[1][i][len(ours_T[1][i])-1])
# figure.suptitle(name)
plt.subplots_adjust(left=0.05, bottom=None, right=.97, top=None, wspace=.2, hspace=.4)
axis[0][0].legend(loc='upper left', fontsize=10, frameon=False)
plt.show()
