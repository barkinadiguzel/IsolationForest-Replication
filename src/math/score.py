import math

def H(n):
    if n > 0:
        return sum(1.0 / i for i in range(1, n + 1))
    return 0

def c_n(n):
    if n <= 1:
        return 0
    return 2 * H(n - 1) - (2 * (n - 1) / n)

def anomaly_score(hx_avg, n):
    cn = c_n(n)
    return 2 ** (-hx_avg / cn)
