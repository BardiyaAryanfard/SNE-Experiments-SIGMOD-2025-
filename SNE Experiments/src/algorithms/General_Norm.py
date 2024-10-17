import math
import random

from src.util.BCM_optimized import BCMOpt


class GeneralNorm:
    def __init__(self, T, n, epsilon, alpha, div):
        self.T = T
        self.n = n
        self.epsilon = epsilon
        self.xi = 1 + alpha
        self.xi_H = math.log(n * T) * math.log(T) / epsilon
        self.f_threshold = int(
            random.uniform(4 * self.xi_H / math.pow(alpha, 2), (4 + alpha) * self.xi_H / math.pow(alpha, 2)))
        self.b_threshold = int(2.0 * math.log(self.f_threshold, 1 + alpha) * self.xi_H / alpha)
        print(self.T, self.n, self.epsilon, self.xi, self.b_threshold, self.f_threshold)
        self.b_threshold = int(self.b_threshold / div)
        self.f_threshold = int(self.f_threshold / div)
        self.f = []
        self.heavy_f = set()
        self.real_f = []
        for i in range(n):
            if i % (int(n / 100)) == 0:
                print(int(i * 100 / n))
            self.f.append(BCMOpt(T, self.epsilon))
            self.real_f.append(0)
        self.b = []
        for i in range(int(math.log(T, self.xi)) + 2):
            self.b.append(BCMOpt(2*n, self.epsilon/math.log(self.f_threshold, 1+alpha)))

    def freq_level(self, x):
        if x == 0:
            return 0
        return int(math.log(x, self.xi) + 1)

    def update(self, u):
        pre_freq = self.real_f[u.element]
        # new
        self.real_f[u.element] += u.sign
        if u.sign == 1:
            if self.real_f[u.element] == int(self.f_threshold / 2):
                self.heavy_f.add(u.element)
        # else:
        #     if self.real_f[u.element] == self.f_threshold - 1:
        #         self.heavy_f.remove(u.element)
        self.f[u.element].update(u.sign)
        post_freq = self.real_f[u.element]
        self.update_level(pre_freq, post_freq)

    def calculate(self):
        V_hat: list[float] = []
        for i in range(len(self.b)):
            b_hat = self.shift_BCM_query(self.b[i].get())
            if b_hat > self.b_threshold:
                for j in range(b_hat):
                    V_hat.append(math.pow(self.xi, i))

        for j in self.heavy_f:
            f_hat = self.shift_BCM_query(self.f[j].get())
            if f_hat > self.f_threshold:
                V_hat.append(f_hat)

        while len(V_hat) < self.n:
            V_hat.append(0)

        return V_hat

    def shift_BCM_query(self, x):
        return max(0, int(x))  # max(0, int(x - math.pow(math.log(self.T, 2), 2) / self.epsilon))

    def update_level(self, pre_freq, post_freq):
        pre_level = self.freq_level(pre_freq)
        post_level = self.freq_level(post_freq)
        if pre_freq > self.f_threshold:
            if post_freq <= self.f_threshold:
                self.b[post_level].update(1)
        else:
            if post_freq <= self.f_threshold:
                if pre_level != post_level:
                    self.b[post_level].update(1)
                    self.b[pre_level].update(-1)
            else:
                self.b[pre_level].update(-1)
