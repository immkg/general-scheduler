import numpy as np


class StaticVariables():
    """docstring for StaticVariables"""
    or_head = 'or'
    and_head = 'and'
    not_head = 'not'
    p_max = 8
    days = list(range(6))
    num_t = 8
    num_s = 4
    num_g = 5
    teachers = np.array(list(range(num_t)))
    subjects = np.array(list(range(num_s)))
    groups = np.array(list(range(num_g)))

    periods = []
    for _ in range(len(days)):
        periods.append(np.array(list(range(p_max))))

    duration = {
        (0, 0, 0, 1): 3,
        (0, 0, 1, 2): 3,
        (0, 0, 2, 3): 3
    }

    rooms = 7

    '''
    (t, s, g, n) = [room_set]
    '''

    room_dict = {}

    tdata = {
        "24-04-1996": [0, 1],
        "30-05-1992": [1, 2, 3],
        "10-17-1888": [3, 5, 9, 11]
    }

    sdata = {
        0: [3, 4],
        1: [3, 5],
        2: [3, 0],
        3: [2, 1, 6],
        4: [12, 11],
        5: [7, 9],
        6: [9, 3, 5],
        7: [0, 7],
        8: [8],

    }
