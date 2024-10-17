import math

import matplotlib.pyplot as plt
import numpy as np

def report(time_step, p):
    print('L' + str(p + 1) + ': NonPrivate=' + str(round(ans_L[p][time_step])))
    print('hist: ' + str([round(val) for val in bcm_L[p][time_step]]) +
          ' Mean: ' + str(round(np.mean(bcm_L[p][time_step]))) +
          ' Std dev: ' + str(np.std(bcm_L[p][time_step])))
    print('Low-T: ' + str([round(val) for val in ours_L[0][p][time_step]]) +
          ' Mean: ' + str(round(np.mean(ours_L[0][p][time_step]))) +
          ' Std dev: ' + str(np.std(ours_L[0][p][time_step])))
    print(['Top-1', 'Top10', 'Top10percent'][p] + ': NonPrivate=' + str(round(ans_T[p][time_step])))
    print('hist: ' + str([round(val) for val in bcm_T[p][time_step]]) +
          ' Mean: ' + str(round(np.mean(bcm_T[p][time_step]))) +
          ' Std dev: ' + str(np.std(bcm_T[p][time_step])))
    print('Low-T: ' + str([round(val) for val in ours_T[0][p][time_step]]) +
          ' Mean: ' + str(round(np.mean(ours_T[0][p][time_step]))) +
          ' Std dev: ' + str(np.std(ours_T[0][p][time_step])))

def report_for_worst(p):
    print('L' + str(p + 1) + ': ')
    print('hist: t=' + str(t[bcm_L_max[p]]) + '\n' + str([round(val) for val in bcm_L[p][bcm_L_max[p]]]) +
          ' Mean: ' + str(round(np.mean(bcm_L[p][bcm_L_max[p]]))) +
          ' Std dev: ' + str(np.std(bcm_L[p][bcm_L_max[p]])))
    print('Low-T: t=' + str(t[LowT_L_max[p]]) + '\n' + str([round(val) for val in ours_L[0][p][LowT_L_max[p]]]) +
          ' Mean: ' + str(round(np.mean(ours_L[0][p][LowT_L_max[p]]))) +
          ' Std dev: ' + str(np.std(ours_L[0][p][LowT_L_max[p]])))
    print(['Top-1', 'Top10', 'Top10percent'][p] + ': ')
    print('hist: t=' + str(t[bcm_T_max[p]]) + '\n' + str([round(val) for val in bcm_T[p][bcm_T_max[p]]]) +
          ' Mean: ' + str(round(np.mean(bcm_T[p][bcm_T_max[p]]))) +
          ' Std dev: ' + str(np.std(bcm_T[p][bcm_T_max[p]])))
    print('Low-T: t=' + str(t[LowT_T_max[p]]) + '\n' + str([round(val) for val in ours_T[0][p][LowT_T_max[p]]]) +
          ' Mean: ' + str(round(np.mean(ours_T[0][p][LowT_T_max[p]]))) +
          ' Std dev: ' + str(np.std(ours_T[0][p][LowT_T_max[p]])))


# name = 'rating-full'
name = 'AmazonFineFoodReviews'
# name = 'sx-askubuntu'
# name = 'wiki-talk-temporal'
# name = 'sx-mathoverflow'
# name = 'sx-superuser'
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
for i in range(5):
    for d in range(len(divs)):
        ours_L[d].append([])
        ours_T[d].append([])
    ans_L.append([])
    ans_T.append([])
    bcm_L.append([])
    bcm_T.append([])

alpha = .5
epsilon = .5
fraction = 1000
for d in range(len(divs)):
    for i in range(fraction):
        if d == 0:
            for j in range(3):
                ans_L[j].append(0)
                ans_T[j].append(0)
                bcm_T[j].append([])
                bcm_L[j].append([])
        for j in range(3):
            ours_L[d][j].append([])
            ours_T[d][j].append([])

T = int(input_file.readline().split(' ')[0])
for ID in ids:
    results_files = []
    for d in divs:
        results_files.append(
            # open('../files/test/' + experiment_name + '_a0.5' + '_d' + str(d) + ID + '_report.txt', 'r'))
            open('../files/test/' + experiment_name + '_a2.0' + '_d' + d + ID + '_report.txt', 'r'))
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
                        ours_L[d][ind][i].append(float(ln[2]))
                        bcm_L[ind][i].append(float(ln[3]))
                    else:
                        ans_T[ind][i] += float(ln[1]) / len_ids
                        ours_T[d][ind][i].append(float(ln[2]))
                        bcm_T[ind][i].append(float(ln[3]))
        else:
            for i in range(fraction):
                results_files[d].readline()
                for j in range(6):
                    ln = results_files[d].readline().split(' ')
                    ind = j % 3
                    if ln[0][0] == 'L':
                        ours_L[d][ind][i].append(float(ln[2]))
                    else:
                        ours_T[d][ind][i].append(float(ln[2]))

LowT_L_max = [0,0,0]
bcm_L_max = [0,0,0]
LowT_T_max = [0,0,0]
bcm_T_max = [0,0,0]
for d in range(len(divs)-1):
    print(['Low-Threshold', 'CSNE'][d])
    for p in range(3):
        try:
            LowT_L_max[p] = np.argmax([np.std(ours_L[d][p][i]) / np.mean(ours_L[d][p][i]) for i in range(5,fraction)]) + 5
        except ValueError:
            print('L' + str(p + 1) + ': NaN')
        try:
            LowT_T_max[p] = np.argmax([np.std(ours_T[d][p][i]) / np.mean(ours_T[d][p][i]) for i in range(5,fraction)]) + 5
        except ValueError:
            print(['Top-1', 'Top10', 'Top10percent'][p] + ': NaN')

# for ts in [250, 500, 750, 999]:
#     print("\n\nt=" + str(t[ts]))
for p in range(3):
    try:
        bcm_L_max[p] = np.argmax([np.std(bcm_L[p][i]) / np.mean(bcm_L[p][i]) for i in range(5, fraction)]) + 5
    except ValueError:
        print('L' + str(p + 1) + ': NaN')
    try:
        bcm_T_max[p] = np.argmax([np.std(bcm_T[p][i]) / np.mean(bcm_T[p][i]) for i in range(5, fraction)]) + 5
    except ValueError:
        print(['Top-1', 'Top10', 'Top10percent'][p] + ': NaN')


for d in range(len(divs)-1):
    print(['Low-Threshold', 'CSNE'][d])
    for p in range(3):
        try:
            print('L' + str(p + 1) + ': ' + str(
                round(1 * np.argmax([np.std(ours_L[d][p][i]) / np.mean(ours_L[d][p][i]) for i in range(5,fraction)]))))
        except ValueError:
            print('L' + str(p + 1) + ': NaN')
        try:
            print(['Top-1', 'Top10', 'Top10percent'][p] + ': ' + str(
                round(1 * np.argmax([np.std(ours_T[d][p][i]) / np.mean(ours_T[d][p][i]) for i in range(5,fraction)]))))
        except ValueError:
            print(['Top-1', 'Top10', 'Top10percent'][p] + ': NaN')

# for ts in [250, 500, 750, 999]:
#     print("\n\nt=" + str(t[ts]))
for p in range(3):
    try:
        print('L' + str(p + 1) + ': ' + str(
            round(1 * np.argmax([np.std(bcm_L[p][i]) / np.mean(bcm_L[p][i]) for i in range(5,fraction)]))))
    except ValueError:
        print('L' + str(p + 1) + ': NaN')
    try:
        print(['Top-1', 'Top10', 'Top10percent'][p] + ': ' + str(
            round(1 * np.argmax([np.std(bcm_T[p][i]) / np.mean(bcm_T[p][i]) for i in range(5,fraction)]))))
    except ValueError:
        print(['Top-1', 'Top10', 'Top10percent'][p] + ': NaN')

for p in range(3):
    report_for_worst(p)