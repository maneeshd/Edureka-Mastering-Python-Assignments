"""
@author: Maneesh D
@date: 30-May-17
@intepreter: Python 3.6

Create below matrix using scipy.
"""
import numpy as np
import scipy.sparse


N = 10
diag = np.zeros(N) + 2
udiag = np.zeros(N) + 1
ldiag = np.zeros(N) + 1
mat = scipy.sparse.dia_matrix(([diag, udiag, ldiag], [0, 2, -2]), shape=(N, N))
print(mat.todense())
