"""
@author: Maneesh D
@date: 30-May-17
@intepreter: Python 3.6

Create below matrix using scipy.
"""
from pprint import pprint

import numpy as np


def symmetrize(a):
    return (a + a.T) // 2

matrix = np.ones((10, 10), dtype=np.int64)
np.fill_diagonal(matrix, 2)

pprint(symmetrize(matrix))
