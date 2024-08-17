from var import *


def bic0(t, s, g, n):
    truth = [
        (duration[(t, s, g, n)] > 0)
    ]
    return np.prod(truth)


def bic1(t, s, g, n, d, p1, p2):
    truth = [
        (p1 > np.min(periods[d])),
        (p1 <= np.max(periods[d]) - duration[(t, s, g, n)] + 1),
        (p2 >= p1),
        (p2 <= p1 + duration[(t, s, g, n)] - 1)
    ]
    return np.prod(truth)


def bic2(t, s, g, n, d, p1, p2):
    truth = [
        (p1 <= p2),
        (p1 >= p2 - duration[(t, s, g, n)] + 1),
        (p1 >= np.min(periods[d])),
        (p1 <= np.max(periods[d]) - duration[(t, s, g, n)] + 1)
    ]
    return np.prod(truth)


def bic3(d, p):
    truth = [
        (p <= np.max(periods[d])),
        (p >= np.min(periods[d]))
    ]
    return np.prod(truth)


def bic4(d, p):
    truth = [
        (p in periods[d])
    ]
    return np.prod(truth)


def bic5(t, s, g, n, d, p):
    truth = [
        (p1 >= np.min(periods[d])),
        (p1 <= np.max(periods[d]) - duration[(t, s, g, n)] + 1)
    ]
    return np.prod(truth)


def bic6(t, s, g, n):
    # this means tsgn belongs to lessons[t] and to lessons[g]
    truth = [
        (duration[(t, s, g, n)] > 0)
    ]
    return np.prod(truth)


def bic7(d):
    truth = [
        (d in days)
    ]
    return np.prod(truth)


def bic8(k, d, p):
    truth = [
        (k >= 1),
        (k <= len(periods[d]) - 2),
        (p >= np.min(periods[d]) + 1),
        (p <= np.max(periods[d]) - k)
    ]
    return np.prod(truth)


def bic9(k, d):
    truth = [
        (k >= 1),
        (k <= len(periods[d]) - 2)
    ]
    return np.prod(truth)


def bic10(k, d, p):
    truth = [
        (p >= np.min(periods[d]) + 1),
        (p <= np.max(periods[d]) - k)
    ]
    return np.prod(truth)


def bic11(d, p):
    truth = [
        (p >= np.min(periods[d]) + 1),
        (p <= np.max(periods[d]) - 1)
    ]
    return np.prod(truth)


def bic12(k, d, p):
    truth = [
        (k >= 1),
        (k <= np.max(periods[d]) - p)
    ]
    return np.prod(truth)


def bic13(d, p):
    truth = [
        (p >= np.min(periods[d])),
        (p <= np.max(periods[d]))
    ]
    return np.prod(truth)


def negation(var):
    var_to_modify = list(var)
    if var[0][0] == '~':
        var_to_modify[0] = var[0][1:]
    else:
        var_to_modify[0] = '~' + var[0]
    return tuple(var_to_modify)


def single(vars):
    and_list = []
    k = len(vars)
    for j in range(k):
        for i in range(j):
            and_list.append(('or', [
                negation(vars[i]),
                negation(vars[j])
            ]))
    return ('and', and_list)


def together(groups, t, s, n):
    '''
    Condition that is satisfied when all groups specified
    have the lesson tsn at the same time
    '''

    and_list = []
    k = len(groups)
    for j in range(k):
        and_list.append(('or', [
                        ('and', [groups[j],
                                 groups[j + 1]]),
                        ('and', [negation(groups[j]),
                                 negation(groups[j + 1])])
                        ]))
    return

# def cardinality(vars, k):
