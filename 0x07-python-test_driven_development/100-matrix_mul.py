#!/usr/bin/python3
"""
This Module defines a Matrix Multiplier

Function returns a multiplied Matrix
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrix

    Args:
        m_a (list): first matrix
        m_b (list): second matrix

    Raises:
        ValueError: all matrix must not be [] or [[]]
                    all matrix must be multiplyable
        TypeError: all matrix must be a list of lists
                    all matrix should only contain int or floats
                    all matrix must be of same size
    Returns:
        list: multiplied matrix
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
        vals = []

        for ma in m_a:
            ma_ct = 0
            tmp_ls = [0 for j in range(len(m_a))]
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
