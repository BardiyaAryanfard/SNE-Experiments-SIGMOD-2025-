import math

from src.util import Laplace
from src.util.Interval import Interval


class BCM:
    def __init__(self, T, epsilon):
        self.root = BCM.Node(None, Interval(0, T), T, epsilon)
        self.t = 0
        self.T = T
        self.epsilon = epsilon

    def update(self, value):
        self.root.update(self.t, value)
        self.t += 1
        return self.get_noisy_sum()

    def get_noisy_sum(self):
        return self.root.get_noisy_sum(Interval(0, self.t))

    def get_real_sum(self):
        return self.root.get_real_sum(Interval(0, self.t))

    class Node:
        def __init__(self, father, interval, T, epsilon):
            self.father = father
            self.interval = interval
            self.noise = Laplace.Laplace.noise(math.log(T, 2) / epsilon)
            self.value = 0
            if interval.len() > 1:
                self.left_child = BCM.Node(self, interval.left_half(), T, epsilon)
                self.right_child = BCM.Node(self, interval.right_half(), T, epsilon)

        def update(self, index, value):
            self.value += value
            if self.interval.len() > 1:
                if self.interval.left_half().contains(index):
                    self.left_child.update(index, value)
                else:
                    self.right_child.update(index, value)

        def get_noisy_sum(self, interval):
            if interval.contains_interval(self.interval):
                return self.value + self.noise
            if (self.interval.right <= interval.left) or (interval.right <= self.interval.left):
                return 0
            return self.left_child.get_noisy_sum(interval) + self.right_child.get_noisy_sum(interval)

        def get_real_sum(self, interval):
            if interval.contains_interval(self.interval):
                return self.value
            if (self.interval.right <= interval.left) or (interval.right <= self.interval.left):
                return 0
            return self.left_child.get_real_sum(interval) + self.right_child.get_real_sum(interval)
