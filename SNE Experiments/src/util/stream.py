class Stream:
    def __init__(self):
        self.updates = []

    def update(self, u):
        self.updates.append(u)

    def get(self, t):
        return self.updates[t]


class Update:

    def __init__(self, element, sign):
        self.element = element
        self.sign = sign
