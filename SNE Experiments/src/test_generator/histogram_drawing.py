import math
import string

import matplotlib.pyplot as plt
import numpy as np

name = ('rating-full')
input_file = open('../files/' + name + '-translated.txt', 'r')
T1 = int(input_file.readline().split(' ')[0])
n = T1
edges = []
v_map = {}
f = []
f1 = []
f2 = []
f3 = []
for i in range(n):
    f.append(0)
T_new = 0
for i in range(0):
    tmp = input_file.readline()
for i in range(T1):
    try:
        ln = input_file.readline().split(' ')
        tmp = ln[0]
        tmp.translate({ord(c): None for c in string.whitespace})
        if v_map.keys().__contains__(tmp) is False:
            v_map.update({tmp: len(v_map)})
        f[v_map[tmp]] += 1
        T_new += 1
    except:
        continue

n = len(v_map)
f = f[0:n]
f1 = []
f2 = []
f3 = []
f4 = []
f5 = []
f6 = []

f.sort()
f.reverse()
t = []
for i in range(n):
    if i % 1000 == 0:
        print(str(i) + " " + str(f[i]))
    t.append(i)

for i in range(n):
    f1.append(math.pow(math.log(f[i]+1, 2),1))
    f2.append(math.pow(math.log(f[i]+1, 2),.5))
    f3.append(math.pow(math.log(f[i]+1, 2),2))
    f4.append(math.pow(math.log(f[i]+1, 2),3))
    f5.append(math.pow(math.log(f[i]+1, 2),4))
    f6.append(math.pow(math.log(f[i]+1, 2),1.5))
    # t[i] = math.pow(math.log(t[i]+1, 2),1)
fig, ax = plt.subplots()
# ax.plot([math.log(x) for x in t], [math.log(x) for x in f], linewidth=5.0, color='green')
ax.plot([math.log(x+1) for x in t], f1, linewidth=5.0, color='blue')
# ax.plot([math.log(x+1) for x in t], f2, linewidth=5.0, color='red')
# ax.plot([math.log(x+1) for x in t], f3, linewidth=5.0, color='orange')
# ax.plot([math.log(x+1) for x in t], f4, linewidth=5.0, color='brown')
# ax.plot([math.log(x+1) for x in t], f5, linewidth=5.0, color='green')
# ax.plot([math.log(x+1) for x in t], f6, linewidth=5.0, color='green')
# plt.xscale("log")
# plt.yscale("log")
plt.show()
