class Norms:
    @staticmethod
    def L(p, x):
        res = 0
        for i in x:
            res += pow(abs(i), p)
        return pow(res, 1.0/p)

    @staticmethod
    def top_k(k, x):
        seq = sorted([abs(ele) for ele in x])
        res = 0
        for i in range(len(seq)-k,len(seq)):
            res += seq[i]
        return res


