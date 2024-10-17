import math

from src.util.Interval import Interval
from src.util.Laplace import Laplace


class BCMOpt:
    def __init__(self, T, epsilon):
        self.root = Node(None, Interval(0, T), T, epsilon, True)
        self.T = T
        self.epsilon = epsilon

    def update(self, value):
        return self.root.update(value)

    def get(self):
        return self.root.last

    def get_real_sum(self):
        return self.root.value


class Node:
    def __init__(self, father, interval, T, epsilon, is_left):
        self.T = T
        self.epsilon = epsilon
        self.father = father
        self.interval = interval
        self.noise = Laplace.noise(math.log(T, 2) / epsilon)
        self.value = 0
        self.is_full = False
        self.noisy_left_sum = 0
        self.is_left_child_full = False
        self.last = 0
        self.is_left = is_left
        if interval.len() > 1:
            self.child = Node(self, interval.left_half(), T, epsilon, True)

    def update(self, value):
        self.value += value
        if self.interval.len() == 1:
            self.is_full = True
            self.last = self.value + self.noise
            return self.value + self.noise
        self.last = self.child.update(value) + self.noisy_left_sum
        if self.child.is_full:
            if self.child.is_left:
                self.noisy_left_sum = self.child.last
                self.child = Node(self, self.interval.right_half(), self.T, self.epsilon, False)
            else:
                self.last = self.value + self.noise
                self.is_full = True
        return self.last
