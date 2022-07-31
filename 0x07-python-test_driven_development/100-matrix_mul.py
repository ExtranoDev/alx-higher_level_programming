#!/usr/bin/python3
"""
"""


def matrix_mul(m_a, m_b):
    """
    """
    arg_lst = [(m_a, 'm_a'), (m_b, 'm_b')]

    for val, nm in arg_lst:
        if val == [] or val == [[]]:
            raise ValueError("{} can't be empty".format(nm))
        if type(val) != list:
            raise TypeError("{} must be a list".format(nm))
        if not all(isinstance(i, list) for i in val):
            raise TypeError("{} must be a list of lists".format(nm))
        for eles in val:
            if not all(type(i) in (int, float) for i in eles):
                raise TypeError("{} should contain only"
                                " integers or floats".format(nm))
        val_len = len(val[0])
        if not all(len(i) == val_len for i in val):
            raise TypeError("each row of {} must be "
                            "of the same size".format(nm))

    if len(m_a[0]) == len(m_b):
        tp = (len(m_a), len(m_a[0]))
        vals = []

        for ma in m_a:
            ma_ct = 0
            tmp_ls = [0 for j in range(tp[1])]
            for mb in m_b:
                tmp_ct = 0
                while tmp_ct < len(mb):
                    tmp_ls[tmp_ct] += ma[ma_ct] * mb[tmp_ct]
                    tmp_ct += 1
                ma_ct += 1
            vals.append(tmp_ls)
        return vals
    else:
        raise ValueError("m_a and m_b can't be multiplied")
