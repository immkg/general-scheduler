from StaticVariables import *
import numpy as np

def bic0(t, s, g, n):
    truth = [
        (StaticVariables.duration[(t, s, g, n)] > 0)
    ]
    return np.prod(truth)


def bic1(t, s, g, n, d, p1, p2):
    truth = [
        (p1 >= np.min(StaticVariables.periods[d])),
        (p1 <= np.max(StaticVariables.periods[d]) - StaticVariables.duration[(t, s, g, n)] + 1),
        (p2 >= p1),
        (p2 <= p1 + StaticVariables.duration[(t, s, g, n)] - 1)
    ]
    return np.prod(truth)


def bic2(t, s, g, n, d, p1, p2):
    truth = [
        (p1 <= p2),
        (p1 >= p2 - StaticVariables.duration[(t, s, g, n)] + 1),
        (p1 >= np.min(StaticVariables.periods[d])),
        (p1 <= np.max(StaticVariables.periods[d]) - StaticVariables.duration[(t, s, g, n)] + 1)
    ]
    return np.prod(truth)


def bic3(d, p):
    truth = [
        (p <= np.max(StaticVariables.periods[d])),
        (p >= np.min(StaticVariables.periods[d]))
    ]
    return np.prod(truth)


def bic4(d, p):
    truth = [
        (p in StaticVariables.periods[d])
    ]
    return np.prod(truth)


def bic5(t, s, g, n, d, p):
    truth = [
        (p1 >= np.min(StaticVariables.periods[d])),
        (p1 <= np.max(StaticVariables.periods[d]) - StaticVariables.duration[(t, s, g, n)] + 1)
    ]
    return np.prod(truth)


def bic6(t, s, g, n):
    # this means tsgn belongs to lessons[t] and to lessons[g]
    truth = [
        (StaticVariables.duration[(t, s, g, n)] > 0)
    ]
    return np.prod(truth)


def bic7(d):
    truth = [
        (d in StaticVariables.days)
    ]
    return np.prod(truth)


def bic8(k, d, p):
    truth = [
        (k >= 1),
        (k <= len(StaticVariables.periods[d]) - 2),
        (p >= np.min(StaticVariables.periods[d]) + 1),
        (p <= np.max(StaticVariables.periods[d]) - k)
    ]
    return np.prod(truth)


def bic9(k, d):
    truth = [
        (k >= 1),
        (k <= len(StaticVariables.periods[d]) - 2)
    ]
    return np.prod(truth)


def bic10(k, d, p):
    truth = [
        (p >= np.min(StaticVariables.periods[d]) + 1),
        (p <= np.max(StaticVariables.periods[d]) - k)
    ]
    return np.prod(truth)


def bic11(d, p):
    truth = [
        (p >= np.min(StaticVariables.periods[d]) + 1),
        (p <= np.max(StaticVariables.periods[d]) - 1)
    ]
    return np.prod(truth)


def bic12(k, d, p):
    truth = [
        (k >= 1),
        (k <= np.max(StaticVariables.periods[d]) - p)
    ]
    return np.prod(truth)


def bic13(d, p):
    truth = [
        (p >= np.min(StaticVariables.periods[d])),
        (p <= np.max(StaticVariables.periods[d]))
    ]
    return np.prod(truth)


def ric1(t, s, g, n, r):
    truth = [
        (r in StaticVariables.room_dict[(t, s, g, n)])
    ]
    return np.prod(truth)
