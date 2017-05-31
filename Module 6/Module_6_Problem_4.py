"""
@author: Maneesh D
@date: 30-May-17
@intepreter: Python 3.6
"""
from pylab import *


n = 256
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
Y = np.sin(2*X)
g = plot(X, Y+1, color='blue', alpha=1.00)
plot(X, Y-1, color='red', alpha=1.00)
show(g)
