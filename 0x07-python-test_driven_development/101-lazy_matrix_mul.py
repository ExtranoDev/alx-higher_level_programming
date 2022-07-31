#!/usr/bin/python3
"""
This Module Multiplies Matrix using Numpy

Function returns a multiplied Matrix
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrix

    Args:
        m_a (list): first matrix
        m_b (list): second matrix

    Returns:
        list: multiplied matrix
    """
    return np.matmul(m_a, m_b)
