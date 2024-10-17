from scipy.stats import laplace


class Laplace:
    @staticmethod
    def noise(b):
        return laplace.rvs(0., b)
