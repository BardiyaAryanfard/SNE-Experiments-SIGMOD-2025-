import math
import time

from src.algorithms.General_Norm import GeneralNorm
from src.non_private.norms import Norms
from src.util.BCM_optimized import BCMOpt
from src.util.input import Input

epsilon = 0.5
alpha = 0.5

inp_name = input().strip()
inp_divs = list(map(int, input().split()))
inp_ids = list(map(int, input().split()))

# name = 'Artificial-powerlaw-8'
name = inp_name
experiment_name = name + "_a" + str(epsilon)
# divs = [150,200]
divs = inp_divs
print(name)
print(divs)


def run_test(input_name, out_file):
    t_0 = time.time()
    input_file = open(input_name, 'r')
    inp = Input.read_input(input_file)
    our_mech = []
    # print("div: " + str(math.log(inp.T, 2) / (epsilon * math.pow(alpha, 2))))
    # our_mech.append(GeneralNorm(inp.T, inp.n, epsilon, alpha, math.log(inp.T, 2) / (epsilon * math.pow(alpha, 2))))
    our_mech.append(GeneralNorm(inp.T, inp.n, epsilon, alpha, 1))
    print('input file read')
    t_1 = time.time()
    print(t_1 - t_0)
    # f = []
    # bcm = []
    # last_bcm = []
    L_norms = [1, 2, 3]
    L_norms_names = ['1', '2', '3']
    Top_norms = [1, 10, int(inp.n / 10)]
    Top_norms_names = ['1', '10', '10p']
    # for i in range(inp.n):
    #     f.append(0)
        # bcm.append(BCMOpt(inp.T, epsilon))
        # last_bcm.append(0)
    our_output = []
    our_output.append([])
    fraction = 1000.0
    for t in range(inp.T):
        # last_bcm[inp.stream.get(t).element] = bcm[inp.stream.get(t).element].update(inp.stream.get(t).sign)
        for mech in our_mech:
            mech.update(inp.stream.get(t))
        # f[inp.stream.get(t).element] += inp.stream.get(t).sign
        if t % (int(inp.T / fraction)) == 0:
            print(str((100.0 * t / inp.T)) + "%: " + str(int(time.time() - t_1)))
            our_output = []
            for d in range(len(divs)):
                our_output.append(our_mech[d].calculate())
                out_file[d].write(str(t) + '\n')
                for i in range(len(L_norms)):
                    # out_file[d].write('L' + L_norms_names[i] + ' ' + str(Norms.L(L_norms[i], f)) + ' ' + str(Norms.L(L_norms[i], our_output[d])) + ' ' + str(Norms.L(L_norms[i], last_bcm)) + '\n')
                    out_file[d].write('L' + L_norms_names[i] + ' ' + str(0) + ' ' + str(Norms.L(L_norms[i], our_output[d])) + ' ' + str(0) + '\n')
                for i in range(len(Top_norms)):
                    # out_file[d].write('T' + Top_norms_names[i] + ' ' + str(Norms.top_k(Top_norms[i], f)) + ' ' + str(Norms.top_k(Top_norms[i], our_output[d])) + ' ' + str(Norms.top_k(Top_norms[i], last_bcm)) + '\n')
                    out_file[d].write('T' + Top_norms_names[i] + ' ' + str(0) + ' ' + str(Norms.top_k(Top_norms[i], our_output[d])) + ' ' + str(0) + '\n')
    input_file.close()
    t_2 = time.time()
    print(t_2 - t_0)


inp_name = '../files/' + name + '-translated.txt'
for ID in inp_ids:
    files = []
    files.append(open('../files/test/' + experiment_name + '_d1' + '_id' + str(ID) + '_report.txt', 'w'))
    run_test(inp_name, files)
    for file in files:
        file.close()
