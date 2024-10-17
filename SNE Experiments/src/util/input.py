from src.util.stream import Stream, Update


class Input:
    @staticmethod
    def read_input(file):
        first_line = file.readline().split(" ")
        T = int(first_line[0])
        n = int(first_line[1])
        stream = Stream()
        for i in range(T):
            new_line = file.readline().split(" ")
            u = Update(int(new_line[0]), int(new_line[1]))
            stream.update(u)
        return Input(stream, T, n)

    def __init__(self, stream, T, n):
        self.stream = stream
        self.T = T
        self.n = n
