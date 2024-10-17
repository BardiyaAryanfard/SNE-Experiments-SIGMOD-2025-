import math

import matplotlib.pyplot as plt
import numpy as np


# def max_diff(arr1, arr2, t):
#     res = 0
#     for i in range(len(t)):
#         # if t[i] >= t[len(t)-1]/10.0:
#         # if t[i] >= 50000:
#         res = max(res, abs(arr1[i]-arr2[i])*100.0/arr2[i])
#     return res


def avg_diff(arr1, arr2, t):
    res = 0
    num = 0.0
    for i in range(len(t)):
        if t[i] >= t[len(t)-1] * 0.5:
        # if t[i] >= 50000:
            num += 1.0
            res += (abs(arr1[i] - arr2[i]) * 100.0 / arr2[i])
    return (res / num)


def rep(x):
    if x<10:
        return f"{x:.1f}"
    return str(round(x))

def find_diffs(name, epsilon, norm_arr1, norm_arr2):
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
    #
    # alpha = .5
    # epsilon = .5
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
                open('../files/test/' + experiment_name + '_a' + epsilon + '_d' + d + ID + '_report.txt', 'r'))
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

    arrs_lowt = [ours_L[0], ours_T[0]]
    arrs_alg1 = [ours_L[1], ours_T[1]]
    arrs_ans = [ans_L, ans_T]
    arrs_bcm = [bcm_L, bcm_T]

    max_lowt = 0
    max_alg1 = 0
    max_bcm = 0

    for lt in norm_arr1:
        for i in norm_arr2:
            max_lowt = max(max_lowt, avg_diff(arrs_lowt[lt][i], arrs_ans[lt][i], t))
            max_alg1 = max(max_alg1, avg_diff(arrs_alg1[lt][i], arrs_ans[lt][i], t))
            max_bcm = max(max_bcm, avg_diff(arrs_bcm[lt][i], arrs_ans[lt][i], t))

    return [rep(max_bcm), rep(max_alg1), rep(max_lowt)]


names = ['sx-mathoverflow', 'AmazonFineFoodReviews', 'sx-askubuntu', 'sx-superuser', 'wiki-talk-temporal', 'rating-full']
rep_names = ['Math', 'Foods', 'Ubuntu', 'Stack', 'Wiki', 'Movie']

for i in range(len(names)):
    res = []
    for eps in ['0.5','2.0']:
        res.extend(find_diffs(names[i], eps, [0,1], [0,1,2]))
    print('\\hline\n'+rep_names[i]+'              & ' + res[0] + '\\%  & ' + res[1] + '\\%  & ' + res[2] + '\\%         & ' + res[3] + '\\% & ' + res[4] + '\\% & ' + res[5] + '\\%          \\\\ ')